import tkinter as tk

# Create the window
window = tk.Tk()

# Create the menu
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)

# Create the labels
title_label = tk.Label(text="Order System")
item_label = tk.Label(text="Item")
quantity_label = tk.Label(text="Quantity")
price_label = tk.Label(text="Price")
total_label = tk.Label(text="Total")

# Create the entry boxes
item_entry = tk.Entry()
quantity_entry = tk.Entry()

# Create the buttons
add_button = tk.Button(text="Add to Order", command=add_order)
clear_button = tk.Button(text="Clear Order", command=clear_order)
submit_button = tk.Button(text="Submit Order", command=submit_order)

# Place the labels and entry boxes on the window
title_label.pack(side="top", fill="x", pady=10)
item_label.pack(side="left", padx=10)
item_entry.pack(side="left", padx=10)
quantity_label.pack(side="left", padx=10)
quantity_entry.pack(side="left", padx=10)
price_label.pack(side="left", padx=10)
total_label.pack(side="left", padx=10)
add_button.pack(side="left", padx=10)
clear_button.pack(side="left", padx=10)
submit_button.pack(side="left", padx=10)

# Create a dictionary of items and prices
items = {
    "Pizza": 10,
    "Burger": 5,
    "Fries": 2,
    "Soda": 1
}

# Define a function to add an item to the order
def add_order():
    # Get the item and quantity from the entry boxes
    item = item_entry.get()
    quantity = int(quantity_entry.get())

    # Add the item to the order
    order.append((item, quantity))

    # Update the total
    total += items[item] * quantity * 1.0

    # Update the labels
    item_label.config(text="Item")
    quantity_label.config(text="Quantity")
    price_label.config(text="Price")
    total_label.config(text="Total: ${}".format(total))

# Define a function to clear the order
def clear_order():
    # Clear the order list
    order.clear()

    # Reset the total
    total = 0

    # Update the labels
    item_label.config(text="Item")
    quantity_label.config(text="Quantity")
    price_label.config(text="Price")
    total_label.config(text="Total: $0")

# Define a function to submit the order
def submit_order():
    # Print the order to the console
    print("Order:")
    for item, quantity in order:
        print("{} x {}".format(item, quantity))

    print("Total: ${}".format(total))

# Start the main loop
window.mainloop()