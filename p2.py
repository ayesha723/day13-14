import json

def dict_json(dictionary):

    try:
        json_str = json.dumps(dictionary)
        restore_dict=json.loads(json_str)
        return restore_dict
    
    except(TypeError, json.JSONDecodeError) as e:
         return {"error": "Conversion failed", "original": dictionary}
    
dictionary={"name" : "ayesha " , "age" : "21"}
result =dict_json(dictionary)
print(result)
