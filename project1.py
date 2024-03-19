def calculate_cost(cost_price):
    """
    Calculates the selling price of a cosmetic product by adding a 10% markup to the cost price.

    Args:
        cost_price (float): The cost price of the cosmetic product.

    Returns:
        float: The selling price of the cosmetic product.
    """
    markup = 0.10  # 10% markup
    selling_price = cost_price * (1 + markup)
    return selling_price

# Example usage
cost_price = float(input("Enter the cost price of the cosmetic product: "))
selling_price = calculate_cost(cost_price)
print(f"The selling price of the cosmetic product is: ${selling_price:.2f}")







