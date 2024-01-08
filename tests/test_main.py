import pytest
from src.utils import (format_card_number, format_account_number, sort_by_date,
                       print_last_5_operations)


@pytest.mark.parametrize("input_number, expected_output", [
	("1234567890123456", "1234 56** **** 3456"),
	("9876543210987654", "9876 54** **** 7654"),
])
def test_format_card_number(input_number, expected_output):
	"""
	Тест функции format_card_number.
	:param input_number: Входной номер карты.
	:param expected_output: Ожидаемый замаскированный номер карты.
	"""
	assert format_card_number(input_number) == expected_output


@pytest.mark.parametrize("input_number, expected_output", [
	("123456789", "**6789"),
	("987654321", "**4321"),
])
def test_format_account_number(input_number, expected_output):
	"""
	Тест функции format_account_number.
	:param input_number: Входной номер счета.
	:param expected_output: Ожидаемый замаскированный номер счета.
	"""
	assert format_account_number(input_number) == expected_output


def test_sort_by_date(example_operations):
	"""
	Тест функции sort_by_date.
	:param example_operations (list): Список примеров операций.
	"""
	sorted_operations = sorted(example_operations, key=sort_by_date)
	assert sorted_operations[0]["date"] == "2022-01-01T12:00:00.000000"
	assert sorted_operations[2]["date"] == "2022-01-03T12:00:00.000000"


def test_print_last_5_operations(capsys, operations_data):
	"""
	Тест функции print_last_5_operations.
	:param capsys: Pytest фикстура для захвата вывода.
	:param operations_data: Список данных об операции.
	"""
	print_last_5_operations(operations_data)
	captured = capsys.readouterr()
	assert "08.12.2019 Открытие вклада" in captured.out
	assert "07.12.2019 Перевод организации" in captured.out
