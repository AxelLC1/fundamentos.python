
# Diccionarios
# {"Clave": "valor"}

teacher = {
    "name": "Axel",
    "l_name": "Luna",
    "phone": "2411303365",
    "groups": ["3ADSM", "3BDSMN"]
}

print(type(teacher))
print(teacher)
print(teacher["name"])
print(teacher["groups"])
teacher["groups"].append("3CDSM")
teacher["phone"] = "2711309201"
teacher["city"] = "Huamantla"
print(teacher)
