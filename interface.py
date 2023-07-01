import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from main import calculate_total_price

def place_order():
    pizza_type = pizza_type_combobox.get()
    quantity = int(quantity_combobox.get())

    total_price = calculate_total_price(pizza_type, quantity)

    if total_price is not None:
        formatted_price = "{:.2f}".format(total_price)  # Format the total price with 2 digits after the decimal point
        total_price_label.config(text=f"Total Price: ${formatted_price}", bg="yellow", fg="red")

root = tk.Tk()
root.title("Pizza Order")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the window position
window_width = 400
window_height = 300
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Set the window size and position
root.geometry(f"{window_width}x{window_height}+{x}+{y}")


root.columnconfigure(0, weight=1)  # Make the first column expand to fit the screen
root.columnconfigure(1, weight=1)  # Make the second column expand to fit the screen

pizza_type_label = tk.Label(root, text="Pizza Type:", font=("Arial", 12, "bold"), fg="blue", bg="yellow")
pizza_type_label.grid(row=0, column=0, padx=10, pady=10, sticky="news")

pizza_types = ["Regular", "Supreme", "Deluxe"]
pizza_type_combobox = ttk.Combobox(root, values=pizza_types, state="readonly")
pizza_type_combobox.grid(row=0, column=1, padx=10, pady=10, sticky="news")
pizza_type_combobox.current(0)

quantity_label = tk.Label(root, text="Quantity:", font=("Arial", 12, "bold"), fg="blue", bg="yellow")
quantity_label.grid(row=1, column=0, padx=10, pady=10, sticky="news")

quantities = list(range(1, 21))
quantity_combobox = ttk.Combobox(root, values=quantities, state="readonly")
quantity_combobox.grid(row=1, column=1, padx=10, pady=10, sticky="news")
quantity_combobox.current(0)

order_button = tk.Button(root, text="Place Order", command=place_order)
order_button.config(
    width=15,
    height=3,
    bg="yellow",
    fg="blue",
    font=("Arial", 23, "bold"),
    relief=tk.RAISED,
    bd=3
)
order_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="news")

total_price_label = tk.Label(root, text="Total Price: $0.00", font=("Arial", 30, "bold"))
total_price_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="news")

root.mainloop()