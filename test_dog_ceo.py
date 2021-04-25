import requests
import pytest

url = "https://dog.ceo/api/"


@pytest.mark.parametrize('images_count', [1, 2, 3])
def test_success(images_count):
    json = requests.get(url + "breeds/image/random/" + str(images_count)).json()
    assert len(json['message']) == images_count


@pytest.mark.parametrize('breeds', [
    "affenpinscher",
    "african",
    "airedale",
    "akita",
    "appenzeller",
    "chow",
    "mexicanhairless"
])
def test_by_breed(breeds):
    json = requests.get(url + "breed/" + breeds + "/images/random/").json()
    assert (json['status'] == "success") & (breeds in json['message'])


def test_difference():
    first_image = requests.get(url + "breeds/image/random/").json()['message']
    second_image = requests.get(url + "breeds/image/random/").json()['message']
    assert first_image != second_image


def test_breeds():
    breeds = requests.get(url + "breeds/list/all").json()['message']
    assert len(breeds) == 95
