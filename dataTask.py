import  json
my_data ={
    "name": "mahefa",
    "age": 25 ans,
    "nationalite": "malagasy"
         }
with open ("data.json","w") as f:
         json.dump(my_data, f)
print("dictionary saved to data.json")
