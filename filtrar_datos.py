#############
nombres = [
    "Harry Houdini",
    "Newton",
    "David Blaine",
    "Hawking",
    "Messi",
    "Teller",
    "Einstein",
    "Pele",
    "Juanes"
]

magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]

otros = [nombre for nombre in nombres if nombre not in magos and nombre not in cientificos]
# hace lo mismo
# otros = []
# for nombre in nombres:
#     if nombre not in magos and nombre not in cientificos:
#         otros.append(nombre)
print(otros, "k")

def hacer_grandioso(nombre):
    return "El gran " + nombre

def imprimir_nombres(lista):
    for nombre in lista:
        print(nombre)

print("Lista de nombres antes de la modificación:")
imprimir_nombres(nombres)
print()

# magos_grandiosos = [hacer_grandioso(mago) for mago in magos]
magos_grandiosos = []
for mago in magos:
    magos_grandiosos.append(hacer_grandioso(mago))


cientificos.sort()
otros.sort()

print("Nombres de los magos grandiosos:")
imprimir_nombres(magos_grandiosos)
print()

print("Nombres de los científicos:")
imprimir_nombres(cientificos)
print()

print("Nombres restantes:")
imprimir_nombres(otros)


