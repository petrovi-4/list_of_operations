import json
import os.path
from utils import print_last_5_operations

if __name__ == "__main__":
	file_path = os.path.join(os.path.dirname(__file__), "..", "operations.json")
	with open(file_path, "r", encoding="utf-8") as file:
		operations_data = json.load(file)

	print_last_5_operations(operations_data)
