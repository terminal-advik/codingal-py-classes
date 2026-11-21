

print("=*= Grocery Billing Queue =*=\n")


low_price_items = 0
medium_price_items = 0
high_price_items = 0
customers_served = 0
total_sales = 0
billing = True 

while billing: 
    name = input("Enter Customer Name: ")
    item_count = int(input(f"Hello {name}!!!!!!!. How many items are you buying today? "))
    if item_count <= 0:
        print("INVAILD item count. PLEASE enter a POSSITIVE NUMBER.\n")
        continue

    customer_total = 0
    item_number = 1
    while item_number <= item_count:
        item_name = (input("Please enter the item's name!!😎: "))
        price = float(input("Now enter the price of that item: "))
        quantity = int(input("Also enter the quantity of that item: "))

        if price <= 0 or quantity <= 0:
            print("INVAILD PRICE OR QUANTITY. PLEASE ENTER AGAIN. \n")
            continue
        item_total = price * quantity
        print(f" {item_name}: {quantity} x {price} = {item_total} ")
        customer_total += item_total

        if price < 50:
            low_price_items += quantity
        elif price <= 100:
            medium_price_items
        else:
            high_price_items += quantity

        item_number += 1

    customers_served += 1
    total_sales += customer_total
    print(f"\nTotal bill for{name}: {customer_total}")
    print("Billing complete🥳🥳🥳!!!\n")
    again = input("Next customer? (yes/no): ")
    if again != "yes":
        billing = False

print("\n=*= 👌GROCERY CATEGORY REPORT👌 =*=")
for slot in range(1, 4):
    if slot == 1:
        label, total = "Low price item", low_price_items
    elif slot == 2:
        label, total = "Medium price item", medium_price_items
    else:
        label, total = "High price item", high_price_items
    if total > 0:
        print(f" {label}: {total} ", end="")
        for item in range(total):
            print("*", end="")
        print()

# print customers_served and total_sales
print("Customers served: ", customers_served)
print("Total sales: ", total_sales)
print("🥳🤯 GROCERY BILLING CLOSED. GOODBYE!!!!!!!!")