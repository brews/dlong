from dlong.core.recipes import ExampleRecipe
from dlong import FractionalDiscount
from dlong import QuadraticDamageModel
from dlong.types import ClimateData
import xarray as xr


def test_examplerecipe():
    """
    Integration test between ExampleRecipe, QuadraticDamageModel, FractionalDiscount
    """
    # Creating a few things to get this set up and put into ExampleRecipe.
    region = [1, 2, 3]
    year = [2019, 2020, 2021]

    input_temperature = xr.DataArray(
        [[1.0, 2.0, 3.0], [2.0, 3.0, 4.0], [3.0, 4.0, 5.0]],
        coords=[region, year],
        dims=["region", "year"],
    )

    damage_coefficients = xr.Dataset(
        data_vars={
            "beta0": (["region"], [1, 1, 1]),
            "beta1": (["region"], [1, 2, 3]),
            "beta2": (["region"], [4, 5, 6]),
        },
        coords={"region": (["region"], region)},
    )

    expected_discounted_damages = xr.DataArray(
        [[6.12, 19.0, 39.215686], [25.5, 52.0, 87.254902], [65.28, 109, 162.745098]],
        coords=[region, year],
        dims=["region", "year"],
    )

    # Put it all together into ExampleRecipe...
    climate = ClimateData(temperature=input_temperature)
    damage_model = QuadraticDamageModel(coefs=damage_coefficients)
    discount_strategy = FractionalDiscount(rate=0.02, reference_year=2020)
    recipe = ExampleRecipe(
        climate=climate, damage_function=damage_model, discount=discount_strategy
    )
    actual_discounted_damages = recipe.discounted_damages()

    xr.testing.assert_allclose(actual_discounted_damages, expected_discounted_damages)
