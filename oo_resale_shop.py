from computer import Computer

class ResaleShop:

    def __init__(self):
        '''Initializes an inventoryh list to store the computers in'''

        self.inventory = []
        
    def buy(self, computer):
        '''Adds newly bought computer to the inventory list'''

        self.inventory.append(computer.description)                                               
        return computer.description
    
    def sell(self, computer_description):
        '''Removes sold computer from the inventory'''
        if computer_description in self.inventory:
            self.inventory.remove(computer_description)
            print("Item", computer_description, "sold.")
        else:
            print("Item", computer_description, "not found. Cannot update price.")

    def refurbish(self, computer, computer_description, new_os):
        '''Removes old computer from inventory and adds refurbished one with new price back to the inventory'''
        if computer_description in self.inventory:
            self.inventory.remove(computer_description) 
            self.inventory.append(f"{computer_description}, updated to {new_os}")
            if int(computer.year_made) < 2000:
                computer.price = 0 # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff

            if new_os is not None:
                computer.operating_system = new_os # update details after installing new OS
        else:
            print("Item", computer_description, "not found. Please select another item to refurbish.")

    def print_inventory(self):
        '''Prints every item in inventory'''
    # If the inventory is not empty
        if self.inventory:
            # For each item
            for item in self.inventory:
                # Print its details
                print(item)
        else:
            print("No inventory to display.")
