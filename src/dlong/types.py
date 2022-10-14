from dataclasses import dataclass
from typing import Protocol
from xarray import Dataset, DataArray


Damages = DataArray
DiscountedDamages = DataArray

# TODO: Should require "beta0", "beta1" and "beta2" variables in this
QuadraticDamageCoefficients = Dataset


@dataclass
class ClimateData:
    temperature: DataArray


class DamageModel(Protocol):
    def project(self, x: ClimateData) -> Damages:
        """
        A DamageModel can project damages given Hazards data
        """


class Discount(Protocol):
    def apply(self, damages: Damages) -> DiscountedDamages:
        """A Discount can be applied Damages"""
