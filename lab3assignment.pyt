# Author: Elvis Tamrakar, Student Id: 23056848
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source. 
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.

def menu():
    print("WELCOME TO THE AMANDO SHOPPING SITE")
    print("1. Add a product to the cart.") 
    print("2. Search for a product.") 
    print("3. Delete a product from the cart.")
    print("4. Display the contents of the cart.")
    print("5. Purchase items.")
    print("6. Quit.")
    userinput= int(input("Please select an option: "))
    return userinput

userinput = menu()
tries = 0
shoppingCart={}
newcart = 0
total = 0

while userinput!=6 and userinput<6 and userinput>0:
    
    
    if userinput==1:
        if (len(shoppingCart)<5):
            productname = str(input("Enter the product-name: "))
            productprice = float(input("Enter the product price: "))
            brandname = str(input("Enter the brand name: "))
            shoppingCart.update({productname:{ "product-price":productprice,"brand":brandname } })
            print (shoppingCart)
            userinput = menu()
        else:
            print("Cart is full")
            userinput = menu()
    elif userinput==2:
        search = str(input("Enter the product you want to search: "))
        if search in shoppingCart.keys():
            print (shoppingCart.get(search))
            userinput = menu()
        else:
            print ("No product exists with the name")
            userinput = menu()
    elif userinput==3:
        delete = str(input("Enter the product you would like to delete: "))
        if shoppingCart == {}:
            print("The cart is empty, no item is found")
            userinput =menu()
        elif delete in shoppingCart.keys():
                shoppingCart.pop(delete)
                userinput =menu()
        else:
            print ("Product not found in cart")
            userinput =menu()
    elif userinput==4:
        if shoppingCart != {}: 
            for key, value in shoppingCart.items():
                print (key, value, sep=":")
            userinput =menu()
        else:
            print("Cart is empty")
            userinput =menu()
    elif userinput==5:
        
        if shoppingCart != {}:
            for key,val in shoppingCart.items():
                total = total + val["product-price"]
            
            print ("The total price is: ", total)
                
            decision = (input("Complete purchase (Y/N)? "))
                
            if decision == "Y" or decision == "y":
                    print ("Thank you for your business.")
                    shoppingCart.clear()
                    
                    userinput = menu()
            elif decision == "N" or decision == "n":
                    "Please continue shopping "
                    userinput = menu()
            else:
                    print ("Please answer either Y or N")
                    continue
                    
            userinput = menu()
                
                
        else:
            print ("Cart is empty, please select an item before completing purchase.") 
            userinput = menu()
else:
    print("Try again")
    userinput =menu()

