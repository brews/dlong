[![pythonpackage](https://github.com/brews/dlong/actions/workflows/pythonpackage.yml/badge.svg)](https://github.com/brews/dlong/actions/workflows/pythonpackage.yml)
[![codecov](https://codecov.io/gh/brews/dlong/branch/main/graph/badge.svg?token=NZI5NI6RSH)](https://codecov.io/gh/brews/dlong)

# dlong
Prototype framework for projected socio-economic climate damages

This is a prototype. It is likely to change in breaking ways. It might delete all your data so don't use it in production.

## Examples
```python
import dlong
from dlong.types import ClimateData
import xarray as xr

# First, let's make some demo data.
# Say 3 years of annual temperature data across 3 regions:
region = [1, 2, 3]
year = [2019, 2020, 2021]
input_temperature = xr.DataArray(
    [[1.0, 2.0, 3.0], [2.0, 3.0, 4.0], [3.0, 4.0, 5.0]],
    coords=[region, year],
    dims=["region", "year"],
)
# And here are coefficients for a quadratic damage function. Different for 
# each region.
damage_coefficients = xr.Dataset(
    data_vars={
        "beta0": (["region"], [1, 1, 1]),
        "beta1": (["region"], [1, 2, 3]),
        "beta2": (["region"], [4, 5, 6]),
    },
    coords={"region": (["region"], region)},
)

# Put it all together to describe climate data, a damage function, and
# a strategy for discounting damages.
climate = dlong.types.ClimateData(temperature=input_temperature)
damage_model = dlong.QuadraticDamageModel(coefs=damage_coefficients)
discount_strategy = dlong.FractionalDiscount(rate=0.02, reference_year=2020)
# We could use these individually, or combine them into a "recipe" to output 
# discounted damages. The idea is that these components are compositable
# so components can be customized and run in large batches.
recipe = dlong.ExampleRecipe(
    climate=climate, damage_function=damage_model, discount=discount_strategy
)
damages = recipe.discounted_damages()
#<xarray.DataArray (region: 3, year: 3)>
#array([[  6.12      ,  19.        ,  39.21568627],
#       [ 25.5       ,  52.        ,  87.25490196],
#       [ 65.28      , 109.        , 162.74509804]])
#Coordinates:
#* region   (region) int64 1 2 3
#* year     (year) int64 2019 2020 2021
```

## Installation
```shell
pip install dlong
```

`dlong` currently requires Python > 3.8 and the `xarray` package.

Install the unreleased bleeding-edge version of the package with:
```shell
pip install git+https://github.com/brews/dlong
```

## Support
Source code is available online at https://github.com/brews/dlong/. This software is Open Source and available under the Apache License, Version 2.0.

## Development

Please file bugs in the [bug tracker](https://github.com/brews/dlong/issues).

Want to contribute? Great! Fork the main branch and file a pull request when you're ready. Please be sure to write unit tests and follow [pep8](https://www.python.org/dev/peps/pep-0008/). Fork away!
