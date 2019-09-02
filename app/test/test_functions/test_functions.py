import pytest
from app.main.functions import check_required_keys


@pytest.mark.parametrize('keys,element,result', [
    (
        ('key1', 'key2', 'key3', 'key4'),
        {
            'key1': 1,
            'key2': 2,
            'key3': 3,
            'key4': 4
        },
        True
    ),
    (
        ('key1', 'key2', 'key3', 'key4'),
        {
            'key1': 1,
            'key2': 2,
            'key3': 3,
        },
        False
    ),
    (
        (),
        {
            'key1': 1,
            'key2': 2,
            'key3': 3,
        },
        True
    ),
    (
        ('key1', 'key2', 'key3', 'key4'),
        {},
        False
    )

])
def test_check_required_keys(keys, element, result):
    assert check_required_keys(keys, element) == result
