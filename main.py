# Import a few useful containers from the typing module
from oo_resale_shop import ResaleShop
from computer import Computer

# def create_computer(description: str,
#                     processor_type: str,
#                     hard_drive_capacity: int,
#                     memory: int,
#                     operating_system: str,
#                     year_made: int,
#                     price: int):
#     return {'description': description,
#             'processor_type': processor_type,
#             'hard_drive_capacity': hard_drive_capacity,
#             'memory': memory,
#             'operating_system': operating_system,
#             'year_made': year_made,
#             'price': price
#     }

def main():
    
    resaleshop = ResaleShop() #creates instance
    # First, let's make a computer
    computer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Add it to the resale store's inventory
    print("Buying", computer.description)
    computer_id = resaleshop.buy(computer)
    print("Adding to inventory...")
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    resaleshop.print_inventory()
    print("Done.\n")

    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", {computer_id}, ", updating OS to", {new_OS})
    print("Updating inventory...")
    resaleshop.refurbish(computer, computer_id, new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    resaleshop.print_inventory()
    print("Done.\n")
    
    # Now, let's sell it!
    print("Selling Item ID:", {computer_id})
    resaleshop.sell(computer_id)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    resaleshop.print_inventory()
    print("Done.\n")

# Calls the main() function when this file is run
if __name__ == "__main__": 
    main()
