"""
Damage models to project damages from hazards
"""

from ..types import Damages, ClimateData, QuadraticDamageCoefficients


class QuadraticDamageModel:
    """
    Example implementation of the dlong.types.DamageModel protocol.

    Damages are computed from input "temperature", given coefficients. Has a quadratic functional form.

    Parameters
    ----------
    coefs:
        Damage function coefficients.
    """

    def __init__(self, coefs: QuadraticDamageCoefficients):
        self.coefs = coefs

    def __repr__(self):
        return f"{type(self).__name__}(coefs={self.coefs!r})"

    def project(self, x: ClimateData) -> Damages:
        """
        Project damages from "temperature"

        This is a quadratic function.
        """
        y = (
            self.coefs.beta0
            + self.coefs.beta1 * x.temperature
            + self.coefs.beta2 * x.temperature**2
        )
        return y
