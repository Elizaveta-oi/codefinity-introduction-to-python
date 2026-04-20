grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50),
}
print(grocery_inventory)

eggs_price = grocery_inventory["Eggs"][1]
if eggs_price > 5:
    grocery_inventory["Eggs"] = (
        grocery_inventory["Eggs"][0],      
        eggs_price - 1,                     
        grocery_inventory["Eggs"][2]         
    )
    print("Eggs are too expensive, reducing the price by $1.")
else:
    print("The price of Eggs is reasonable.")

grocery_inventory.update({"Tomatoes" : ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes:", grocery_inventory)


milk_category, milk_price, milk_stock = grocery_inventory["Milk"]
if milk_stock < 10:
    milk_stock += 20
    grocery_inventory["Milk"] = (milk_category, milk_price, milk_stock)
    print("Milk needs to be restocked. Increasing stock by 20 units.")
else:
    print("Milk has sufficient stock.")


apples_price = grocery_inventory["Apples"][1]
if apples_price > 2:
    grocery_inventory.pop("Apples", None)
    print("Apples removed from inventory due to high price.")

print("Updated inventory:", grocery_inventory)
