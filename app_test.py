import requests

url = "http://127.0.0.1:5000/"
data = {
    "duedate" : "Sep 14, 2029",
    "from_addr" : {
        "company_name" : "Py App Tester Corp",
        "addr1" : "Magchi Galli",
        "addr2" : "Pudhacha Gaav"
    },
    "invoice_number" : 145,
    "items" : [
        {"title" : "brochure_design",
        "charge" : 500},
        {"title" : "conference",
        "charge" : 5000}
    ],
    "to_addr" : {
        "company_name" : "Gavatali app company",
        "addr1" : "shejarchi chaal",
        "addr2" : "Bajucha nagar"
    }    
}

html = requests.post(url, json = data)
with open("invoice.pdf", "wb") as f:
    f.write(html.content)


