import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import gspread
from oauth2client.service_account import ServiceAccountCredentials
load_dotenv()


#Sendgrid API
#Status code 202 means the email was successfully sent
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")
SENDGRID_TEMPLATE_ID = os.getenv("SENDGRID_TEMPLATE_ID", default="OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")
client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
print("CLIENT:", type(client))
subject = "Your Receipt from Madeline's Grocery Shoppe"
html_content = "Thank you for visiting today. Please see your itemized receipt below."
print("HTML:", html_content)
#to_emails value is customizable to any email address
message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS, subject=subject, html_content=html_content)
try:
    response = client.send(message)
    print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
    print(response.status_code) 
    print(response.body)
    print(response.headers)
except Exception as err:
    print(type(err))
    print(err)



#Google API Authorization 
DOCUMENT_ID = "1ItN7Cc2Yn4K90cMIsxi2P045Gzw0y2JHB_EkV4mXXpI"
SHEET_NAME = "products"
TAX_RATE = os.getenv("TAX_RATE")
CREDENTIALS_FILEPATH = './google-credentials.json'
AUTH_SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets", #> Allows read/write access to the user's sheets and their properties.
    "https://www.googleapis.com/auth/drive.file" #> Per-file access to files created or opened by the app.
]
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)
print("CREDS:", type(credentials)) #> <class 'oauth2client.service_account.ServiceAccountCredentials'>
client = gspread.authorize(credentials)
#print("CLIENT:", type(client))
#Read sheet values
print("-----------------")
print("READING DOCUMENT...")
doc = client.open_by_key(DOCUMENT_ID)
#print("DOC:", type(doc), doc.title) #> <class 'gspread.models.Spreadsheet'>
sheet = doc.worksheet(SHEET_NAME)
#print("SHEET:", type(sheet), sheet.title)#> <class 'gspread.models.Worksheet'>
rows = sheet.get_all_records()
#print("ROWS:", type(rows)) #> <class 'list'>
for row in rows:
    print(row)
print("-----------------")
print("NEW ROW...")
auto_incremented_id = len(rows) + 898248001108
new_row = {
    "id": auto_incremented_id,
    "name": "Product {auto_incremented_id} (created from my python app)",
    "department": "snacks",
    "price": 4.99,
    "availability_date": "2021-02-17"
}
print(new_row)
#print("________________________")
#print("WRITING VALUES TO DOCUMENT...")
new_values = list(new_row.values())
next_row_number = len(rows) + 2
response = sheet.insert_row(new_values, next_row_number)
#print("RESPONSE:", type(response))
#print(response)



#Beginning of Shopping Cart User Input
from datetime import datetime
now = datetime.now()
#Store the results of the input process in the selected ID variable
print("________________________")
print("Madeline's Grocery Shoppe")
print("________________________")
print("Website: madelinegrocery.com")
print("Phone: 212.000.0000")

total_price = 0
selected_ids = []
def to_usd(total_price):
    return "${total_price:,.2f}".format(total_price)


#Nest inside a new loop with selected IDs 
selected_products = []
while True:
    selected_id = input("Please enter a product ID: ") #Product ID is a string
    if selected_id.upper() == "DONE":
        break
    else:
        matching_products = [p for p in rows if str(p["id"]) == str(selected_id)]
        if any(matching_products):
            selected_ids.append(matching_products[0])
            print(matching_products, "name", "price")
        else:
            print("Invalid entry, please try again.")

checkout_time = datetime.now()
def to_usd(price):
    return f"$(price:,.2f)"

subtotal = sum([float(p["price"]) for p in selected_products])     

#Look up the corresponding product from the list using list comprehension - filter items to a subset that match a certain condition
#Remember to convert numbers to strings what concatinating them 
#print = selected_ids
#Define this variable somewhere above the loop
#Separate fetching product names and prices in its own process


#print("SELECTED PRODUCT: " + matching_product["name"] + " " + str(matching_product["price"])
#print[float("TOTAL PRICE: " + str(total_price))]
print("Checkout Time: " + str(checkout_time.strftime("%Y-%M-%D %H:%m:%S")))
for p in selected_products:
    print("SELECTED PRODUCT: " + p["name"] + "   " + '${:.2f}'.format(p["price"]))

print(f"Subtotal: {subtotal:,.2f}")
print(f"Plus NYC Sales Tax (8.75%): {(subtotal * 0.0875):,.2f}")
print(f"Total: {((subtotal * 0.0875) + subtotal):,.2f}")
print("________________________")
print("Thanks for stopping by! See you soon.")

