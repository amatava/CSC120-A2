# Import a few useful containers from the typing module
from oo_resale_shop import ResaleShop
from computer import Computer


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
    computer_description = resaleshop.buy(computer)
    print("Adding to inventory...")
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    resaleshop.print_inventory()
    print("Done.\n")

    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item:", {computer_description}, ", updating OS to", {new_OS})
    print("Updating inventory...")
    resaleshop.refurbish(computer, computer_description, new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    resaleshop.print_inventory()
    print("Done.\n")
    
    # Now, let's sell it!
    print("Selling Item:", {computer_description})
    resaleshop.sell(computer_description)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    resaleshop.print_inventory()
    print("Done.\n")

# Calls the main() function when this file is run
if __name__ == "__main__": 
    main()
