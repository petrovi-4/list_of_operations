import json
from datetime import datetime as dt


def format_card_number(card_number):
	if card_number:
		masked_number = card_number[:6] + " XX** **** " + card_number[-4:]
		return masked_number
	return ""


def format_account_number(account_number):
	if account_number:
		masked_number = "**" + account_number[-4:]
		return masked_number
	return ""


def sort_by_date(operation):
	return dt.strptime(operation["date"], '%Y-%m-%dT%H:%M:%S.%f')


def print_last_5_operations(operations):
	executed_operations = [operation for operation in operations if "state" in
	                       operation and operation["state"] == "EXECUTED"]
	executed_operations = sorted(executed_operations, key=sort_by_date,
	                             reverse=True)[:5]

	for operation in executed_operations:
		date = dt.strptime(operation["date"],
		                   "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
		description = operation["description"]
		from_account = format_card_number(operation.get("from", ""))
		to_account = format_account_number(operation["to"])
		amount = float(operation['operationAmount']['amount'])
		currency = operation['operationAmount']['currency']['name']

		print(f"{date} {description}\n{from_account} -> {to_account}\n"
		      f"{amount} {currency}\n")


if __name__ == "__main__":
	with open("../operations.json", "r", encoding="utf-8") as file:
		operations_data = json.load(file)

	print_last_5_operations(operations_data)
