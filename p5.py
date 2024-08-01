def give_string(template ,values):

    for key , value in values.items():
        template=template.replace(f"{{{key}}}", str(value))
    return template

template="My name is {name} and i am {age} years old"
values = {"name":"ayesha" , "age" : "34"}
result=give_string(template,values)
print(result)

