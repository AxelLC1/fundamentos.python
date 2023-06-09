# Function input -> retorna string 
name = input('como te llamas? \n')
age = int(input('Cuantos años tienes? \n'))
future = int(input('Cuantos años mas? \n'))

print("Hola \t" + name)
print("En \t" + str(future) + "años tendras \t" + str( age + future))

# Format Strings
"""
    Hola Axel, en 3 años tendras 24 años
"""
text_complete = "Hola {}, en {} años tendras {} años"
print(text_complete.format(name, future, age + future))

print(f"Hola {name}, en {future} años tendras {age + future} años")
