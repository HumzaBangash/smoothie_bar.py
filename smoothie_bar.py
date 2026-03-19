"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[✓] 1. Header Docstring included.
[✓] 2. Global Constants BASES and FRUITS defined as Tuples.
[✓] 3. Professional function get_price(size) returns a float.
[✓] 4. Professional function blend(size, base, fruit, scoops) for output.
[✓] 5. main() function handles try/except for scoops (int).
[✓] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTS (The Pantry)
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")


def get_price(size):
    """Returns the price of the smoothie based on size."""
    size = size.lower()
    
    if size == "small":
        return 3.00
    elif size == "medium":
        return 4.00
    elif size == "large":
        return 5.00
    else:
        return 0.0  # fallback if invalid input


def blend(size, base, fruit, scoops):
    """Prints the smoothie order summary."""
    price = get_price(size)
    
    print("\n--- Smoothie Order ---")
    print(f"Size: {size.capitalize()}")
    print(f"Base: {base}")
    print(f"Fruit: {fruit}")
    print(f"Scoops: {scoops}")
    print(f"Total Price: ${price:.2f}")
    print("----------------------\n")


def main():
    """Main function to run the smoothie bar system."""
    # Humza Bangash smoothie_bar.py project
    print("🍓 Welcome to the Smoothie Bar! 🍌")
    
    # Size input
    size = input("Choose a size (Small, Medium, Large): ").lower()
    
    # Display bases and get input
    print("\nAvailable Bases:")
    for b in BASES:
        print("-", b)
    base = input("Choose a base: ")
    
    # Display fruits and get input
    print("\nAvailable Fruits:")
    for f in FRUITS:
        print("-", f)
    fruit = input("Choose a fruit: ")
    
    # Scoops input with try/except
    try:
        scoops = int(input("How many scoops of fruit?: "))
    except ValueError:
        print("Invalid input! Defaulting scoops to 1.")
        scoops = 1
    
    # Call blend function
    blend(size, base, fruit, scoops)


# Run the program
if __name__ == "__main__":
    main()
