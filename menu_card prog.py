menu = {"burger": 149.0,
        "popcorn": 109.0,
        "fries": 99.0,
        "pizza": 179.0,
        "chips": 59.0,
        "soda": 49.0,
        "juice": 69.0}

cart = []
total = 0

print("~~~~~~ MENU ~~~~~~")
for key,value in menu.items():
    print(f"{key:10}: ₹{value:.2f}")
print("~~~~~~~~~~~~~~~~~~")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print(cart)

for i in cart:
    total += menu.get(food)
    print(food)