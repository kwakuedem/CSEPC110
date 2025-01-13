#program to calculate the price of a meal.

# prompt for the price of a child and an adult meal
price_of_child_meal=float(input("\nWhat is the price of a child's meal? "))
price_of_adult_meal=float(input("What is the price of an adult's meal? "))

# prompt for the number of adults and children
number_of_children=int(input("How many children are there? "))
number_of_adult=int(input("How many adults are there? "))

#Process and store cost of meal for children and adults and store in their repective variables
cost_of_children_meal= number_of_children * price_of_child_meal
cost_of_adults_meal=number_of_adult * price_of_adult_meal

#process and store subtotal
subtotal=(cost_of_children_meal + cost_of_adults_meal)

#Display subtotal
print(f"\nSubtotal: ${subtotal:.2f}")

# Final Requirements

#prompt for sales tax rate 
tax_rate=float(input("\nWhat is the sales tax rate? "))

#compute sales tax
sales_tax=(tax_rate / 100)*subtotal

#compute total cost
total=subtotal+sales_tax

#Displaying sales tax and total cost respectively
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total cost : ${total:.2f}")

#prompt for amount given by the customer for payment
payment_amount=float(input("\nWhat is the payment amount? "))

#compute and store balance to be given to customer in a variable called change
change=payment_amount-total

#Display change
print(f"Change: ${change:.2f}\n")

# Additional Features: Friendly Summary
print("\n----- Receipt Summary -----")
print(f"Child Meal Price: ${price_of_child_meal:.2f}")
print(f"Adult Meal Price: ${price_of_adult_meal:.2f}")
print(f"Number of Children: {number_of_children}")
print(f"Number of Adults: {number_of_adult}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Sales Tax ({tax_rate}%): ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")
print(f"Payment: ${payment_amount:.2f}")
print(f"Change: ${change:.2f}")
print("---------------------------")