print("Hola mundo soy Dani Fuster Latorre")
print("Hola mundo soy Dani Fuster Latorre")

#soy duende de loco 
print("Hola mundo soy Dani Fuster Latorre")

"""
texto que no se va a interpretar, va serios
texto que no se va a interpretar, va serios
texto que no se va a interpretar, va serios
"""

#variables

texto = "repaso de python"
nombre = "DANI"
altura = "177cm"
year = 2023

print(f"{texto} - {nombre} - {altura} - {str(year)}") 
print(texto + "  - "  + nombre + "  -  " + altura + "  - " + str(year)) 

# Entrada
#sitioweb = input("¿Cual es tu página web?: ")
#print("El sitio web del usuario es: " + sitioweb)

# Condiciones 
"""
altura = int(input("¿Cual es tu página web?: "))
if altura >= 170:
    print ("Eres una persona alta!!")
else:
    print ("Eres bajito!!")
"""

# Funciones
"""
var_altura = int(input("¿Cual es tu página web?: "))

def mostrarAltura(altura):
    resultado = ""

    if altura >= 170:
         resultado = "Eres una persona alta!!"
    else:
         resultado = "Eres bajito!!"
    
    return resultado

print(mostrarAltura(var_altura))
"""

# Listas
personas = ["Víctor", "Paco", "Pepe"]
print(personas[2])

for persona in personas:
    print("-" + persona)
