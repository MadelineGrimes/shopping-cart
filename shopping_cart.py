import os
from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
load_dotenv
#Google API Authorization 
DOCUMENT_ID = "1ItN7Cc2Yn4K90cMIsxi2P045Gzw0y2JHB_EkV4mXXpI"
SHEET_NAME = "Shopping Cart Project - Datastore (PUBLIC)"
CREDENTIALS_FILEPATH = '/Users/madelinegrimes/Documents/GitHub/shopping-cart/google-credentials.json'
AUTH_SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets", #> Allows read/write access to the user's sheets and their properties.
    "https://www.googleapis.com/auth/drive.file" #> Per-file access to files created or opened by the app.
]
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)
print("CREDS:", type(credentials)) #> <class 'oauth2client.service_account.ServiceAccountCredentials'>
client = gspread.authorize(credentials)
print("CLIENT:", type(client))

#Read sheet values

print("-----------------")
print("READING DOCUMENT...")

doc = client.open_by_key(DOCUMENT_ID)
print("DOC:", type(doc), doc.title) #> <class 'gspread.models.Spreadsheet'>

sheet = doc.worksheet(SHEET_NAME)
print("SHEET:", type(sheet), sheet.title)#> <class 'gspread.models.Worksheet'>

rows = sheet.get_all_records()
print("ROWS:", type(rows)) #> <class 'list'>

for row in rows:
    print(row)

print("-----------------")
print("NEW ROW...")

auto_incremented_id = len(rows) + 898248001108
new_row = {
    "id": auto_incremented_id,
    "name": f"Product {auto_incremented_id} (created from my python app)",
    "department": "snacks",
    "price": 4.99,
    "availability_date": "2021-02-17"
}
print(new_row)

print("-----------------")
print("WRITING VALUES TO DOCUMENT...")
new_values = list(new_row.values())
next_row_number = len(rows) + 2
response = sheet.insert_row(new_values, next_row_number)
print("RESPONSE:", type(response))
print(response)


#Beginning of Shopping Cart User Input

#Store the results of the input process in the selected ID variable
total_price = 

while True:
    selected_id = input("Please enter a product ID: ") #Product ID is a string
    if selected_id == "DONE":
        break
    else:
#Look up the corresponding product from the list using list comprehension - filter items to a subset that match a certain condition
        matching_products = [p for p in SHEET_NAME if str(p["id"]) == str(selected_id)]
        matching_product = matching_products[0]
        total_price = total_price + (matching_product["price"]) 
        print("SELECTED PRODUCT: " + matching_product["name"] + " " + str(matching_product["price"])
#Remember to convert numbers to strings what concatinating them 

#Define this variable somewhere above the loop
total_price = 0 
print("TOTAL PRICE: " + str(total_price))
