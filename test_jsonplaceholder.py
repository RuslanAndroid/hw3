import requests
import pytest

url = "https://jsonplaceholder.typicode.com/posts/"


@pytest.mark.parametrize('ids', range(1, 5))
def test_by_ids(ids):
    json = requests.get(url + str(ids)).json()
    assert len(json) != 0


@pytest.mark.parametrize('userId', range(1, 5))
def test_post_data(userId):
    json = requests.post(
        url=url,
        data={'title': "her",
              'body': 'bar',
              'userId': userId
              }).json()
    assert int(json['userId']) == userId


@pytest.mark.parametrize('userId', range(1, 5))
def test_filter_data(userId):
    json = requests.get(url + '?userId=' + str(userId)).json()
    assert len(json) > 0


@pytest.mark.parametrize('post, title', [('1', 'term'), ('2', 'frol'), ('10', 'must')])
def test_patch_data(post, title):
    json = requests.patch(
        url=url + post,
        data={'title': title}).json()
    assert json['title'] == title


def test_delete_data():
    code = requests.delete(url=url + '1/').status_code
    assert code == 200
