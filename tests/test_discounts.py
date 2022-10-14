from dlong.core.discounts import FractionalDiscount
import xarray as xr


def test_fractionaldiscount_repr():
    """
    Test that FractionalDiscount's repr magic can create equal instance.
    """
    original_discount_strategy = FractionalDiscount(rate=0.02, reference_year=2020)
    new_discount_strategy = eval(repr(original_discount_strategy))
    assert new_discount_strategy == original_discount_strategy


def test_fractionaldiscount_eq_pass():
    """
    Test that FractionalDiscount's eq magic passes equal discounts.
    """
    discount_strategy_a = FractionalDiscount(rate=0.02, reference_year=2020)
    discount_strategy_b = FractionalDiscount(rate=0.02, reference_year=2020)
    assert discount_strategy_a == discount_strategy_b


def test_fractionaldiscount_eq_unequal():
    """
    Test that FractionalDiscount's eq magic sees unequal discounts.
    """
    discount_strategy_a = FractionalDiscount(rate=0.02, reference_year=2020)
    discount_strategy_b = FractionalDiscount(rate=0.03, reference_year=2021)
    assert discount_strategy_a != discount_strategy_b


def test_fractionaldiscount_apply():
    """
    Test that FractionalDiscount can be applied to Damages.
    """
    # Damages currently require a "year" dim for FractionalDiscount...
    input_damages = xr.DataArray(
        [100.0, 100.0, 100.0], coords=[[-1, 0, 1]], dims="year"
    )
    expected_discounted_damages = xr.DataArray(
        [400.0, 100.0, 25], coords=[[-1, 0, 1]], dims="year"
    )

    # Choosing this rate so we avoid float point problems.
    discount = FractionalDiscount(rate=3.0, reference_year=0)
    actual_discounted_damages = discount.apply(input_damages)

    xr.testing.assert_equal(actual_discounted_damages, expected_discounted_damages)
