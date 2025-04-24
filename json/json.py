jsondata = {
  "customers": [
    {
      "name": "Meessam",
      "date_joined": "23-4-20",
      "balance": 20000,
      "card_type": "Mastercard"
    },
    {
      "name": "Hassan",
      "date_joined": "23-4-20",
      "balance": 2000000,
      "card_type": "Mastercard"
    },

    {
      "name": "Ayan",
      "date_joined": "23-4-20",
      "balance": 200,
      "card_type": "Mastercard"
    },

    {
      "name": "Basil",
      "date_joined": "23-4-20",
      "balance": 20000,
      "card_type": "Mastercard"
    }

  ]
}


for index in range(0,len(jsondata['customers'])):
    print(f"Name: {jsondata['customers'][index]['name']}")
    print(f"Name: {jsondata['customers'][index]['date_joined']}")
    print(f"Name: {jsondata['customers'][index]['balance']}")
    print(f"Name: {jsondata['customers'][index]['card_type']}")

    print()  

