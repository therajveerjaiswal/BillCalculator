print(">>> Bill Calculation Software written in Python\n>>> [Author:Rajveer]")
import numpy as np

def get_customer_details():
    print("****************************")
    name = input(">>> Enter Customer's Name: ").strip()
    mob = input(">>> Enter Customer's Mobile: ").strip()
    return name, mob

def get_order_details():
    print("****************************")
    orders = []
    num_orders = int(input(">>> Enter number of orders: "))
    for _ in range(num_orders):
        order_name = input(">>> Enter order name: ").strip()
        order_price = float(input(">>> Enter cost of order: "))
        order_quantity = int(input(">>> Enter quantity of order: "))
        orders.append((order_name, order_price, order_quantity))
    return orders

def calculate_total(orders):
    return [price * quantity for _, price, quantity in orders]

def print_receipt(customer_details, orders, totals):
    print("****************************")
    print("[*].....wait while receipt is being generated")
    print("********************************************")
    print(f">> Customer Name: {customer_details[0]}")
    print(f">> Customer Mobile: {customer_details[1]}")
    print("********************************************")
    print(">> Order Details:")
    print("{:<20} {:<10} {:<10} {:<10}".format("Order Name", "Price", "Quantity", "Total"))
    print("----------------------------------------------------------")
    for order, total in zip(orders, totals):
        name, price, quantity = order
        print(f"{name:<20} {price:<10} {quantity:<10} {total:<10}")
    print("----------------------------------------------------------")
    print(f">> Sub Total = Rs {sum(totals):.2f}")
    print("********************************************")

def main():
    customer_details = get_customer_details()
    orders = get_order_details()
    totals = calculate_total(orders)
    print_receipt(customer_details, orders, totals)

if __name__ == "__main__":
    main()
