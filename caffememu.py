#Define the memu of caffee
memu ={
    'Pizza':15,
    'pasta':15,
    'Burger':5,
    'coffee':6,
    'ice-tea':7,
    }
print("Welcome to PYTHON CAFEE ")
print("Pizza: $12\npasta: $15\nBurger: $5\ncoffee: $6\nice-tea: $7")

total_order =0

item_1 = input("Enter the name of the item you want to order....")

if item_1 in memu:
    total_order += memu[item_1]
    print(f"your item {item_1} is added")
else:
    print(f"{item_1} is not avaiable")

another_item = input("would you like to order any other item ?")
if another_item == "Yes":
    item_2 = input("enter the second item ")
    if item_2 in memu:
        total_order += memu[item_2]
        print(f"Item {item_2} is add to the order")
    else:
        print(f"Item {item_2} is not available")
print (f" Total amount :{total_order}")
