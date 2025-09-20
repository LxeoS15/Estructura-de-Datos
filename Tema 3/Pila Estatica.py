class PilaEstatica:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pila = [None] * capacidad
        self.tope = -1

    def push(self, elemento):
        if self.tope < self.capacidad - 1:
            self.tope += 1
            self.pila[self.tope] = elemento
        else:
            print("Pila llena")

    def pop(self):
        if self.tope >= 0:
            elemento = self.pila[self.tope]
            self.tope -= 1
            return elemento
        else:
            print("Pila vacía")

    def peek(self):
        return self.pila[self.tope] if self.tope >= 0 else None