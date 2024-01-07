import pytest
from src.main import (format_card_number, format_account_number, sort_by_date,
                      print_last_5_operations)


@pytest.mark.parametrize("input_number, expected_output", [
    ("1234567890123456", "123456 XX** **** 3456"),
    ("9876543210987654", "987654 XX** **** 7654"),
])
def test_format_card_number(input_number, expected_output):
	assert format_card_number(input_number) == expected_output


@pytest.mark.parametrize("input_number, expected_output", [
    ("123456789", "**6789"),
    ("987654321", "**4321"),
])
def test_format_account_number(input_number, expected_output):
	assert format_account_number(input_number) == expected_output


def test_sort_by_date(example_operations):
	sorted_operations = sorted(example_operations, key=sort_by_date)
	assert sorted_operations[0]["date"] == "2022-01-01T12:00:00.000000"
	assert sorted_operations[2]["date"] == "2022-01-03T12:00:00.000000"


def test_print_last_5_operations(capsys, operations_data):
	print_last_5_operations(operations_data)
	captured = capsys.readouterr()
	assert "08.12.2019 Открытие вклада" in captured.out
	assert "07.12.2019 Перевод организации" in captured.out
