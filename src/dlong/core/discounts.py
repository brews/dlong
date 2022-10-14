"""
Discounting strategies to apply to Damages
"""
from ..types import Damages, DiscountedDamages


class FractionalDiscount:
    """
    Discounting strategy for fractional discounts from a reference period

    Parameters
    ----------
    rate :
        Fractional discount rate. Note, this is not a percentage.
    reference_year :
        Reference year from which to apply the discounting rate.
    """

    def __init__(self, *, rate: int | float, reference_year: int):
        self.rate = rate
        self.reference_year = reference_year

    def __repr__(self):
        return f"{type(self).__name__}(rate={self.rate!r}, reference_year={self.reference_year!r})"

    def __eq__(self, other):
        return (
            self.rate == other.rate
            and self.reference_year == other.reference_year
            and type(self) == type(other)
        )

    def apply(self, damages: Damages) -> DiscountedDamages:
        """
        Apply discounting to given damages
        """
        # TODO: Not sure about the damages.year below. Should be "time"? Are these always going to be annual.
        return damages / (1 + self.rate) ** (damages.year - self.reference_year)
