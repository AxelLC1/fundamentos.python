def saluda():
    print("Hola a Todos!")

saluda()

# Con parametros, sin retorno
def duplica(num):
    print(num * 2)

duplica(5)

def suma(num1, num2):
    print(f"la suma de los numeros es: { num1 + num2}")

suma(23, 45)

# Prametros opcionales, sin retorno
def get_lista(al_1 = "Jose", al_2 = "Darlen"):
    return [al_1, al_2]

my_list = get_lista()
print(my_list)
my_list = get_lista("Peter")
print(my_list)
my_list = get_lista("Peter Parker", "Tony Stark")
print(my_list)
my_list = get_lista(al_2="Peter Parker", al_1="Tony Stark")
print(my_list)