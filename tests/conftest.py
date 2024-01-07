import os
import json
import pytest
from src.main import (format_card_number, format_account_number, sort_by_date,
                      print_last_5_operations)


@pytest.fixture
def operations_data():
	file_path = os.path.join(os.path.dirname(__file__), "..", "operations.json")
	with open(file_path, "r", encoding="utf-8") as file:
		return json.load(file)


@pytest.fixture
def example_operations():
	return [
		{"date": "2022-01-01T12:00:00.000000"},
		{"date": "2022-01-02T12:00:00.000000"},
		{"date": "2022-01-03T12:00:00.000000"}
	]