"""
Contains various recipes for calculating damages from hazards and then applying discounting.
"""

from ..types import (
    DamageModel,
    Discount,
    Damages,
    DiscountedDamages,
    ClimateData,
)


class ExampleRecipe:
    """
    An example basic recipe combining damage function, discounting and hazard data.
    """

    def __init__(
        self,
        *,
        climate: ClimateData,
        damage_function: DamageModel,
        discount: Discount,
    ):
        self.climate = climate
        self.damage_function = damage_function
        self.discount = discount

    def damages(self) -> Damages:
        """
        Compute un-discounted damages.
        """
        return self.damage_function.project(x=self.climate)

    def discounted_damages(self) -> DiscountedDamages:
        """
        Compute discounted damages.
        """
        return self.discount.apply(self.damages())
