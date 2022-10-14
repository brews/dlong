from dlong.core.damages import QuadraticDamageModel
from dlong.types import ClimateData
import xarray as xr


def test_quadraticdamagemodel_project():
    """
    Test that QuadraticDamageModel.project() gives correct numbers in simple case.
    """
    idx = [1, 2, 3]
    input_coefs = xr.Dataset(
        data_vars={
            "beta0": (["idx"], [1, 1, 1]),
            "beta1": (["idx"], [1, 2, 3]),
            "beta2": (["idx"], [4, 5, 6]),
        },
        coords={"idx": (["idx"], idx)},
    )
    input_temperature = xr.DataArray([-1.0, 0.0, 1.0], coords=[idx], dims="idx")
    climate = ClimateData(temperature=input_temperature)

    expected_damages = xr.DataArray([4.0, 1.0, 10.0], coords=[idx], dims="idx")

    damage_model = QuadraticDamageModel(coefs=input_coefs)
    actual_damages = damage_model.project(x=climate)
    xr.testing.assert_equal(actual_damages, expected_damages)


def test_quadraticdamagemodel_repr():
    """
    Test that QuadraticDamageModel's repr magic spits out a str.
    """
    input_coefs = xr.Dataset(
        data_vars={
            "beta0": (["idx"], [0, 0, 0]),
            "beta1": (["idx"], [1, 2, 3]),
            "beta2": (["idx"], [4, 5, 6]),
        },
        coords={"idx": (["idx"], [1, 2, 3])},
    )

    damage_model = QuadraticDamageModel(coefs=input_coefs)
    damage_model_str = repr(damage_model)
    assert isinstance(damage_model_str, str)
