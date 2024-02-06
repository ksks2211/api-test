# api-test

`api-test` is a Python library designed for personal use to facilitate learning, testing, and experimenting with RESTful APIs. It includes simple use cases of RESTful APIs.

## Installation

To install the library, you can use the following pip command:

```bash
pip install git+https://github.com/ksks2211/api-test
```

## Features

`api-test` offers the following features:

- **Quotes API**: Fetch random quotes.
- **OpenWeatherMap API**: Retrieve weather information by city name. Requires an API key set as `OWM_API_KEY`.


## Environment Configuration

For the library to function properly, especially when accessing APIs that require keys, you need to set up environment variables. Create a `.env` file in the root directory of your project and fill in the necessary API keys.

Example `.env` file:

```plaintext
# .env.example
XXX_XXX_KEY=
```

Fill in `XXX_XXX_KEY` with your API key. This key will be loaded into your application to authenticate API requests.


## Usage

### Fetching Quotes

To get random quotes:

```python
from api_test.quotes import get_quotes
quotes = get_quotes()
```

### Getting Weather Information

To fetch weather information for a specific city:

```python
from api_test.weather import get_weather_by_city
city_name = "London"
london_weather = get_weather_by_city(city_name)
```

**Note**: Ensure you have set your OpenWeatherMap API key as `OWM_API_KEY` in your environment variables.

## Utilities

The library includes a set of utility functions within `common.py` for JSON data manipulation, such as `to_json`, `save_json`, and `save_dict_as_json`, among others. These functions assist in converting data to JSON strings, saving JSON strings to files, and saving dictionaries as JSON files.
