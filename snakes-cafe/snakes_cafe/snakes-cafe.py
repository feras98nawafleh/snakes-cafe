# Adding Items to the Menu

Appetizers = ["Wings","Cookies","Spring Rolls"]
Entrees = ["Salmon","Steak","Meat Tornado","A Literal Garden"]
Desserts = ["Ice Cream","Cake","Pie"]
Drinks = ["Coffee","Tea","Unicorn Tears"]


# Dictionary Created Named Menu

menu = {
  "Appetizers":Appetizers,
  "Entrees":Entrees,
  "Desserts":Desserts,
  "Drinks":Drinks
}
items = {   
  "wings":0,
  "cookies":0,
  "spring rolls":0,
  "salmon":0,
  "steak":0,
  "meat tornado":0,
  "a literal garden":0,
  "ice cream":0,
  "cake":0,
  "pie":0,
  "coffee":0,
  "tea":0,
  "unicorn tears":0,
}

# function welcome message and instructions
def snakes_cafe():
    print ("**************************************")
    print('**    Welcome to Snakes Cafe     **')    
    print('**    How can I help you? Please see the menu below.    **')      
    print('**') 
    print('**    To quit at any time, type "quit/q"  **')  
    print("**************************************")

def order():
    for i in menu:
        print(i + ':')
        for j in menu[i]:
            print(j)
        print("-------")
    
order()
print("****** End of Menu ******")
print("**  What would you like to order?   **")
print("**************************************")
    
order = input()
order = order.lower()
counter = 0
while order != "quit" or order != "q":
      if(order in items):
          # incremnet number of orders
        items[order] = items[order] + 1
        counter += 1 
        print (f"** {items[order]} order of {order} have been added to your meal **")
        print("")
        print(f"Number of orders: {counter}")
        order=input(" would you like to order more? If yes tell me please ").lower()
        if order=="quit":
          break
        else:
          continue
      #Here if the user ordered something doesn't exist 
      else:
          print("Sorry We don't have your order now ")
          order = input(" would you like to order more? If yes tell me please If no just quit ").lower()
          if order == "quit" or order == "q":
            break
          else:
            continue
    
                    
if __name__=="__main__":
    snakes_cafe()
