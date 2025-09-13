# Paso 1: Preguntar cuántos números se van a ingresar
cantidad = int(input("¿Cuántos números deseas ingresar? "))

# Paso 2: Crear una lista vacía para almacenar los números
vector = []

# Paso 3: Pedir los números uno por uno
for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    vector.append(numero)

# Paso 4: Mostrar el vector original
print("\nVector original ingresado:")
print(vector)

# Paso 5: Ordenar el vector de menor a mayor
vector_ordenado = sorted(vector)

# Paso 6: Mostrar el vector ordenado
print("\nVector ordenado de menor a mayor:")
print(vector_ordenado)