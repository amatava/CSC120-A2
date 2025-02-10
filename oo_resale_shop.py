from computer import Computer

class ResaleShop:

    # What attributes will it need?
    
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []
        self.new_id = 0
        
         # You'll remove this when you fill out your constructor

    # What methods will you need?
    def buy(self, computer):
        #create a new computer instances with Computer(...)
        computer_id = self.new_id
        #2. call inventory.append(...) to add the
        #new Computer instance to the inventory
        self.inventory.append({"id": computer_id, "computer": computer})                                                       
        #give the next computer added its own iD
        self.new_id += 1
        return computer_id
    
    def sell(self, computer_id):
        if self.inventory[computer_id] is not None:
            del self.inventory[computer_id]
            print("Item", computer_id, "sold.")
        else:
            print("Item", computer_id, "not found. Cannot update price.")

    def refurbish(self, computer, computer_id, new_os):
        if self.inventory[computer_id] is not None:
            computer = self.inventory[computer_id]["computer"] # locate the computer
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
            print("Item", computer_id, "not found. Please select another item to refurbish.")

    def print_inventory(self):
    # If the inventory is not empty
        if self.inventory:
            # For each item
            for item in self.inventory:
                computer = item["computer"]
                # Print its details
                print(f'Item ID: {self.inventory.index(item)} : {item}')
        else:
            print("No inventory to display.")
