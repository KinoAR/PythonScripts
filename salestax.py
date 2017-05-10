#!/usr/bin/env python3
""" This is a script to calculate the sales tax in connecticut on any purchase. """
INPUTSTRING = input("Enter Total Price: ")

def calculate_sales_tax(price):
    "Calculates the sales tax upon recieving a price parameter."

    sales_tax = 0.0635
    print("The price with sales tax is:" + "{0:.2f}".format(float(price) * (1 + sales_tax)))
    print("Sales Tax: " + "{0:.2f}".format(float(price) * sales_tax))

calculate_sales_tax(float(INPUTSTRING))
