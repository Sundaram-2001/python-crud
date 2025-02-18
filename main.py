import json
with open('data.json','r') as file:
    data=json.load(file)
formatted_data=json.dumps(data,indent=4)
print(formatted_data)




