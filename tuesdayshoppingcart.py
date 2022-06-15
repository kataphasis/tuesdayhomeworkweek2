itemlist= {"red apple": 1, "green apple": 2, "banana": 3, "avocado": 4, "cabbage": 5}
cart = {}
def browse():
    print("Select an item:")
    print("Red apple: e")
    print("Green apple: f")
    print("Banana: g")
    print("Avocado: h")
    print("Cabbage: i")
    print("Go back to main menu: j")
    itemchoice = input("Pick an item or choose to go back to main menu: ")
    itemquantity = input("How many do you want? ")
    #I do not understand why me putting j doesn't break the loop and go back to the main menu, i've tried everything i can think of, it says too many values being pulled at once, it says this or that thing isn't an integer, it's saying j is getting put through the while loop in various ways even though I've not writtten anything that should make j go through the while loop, i've only written j to go to main menu, i'm going to bed lol
    
    while itemchoice != "j":
        itemchoice = input("select again: ")    
        if itemchoice == "e":
            
            itemquantity = input("select quantity for new item: ")
            itemtotal = int(itemlist['red apple']) * itemquantity
            cart["Red apple"] = int(itemtotal)
        elif itemchoice == "f":
            
            itemquantity = input("select quantity for new item: ")
            itemtotal = int(itemlist['green apple']) * itemquantity
            cart["Green apple"] = int(itemtotal)
        elif itemchoice == "g":
            
            itemquantity = input("select quantity for new item: ")
            itemtotal = int(itemlist['banana']) * itemquantity            
            cart["banana"] = int(itemtotal)
        elif itemchoice == "h":
            
            itemquantity = input("select quantity for new item: ")
            itemtotal = int(itemlist['avocado']) * itemquantity
            cart["Avocado"] = int(itemtotal)
        elif itemchoice == "i":
            
            itemquantity = input("select quantity for new item: ")
            itemtotal = int(itemlist['cabbage']) * itemquantity
            cart["Cabbage"] = int(itemtotal)
    if itemchoice == "j":
        mainmenu()
def viewcart():
    for k, v in cart.items():
        print(k, + " $", v)
        print("Total: $", + sum(v))
    print("Would you like to go back to the main menu? y/n")
    viewcartchoice = input("Select: ")
    if viewcartchoice == "y":
        mainmenu()
    if viewcartchoice == "n":
        editcart()
def editcart():
    print("Which items would you like to take away?")
    for k, v in cart:
        print(k, " $", v)
    delete_items = input("Please type out the item you wish to delete (case sensitive) or type m to go back to mainmenu: ")
    if delete_items == "Red apples":
        cart.pop("red apples")
    elif delete_items == "Green apples":
        cart.pop("green apples")
    elif delete_items == "Banana":
        cart.pop("banana")
    elif delete_items == "Avocado":
        cart.pop("avocado")
    elif delete_items == "Cabbage":
        cart.pop("cabbage")
    elif delete_items == "m":
        mainmenu()

    

def mainmenu():
    print("Welcome to Patrick's shopping cart!")
    print("Please select an option below")
    print("Browse and add items: a")
    print("View cart: b")
    print("Change items in cart: c")
    print("Quit Program: d")
    choice = input("Select option: ")
    if choice == "a":
        browse()
    elif choice == "b":
        viewcart()
    elif choice == "c":
        editcart()
    elif choice == "d":
        for k, v in cart:
            print(k, + " $", + v)
            print(sum(v))
            break
mainmenu()