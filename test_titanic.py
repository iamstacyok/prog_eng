import pytest
import pandas as pd
from lab3_1 import change_port_names, filter_by_age, get_results

@pytest.fixture
def df():
    data = {
        'Sex':      ['male', 'male', 'male', 'female', 'male', 'male', 'female', 'male'],
        'Age':      [25, 35, 45, 30, 50, 20, 40, 60],
        'Survived': [0, 1, 0, 1, 0, 1, 0, 0],
        'Embarked': ['C', 'Q', 'S', 'C', 'Q', 'S', 'C', 'S']
    }
    return pd.DataFrame(data)

def test_change_port_names(df):
    #arrange
    expected_ports = ['Шербур', 'Квинстаун', 'Саутгемптон', 'Шербур', 'Квинстаун', 'Саутгемптон', 'Шербур',
                      'Саутгемптон']
    #act
    actual_ports = change_port_names(df)['Embarked'].tolist()
    #assert
    assert expected_ports == actual_ports

def test_filter_by_age(df):
    #arrange
    age_limit = 30
    #act
    filtered = filter_by_age(df, age_limit)
    #assert
    assert len(filtered) == 3
    assert all(filtered['Sex'] == 'male')
    assert all(filtered['Age'] > age_limit)
    assert all(filtered['Survived'] == 0)

def test_get_results(df):
    #arrange
    filtered = filter_by_age(change_port_names(df), 30)
    expected_embarked = ['Квинстаун', 'Саутгемптон']
    expected_embarked_counts = [1, 2]
    #act
    result = get_results(filtered)
    print(result)
    #assert
    assert list(result['Embarked']) == expected_embarked
    assert list(result['Погибших мужчин старше указанного возраста']) == expected_embarked_counts
