import requests
import pytest

url = "https://api.openbrewerydb.org/"


@pytest.mark.parametrize('cityes', [
    "san_diego",
    "moscow",
    "paris",
    "washington",
    "sidney"
])
def test_by_city(cityes):
    json = requests.get(url + "breweries?by_city=" + cityes).json()
    assert len(json) != 0


@pytest.mark.parametrize('ids', range(1, 10))
def test_by_ids(ids):
    json = requests.get(url + "breweries/" + str(ids)).json()
    assert len(json) != 0


@pytest.mark.parametrize('queryes', [
    "akita",
    "moll",
    "spencer",
    "lily",
    "faust",
    "ground",
    "best"
])
def test_search(queryes):
    json = requests.get(url + "breweries/search?query=" + queryes).json()
    assert len(json) != 0


@pytest.mark.parametrize('queryes', [
    "moll",
    "spencer",
    "lily",
    "faust",
    "ground",
    "best"
])
def test_autocomplete(queryes):
    json = requests.get(url + "breweries/autocomplete?query=" + queryes).json()
    assert (len(json) != 0) & (queryes in json[0]['name'].lower())