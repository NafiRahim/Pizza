def calculate_discount(quantity):
    discount = 0.0

    if quantity >= 5:
        discount = 0.25  # 25% discount for ordering 5 or more pizzas
    elif quantity >= 2:
        discount = 0.10  # 10% discount for ordering 2 or more pizzas

    return discount

def calculate_total_price(pizza_type, quantity):
    regular_price = 10.00
    supreme_price = 12.00
    deluxe_price = 15.00

    if pizza_type == "Regular":
        pizza_price = regular_price
    elif pizza_type == "Supreme":
        pizza_price = supreme_price
    elif pizza_type == "Deluxe":
        pizza_price = deluxe_price
    else:
        print("Invalid pizza type.")
        return None

    discount = calculate_discount(quantity)
    pizza_price -= pizza_price * discount

    total_price = pizza_price * quantity
    return total_price

def place_pizza_order():
    print("Welcome to our pizza order app!")

    pizza_type = str(input("What type of pizza would you like? (Regular, Supreme, Deluxe): "))
    quantity = int(input("How many pizzas would you like?: "))

    total_price = calculate_total_price(pizza_type, quantity)

    if total_price is not None:
        print(f"\nYour order summary:")
        print(f"Pizza Type: {pizza_type}")
        print(f"Quantity: {quantity}")
        print(f"Total Price: ${total_price}")




# Call the function to place a pizza order
place_pizza_order()
