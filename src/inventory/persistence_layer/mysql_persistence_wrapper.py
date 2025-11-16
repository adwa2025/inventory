"""Defines the MySQLPersistenceWrapper class."""

from inventory.application_base import ApplicationBase
from mysql import connector
from mysql.connector.pooling import (MySQLConnectionPool)
import inspect
import json

class MySQLPersistenceWrapper(ApplicationBase):
	"""Implements the MySQLPersistenceWrapper class."""

	def __init__(self, config:dict)->None:
		"""Initializes object. """
		self._config_dict = config
		self.META = config["meta"]
		self.DATABASE = config["database"]
		super().__init__(subclass_name=self.__class__.__name__, 
				   logfile_prefix_name=self.META["log_prefix"])
		self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}:It works!')

		# Database Configuration Constants
		self.DB_CONFIG = {}
		self.DB_CONFIG['database'] = \
			self.DATABASE["connection"]["config"]["database"]
		self.DB_CONFIG['user'] = self.DATABASE["connection"]["config"]["user"]
		self.DB_CONFIG['password'] = self.DATABASE["connection"]["config"]["password"]
		self.DB_CONFIG['host'] = self.DATABASE["connection"]["config"]["host"]
		self.DB_CONFIG['port'] = self.DATABASE["connection"]["config"]["port"]

		self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}: DB Connection Config Dict: {self.DB_CONFIG}')

		# Database Connection
		self._connection_pool = \
			self._initialize_database_connection_pool(self.DB_CONFIG)
		

		# SQL String Constants
		self.SELECT_ALL_SUPPLIERS = \
			"SELECT id, name, location FROM suppliers"
		
		self.SELECT_ALL_SUPPLIERS_WITH_PARTS = \
			f"SELECT s.name AS Supplier, p.name AS Part, x.price, x.lead_time " \
			f"FROM suppliers s, parts p, supply_xref x " \
			f"WHERE x.supplier_id = s.id AND x.part_id = p.id"
		
		self.SELECT_ALL_PARTS_FOR_SUPPLIER_ID = \
			f"SELECT id, name, description, price, lead_time " \
			f"FROM parts, supply_xref " \
			f"WHERE (supplier_id = %s) AND (parts.id = part_id)"





	# MySQLPersistenceWrapper Methods
	def select_all_suppliers(self)->list:
		"""Selects all suppliers from the database."""
		cursor = None
		results = None
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.SELECT_ALL_SUPPLIERS)
					results = cursor.fetchall()
			return results
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: Problem selecting all suppliers: {e}')

	def select_all_suppliers_with_parts(self)->list:
		"""Selects all suppliers with their parts from the database."""
		cursor = None
		results = None
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.SELECT_ALL_SUPPLIERS_WITH_PARTS)
					results = cursor.fetchall()
			return results
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: Problem selecting all suppliers with parts: {e}')
	
	def select_all_parts_for_supplier_id(self, supplier_id:int)->list:
		"""Selects all parts for a given supplier ID from the database."""
		cursor = None
		results = None
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.SELECT_ALL_PARTS_FOR_SUPPLIER_ID, (supplier_id,))
					results = cursor.fetchall()
			return results
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: Problem selecting all parts for supplier ID {supplier_id}: {e}')







		##### Private Utility Methods #####

	def _initialize_database_connection_pool(self, config:dict)->MySQLConnectionPool:
		"""Initializes database connection pool."""
		try:
			self._logger.log_debug(f'Creating connection pool...')
			cnx_pool = \
				MySQLConnectionPool(pool_name = self.DATABASE["pool"]["name"],
					pool_size=self.DATABASE["pool"]["size"],
					pool_reset_session=self.DATABASE["pool"]["reset_session"],
					use_pure=self.DATABASE["pool"]["use_pure"],
					**config)
			self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}: Connection pool successfully created!')
			return cnx_pool
		except connector.Error as err:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: Problem creating connection pool: {err}')
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: Check DB cnfg:\n{json.dumps(self.DATABASE)}')
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}:Problem creating connection pool: {e}')
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}:Check DB conf:\n{json.dumps(self.DATABASE)}')
