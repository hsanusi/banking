import requests

endpoint = "http://localhost:8000/thirdparty/api/create_customer/"

form = {
        "id": 6,
        "customer_id": "0007",
        "title": "Dr",
        "surname": "Haruna",
        "first_name": "Baraqat",
        "other_name": "Oluwatobi",
        "sex": "F",
        "date_of_birth": "2018-02-01",
        "home_address": "6, Broad Street\r\nMarina",
        "phone": "08120808094",
        "occupation": "Software Developer",
        "office_address": "13, Nnadi Street Off Liasu Road Via Ile Iwe Bus Stop",
        "email": "harunabaraqat@ncr.com",
        "marital_status": "Married",
        "status": True,
        "next_of_kin": "Sanusi Babatunde",
        "next_of_kin_phone": "08023527520",
        "passport": None,
        "group": 2,
        "registered_by": 1
    }
print(5 - float("-inf"))
# get_response = requests.get(endpoint, json={"query": "Hello Customers"})
get_response = requests.post(endpoint,json=form)

# print(get_response.status_code)
# print(get_response.json())
