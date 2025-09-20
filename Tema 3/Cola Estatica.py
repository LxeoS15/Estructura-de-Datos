class ColaEstatica:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cola = [None] * capacidad
        self.inicio = 0
        self.fin = -1
        self.tamano = 0

    def enqueue(self, elemento):
        if self.tamano < self.capacidad:
            self.fin = (self.fin + 1) % self.capacidad
            self.cola[self.fin] = elemento
            self.tamano += 1
        else:
            print("Cola llena")

    def dequeue(self):
        if self.tamano > 0:
            elemento = self.cola[self.inicio]
            self.inicio = (self.inicio + 1) % self.capacidad
            self.tamano -= 1
            return elemento
        else:
            print("Cola vacía")