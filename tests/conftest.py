import os
import json
import pytest


@pytest.fixture
def operations_data():
	"""
	Фикстура для загрузки данных об операциях из файла.
	:return list: Список данных об операциях.
	"""
	file_path = os.path.join(os.path.dirname(__file__), "..", "operations.json")
	with open(file_path, "r", encoding="utf-8") as file:
		return json.load(file)


@pytest.fixture
def example_operations():
	"""
	Фикстура для предоставления примерных данных об операциях.
	:return list: Список примеров операций.
	"""
	return [
		{"date": "2022-01-01T12:00:00.000000"},
		{"date": "2022-01-02T12:00:00.000000"},
		{"date": "2022-01-03T12:00:00.000000"}
	]