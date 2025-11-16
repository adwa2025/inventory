from inventory.service_layer.app_services import AppServices
from inventory.application_base import ApplicationBase
import sys

class ConsoleUI(ApplicationBase):
    """ Define the ConsoleUI class. """

    def __init__(self, config:dict)->None:
        """ Initializes object. """
        self._config_dict = config
        self.META = config["meta"]
        super().__init__(subclass_name=self.__class__.__name__, 
                logfile_prefix_name=self.META["log_prefix"])
        self.app_services = AppServices(config)

    # Public Methods
    def display_menu(self)->None:
        """ Display the menu. """
        print(f"\n\n\tInventory Management System")
        print()
        print(f"\t1. List all suppliers")
        print(f"\t2. List all parts")
        print(f"\t3. Add Supplier")
        print(f"\t4. Add Part")
        print(f"\t5. Record Supplier Part")
        print(f"\t6. Exit")
        print()

    def process_menu_choice(self)->None:
        """ Process users menu choice. """
        choice = input("\tEnter your choice (1-6): ")

        match choice:
            case '1': self.list_suppliers()
            case '2': self.list_parts()
            case '3': self.add_supplier()
            case '4': self.add_part()
            case '5': self.record_supplier_part()
            case '6': sys.exit(0)
            case _: print("\tInvalid Menu choice {choice}. Please try again.")

    def list_suppliers(self)->None:
        """ Listing all suppliers. """
        print("\tListing all suppliers...")

    def list_parts(self)->None:
        """ Listing all parts. """
        print("\tListing all parts...")

    def add_supplier(self)->None:
        """ Add a new supplier. """
        print("\tAdding a new supplier...")

    def add_part(self)->None:
        """ Add a new part. """
        print("\tAdding a new part...")

    def record_supplier_part(self)->None:
        """ Record a supplier part. """

    def start(self)->None:
        while True:
            self.display_menu()
            self.process_menu_choice()