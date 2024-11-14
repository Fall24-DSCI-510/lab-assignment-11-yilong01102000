import pytest

from run import (
    preprocess_data,
    species_count,
    average_sepal_length,
    max_petal_width,
    min_petal_length,
    count_sepal_length_above_5,
    count_petal_length_below_2,
    get_sepal_width_above_3_5,
    species_count_petal_width_above_1_5,
    get_virginica_petal_length_above_6,
    get_largest_sepal_width,
)

data_file = "iris.data"  # Replace with the correct path to your Iris dataset

def test_preprocess_data():
    preprocessed = preprocess_data(data_file)
    assert len(preprocessed) == 138, "Unexpected number of rows after preprocessing"
    assert "ID" in preprocessed.columns, "ID column is missing after preprocessing"

def test_species_count():
    result = species_count(data_file)
    expected = {'Iris-versicolor': 49, 'Iris-setosa': 45, 'Iris-virginica': 44}
    assert result == expected, f"Expected {expected}, but got {result}"

def test_average_sepal_length():
    result = average_sepal_length(data_file)
    expected = 5.8
    assert result == expected, f"Expected {expected}, but got {result}"

def test_max_petal_width():
    result = max_petal_width(data_file)
    expected = 2.5
    assert result == expected, f"Expected {expected}, but got {result}"

def test_min_petal_length():
    result = min_petal_length(data_file)
    expected = 1.0
    assert result == expected, f"Expected {expected}, but got {result}"

def test_count_sepal_length_above_5():
    result = count_sepal_length_above_5(data_file)
    expected = 107
    assert result == expected, f"Expected {expected}, but got {result}"

def test_count_petal_length_below_2():
    result = count_petal_length_below_2(data_file)
    expected = 45
    assert result == expected, f"Expected {expected}, but got {result}"

def test_get_sepal_width_above_3_5():
    result = get_sepal_width_above_3_5(data_file)
    expected = [4, 5, 10, 14, 16, 17, 19, 20, 40, 42, 44, 103]
    assert result == expected, f"Expected {expected}, but got {result}"

def test_species_count_petal_width_above_1_5():
    result = species_count_petal_width_above_1_5(data_file)
    expected = {'Iris-virginica': 41, 'Iris-versicolor': 5}
    assert result == expected, f"Expected {expected}, but got {result}"

def test_get_virginica_petal_length_above_6():
    result = get_virginica_petal_length_above_6(data_file)
    expected = [101, 103, 121]
    assert result == expected, f"Expected {expected}, but got {result}"

def test_get_largest_sepal_width():
    result = get_largest_sepal_width(data_file)
    expected = 5
    assert result == expected, f"Expected {expected}, but got {result}"


