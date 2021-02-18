# Coffee API

## Description and Features

* The Project consists of mainly two models: CoffeeMachine and CoffeePod.
* The project has **Continous integration** and **Continous deployment** using github actions and heroku (check github repository)
* The endpoints are documented using swagger and redoc, and can be found on the relevant urls `/swagger/` and `/redoc/`
* Browasable API in the root url.
* Admin page to manipulate data directly on `/admin/` with username = `admin` and password = `changeme`
* machines enpoint can be filtered by : `product_type`, `water_line_compatible`, `model_type`.
* pods endpoint can be filtered by: `product_type`, `coffee_flavor` , `pack_size`.
* On every push, code is checked against static validation tools (black, isort and bandit) and unit tests are run.
