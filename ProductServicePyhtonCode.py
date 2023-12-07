import sys
import requests
import json

# Check if the base URL is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python your_product_script.py <base_url>")
    sys.exit(1)

# Get the base URL from the command-line argument
base_url = sys.argv[1]

def get_headers():
    # Define your headers here
    headers = {
        'Authorization': """Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRlc3Q0QHRlc3QuY29tIiwiX2lkIjoiNjU2ZjQ2NTI0ZGEwMGQwMDE3NmQwZTRkIiwiaWF0IjoxNzAxNzkxMzE0LCJleHAiOjE3MDQzODMzMTR9.doBeXKaajbI72bkRpHx6pIXXno6wt87B-dI43hX3UP0""",        'Content-Type': 'application/json'
    }
    return headers

# Function to make a POST request
def post_request(endpoint, payload):
    url = f"{base_url}/{endpoint}"
    headers = get_headers()
    response = requests.post(url, headers=headers, data=payload)
    with open("output.txt", "a") as output_file:
        output_file.write(f"URL: {url}\n")
        output_file.write(f"Response: {response.text}\n\n")

# Function to make a GET request
def get_request(endpoint):
    url = f"{base_url}/{endpoint}"
    headers = get_headers()
    response = requests.get(url, headers=headers)
    with open("output.txt", "a") as output_file:
        output_file.write(f"URL: {url}\n")
        output_file.write(f"Response: {response.text}\n\n")

# Example usage for product:

# POST request to /product/create
payload_create_product = json.dumps({
    "name": "Olive Oil",
    "desc": "great Quality of Oil",
    "type": "oils",
    "banner": "http://codergogoi.com/youtube/images/oliveoil.jpg",
    "unit": 1,
    "price": 400,
    "available": True,
    "supplier": "Golden seed firming"
})
post_request("product/create", payload_create_product)

# POST request to /ids
payload_ids = json.dumps({
    "ids": [
        "611badc2eeef961f9d33f2e4",
        "611badc2eeef961f9d33f2e4"
    ]
})
post_request("ids", payload_ids)

# GET request to /category/fruits
get_request("category/fruits")

# GET request to /
get_request("")

# GET request to /<product_id>
get_request("611e0109b81af50c9ea7a478")

# PUT request to /wishlist
payload_wishlist = json.dumps({
    "_id": "612cbc9ff201aa8b286fcd13"
})
post_request("wishlist", payload_wishlist)

# PUT request to /cart
payload_cart = json.dumps({
    "_id": "612cbc9ff201aa8b286fcd13",
    "qty": 3
})
post_request("cart", payload_cart)

# DELETE request to /cart/<product_id>
get_request("cart/612cbc9ff201aa8b286fcd13")

# DELETE request to /wishlist/<product_id>
get_request("wishlist/612cbc9ff201aa8b286fcd13")
