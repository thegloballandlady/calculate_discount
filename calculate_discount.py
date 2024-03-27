# Define the calculate_discount function
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else:
        return price

# Main program
def main():
    # Get user input for original price and discount percentage
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price using the calculate_discount function
    final_price = calculate_discount(original_price, discount_percent)

    # Print the final price after applying the discount
    if final_price != original_price:
        print(f"Final price after applying {discount_percent}% discount: ${final_price:.2f}")
    else:
        print("No discount applied. Original price remains the same.")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
