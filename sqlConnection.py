# Group: CrtAltElite
# Skye Jones: 4122217
# Uwais Cornelius: 4121659
# Jean-Jacques Van Schalkwyk: 4204301
# Kaamiel Isaacs: 4129581
# Thaakirah Mosoval: 4314422
# File name: sqlConnection.py
# Final DB CSC312 Assignment
# Due: 12 October
import mysql.connector

# function for query to list all users
def listUsers(cursor):
    cursor.execute("SELECT user_id, username, email FROM User;")
    rows = cursor.fetchall()
    if not rows:
        print("\nNo users found\n")
    else:
        print("\nUsers:")
        for row in rows:
            print(f"User ID: {row[0]}, Username: {row[1]}, e-mail address: {row[2]}")
        print("\n")  

# function for query to list all items and their values
def listItems(cursor):
    cursor.execute("SELECT item_id, name, current_value FROM Item;")
    rows = cursor.fetchall()
    if not rows:
        print("\nNo items found\n")
    else:
        print("\nItems:")
        for row in rows:
            print(f"Item ID: {row[0]}, Item name: {row[1]}, Item value: {row[2]}")
        print("\n")

# function for query to list items in office inventory
def listItemsInOffice(cursor):
    cursor.execute("SELECT Inventory.name AS Inventory, Item.name AS Item FROM Item JOIN Inventory ON Item.inventory_id = Inventory.inventory_id WHERE Inventory.name = 'Office Inventory';")
    rows = cursor.fetchall()
    if not rows:
        print("\nNo items found for office\n")
    else:
        print("\nItems in office:")
        for row in rows:
            print(f"Inventory: {row[0]}, Item name: {row[1]}")
        print("\n")  

# function for query to count items owned by users
def countItemsOfUsers(cursor):
    cursor.execute("SELECT User.username, COUNT(Item.item_id) AS total_items FROM User JOIN Inventory ON User.user_id = Inventory.user_id JOIN Item ON Inventory.inventory_id = Item.inventory_id GROUP BY User.username;")
    rows = cursor.fetchall()
    if not rows:
        print("\nNo items found for users\n")
    else:
        print("\nAmount of items per user:")
        for row in rows:
            print(f"Username: {row[0]}, Total items: {row[1]}")
        print("\n")  

# function for query to list items from most to least valuable
def orderValue(cursor):
    cursor.execute("SELECT name, current_value FROM Item ORDER BY current_value DESC;")
    rows = cursor.fetchall()
    if not rows:
        print("\nNo items found\n")
    else:
        print("\nItems from most to least valuable:")
        for row in rows:
            print(f"Item name: {row[0]}, Item value: {row[1]}")
        print("\n") 

# function for query to list items and their respective categories
def listItemCategories(cursor):
    cursor.execute("SELECT Item.name AS Item, Category.name AS Category FROM Item JOIN Item_Category ON Item.item_id = Item_Category.item_id JOIN Category ON Item_Category.category_id = Category.category_id;")
    rows = cursor.fetchall()
    if not rows:
        print("\nNo items found\n")
    else:
        print("\nItems and their categories:")
        for row in rows:
            print(f"Item name: {row[0]}, Category: {row[1]}")
        print("\n") 

# function for query to show users inventory value
def totalValues(cursor):
    cursor.execute("SELECT User.username, SUM(Item.current_value) AS total_value FROM User JOIN Inventory ON User.user_id = Inventory.user_id JOIN Item ON Inventory.inventory_id = Item.inventory_id GROUP BY User.username;")
    rows = cursor.fetchall()
    if not rows:
        print("\nNo values found\n")
    else:
        print("\nUsers' inventory values:")
        for row in rows:
            print(f"Username: {row[0]}, Inventory value: {row[1]}")
        print("\n") 

# function for query to show items with no tags
def listTaglessItems(cursor):
    cursor.execute("SELECT Item.name FROM Item LEFT JOIN Item_Tag ON Item.item_id = Item_Tag.item_id WHERE Item_Tag.tag_id IS NULL;")
    rows = cursor.fetchall()
    if not rows:
        print("\nNo tagless items found\n")
    else:
        print("\nItems with no tag:")
        for row in rows:
            print(f"Item name: {row[0]}")
        print("\n") 

# function for query to list item images
def listItemImages(cursor):
    cursor.execute("SELECT User.username, Inventory.name AS Inventory, Item.name AS Item, Image.file_name FROM Image JOIN Item ON Image.item_id = Item.item_id JOIN Inventory ON Item.inventory_id = Inventory.inventory_id JOIN User ON Inventory.user_id = User.user_id;")
    rows = cursor.fetchall()
    if not rows:
        print("\nNo images found\n")
    else:
        print("\nImages of items:")
        for row in rows:
            print(f"Username: {row[0]}, Inventory: {row[1]}, Item name: {row[2]}, Image: {row[3]}")
        print("\n") 

# function for query to summarize inventory information
def summariseInventories(cursor):
    cursor.execute("SELECT Inventory.name, (SELECT COUNT(*) FROM Item WHERE Item.inventory_id = Inventory.inventory_id) AS total_items, (SELECT SUM(current_value) FROM Item WHERE Item.inventory_id = Inventory.inventory_id) AS total_value FROM Inventory;")
    rows = cursor.fetchall()
    if not rows:
        print("\nNo inventories found\n")
    else:
        print("\nSummary of inventories:")
        for row in rows:
            print(f"Inventory: {row[0]}, Total items: {row[1]}, Total value: {row[2]}")
        print("\n") 

try:
    # establishing connection to database
    conn = mysql.connector.connect(
        host="localhost",
        user="marker",
        password="securepassword",
        database="inventory_system"
    )

    if conn.is_connected():
        print("Successfully connected to inventory_system database.")

    cursor = conn.cursor()

    # creating menu for user to choose quries and/or close the program
    while True:
        print("Query our database:")
        print("1.  List all users")
        print("2.  List all items")
        print("3.  List items in the office")
        print("4.  Count items for each user")
        print("5.  Order items by most to least valuable")
        print("6.  List items and their categories")
        print("7.  Show users' total inventory value")
        print("8.  List items with no tags")
        print("9.  List item images")
        print("10. Show summary of inventories")
        print("11. Exit program")
        
        choice = input("Enter your choice by entering only the number (e.g. to list all users just enter '1'): ")
        
        if choice == "1":
            listUsers(cursor)
        elif choice == "2":
            listItems(cursor)
        elif choice == "3":
            listItemsInOffice(cursor)
        elif choice == "4":
            countItemsOfUsers(cursor)
        elif choice == "5":
            orderValue(cursor)
        elif choice == "6":
            listItemCategories(cursor)
        elif choice == "7":
            totalValues(cursor)
        elif choice == "8":
            listTaglessItems(cursor)
        elif choice == "9":
            listItemImages(cursor)
        elif choice == "10":
            summariseInventories(cursor)
        elif choice == "11":
            print("Thanks for querying!")
            break
        else:
            print("Input not valid. Try again.")

except mysql.connector.Error as err:
    print(f"Connection failed: {err}")

finally:
    # cleanup
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
    print("inventory_system database connection closed")