import os
from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv

#Beginning of Shopping Cart User Input

#Store the results of the input process in the selected ID variable
selected_id = input("Please enter a product ID: ") #Product ID is a string
print(selected_id)
print(type(selected_id))



#Accept and print individual user input values
#Use a while loop
i = 1
while i < 898248001107:
    print(i)
    if i == DONE:
        break
    i += 1


#Use if/else statement with a break keyword once DONE is entered





































#Google API Authorization 
DOCUMENT_ID = os.getenv("GOOGLE_SHEET_ID", default="OOPS")
SHEET_NAME = os.getenv("SHEET_NAME", default="Products-2021")

CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "shopping-cart", "google-credentials.json")

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

