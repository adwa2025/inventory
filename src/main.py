"""Entry point for the Employee Training Application."""

import json
from argparse import ArgumentParser
from inventory.presentation_layer.user_interface import UserInterface
from inventory.persistence_layer.mysql_persistence_wrapper import MySQLPersistenceWrapper


def main():
	"""Entry point."""
	args = configure_and_parse_commandline_arguments()

	if args.configfile:
		config = None
		with open(args.configfile, 'r') as f:
			config = json.loads(f.read())

	# initiate the mysql connection
	db = MySQLPersistenceWrapper(config)
	suppliers_list = db.select_all_suppliers()
	for supplier in suppliers_list:
		print(f"{supplier}")

	print("*"*40)
	suppliers_list = db.select_all_suppliers()
	for supplier in suppliers_list:
		print(f"Supplier {supplier[0]}: {supplier[1]}") # Supplier 1: 
		parts = db.select_all_parts_for_supplier_id(supplier[0])
		for part in parts:
			print(f"{part}")
			
		


def configure_and_parse_commandline_arguments():
	"""Configure and parse command-line arguments."""
	parser = ArgumentParser(
	prog='main.py',
	description='Start the application with a configuration file.',
	epilog='POC: Your Name | your@email')

	parser.add_argument('-c','--configfile',
					help="Configuration file to load.",
					required=True)
	args = parser.parse_args()
	return args



if __name__ == "__main__":
	main()