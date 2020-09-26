import json 
  
# Opening JSON file 
with open('pollution_data.json', 'r') as data: 
  
    # Reading from json file 
    json_object = json.load(data) 
  
print(json_object) 