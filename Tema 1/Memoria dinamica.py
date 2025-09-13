def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generar_primos(limite):
    primos = []  # Memoria dinámica: lista que crece según se agregan elementos
    for num in range(2, limite + 1):
        if es_primo(num):
            primos.append(num)  # Se reserva espacio en tiempo de ejecución
    return primos

if __name__ == "__main__":
    limite = int(input("Ingresa el límite superior para generar primos: "))
    lista_primos = generar_primos(limite)
    print(f"Números primos hasta {limite}:")
    print(lista_primos)