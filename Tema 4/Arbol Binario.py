class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        self.raiz = self._insertar_rec(self.raiz, dato)

    def _insertar_rec(self, nodo, dato):
        if nodo is None:
            return Nodo(dato)
        if dato < nodo.dato:
            nodo.izquierda = self._insertar_rec(nodo.izquierda, dato)
        else:
            nodo.derecha = self._insertar_rec(nodo.derecha, dato)
        return nodo

    def buscar(self, dato):
        return self._buscar_rec(self.raiz, dato)

    def _buscar_rec(self, nodo, dato):
        if nodo is None or nodo.dato == dato:
            return nodo
        if dato < nodo.dato:
            return self._buscar_rec(nodo.izquierda, dato)
        else:
            return self._buscar_rec(nodo.derecha, dato)

    def eliminar(self, dato):
        self.raiz = self._eliminar_rec(self.raiz, dato)

    def _eliminar_rec(self, nodo, dato):
        if nodo is None:
            return nodo
        if dato < nodo.dato:
            nodo.izquierda = self._eliminar_rec(nodo.izquierda, dato)
        elif dato > nodo.dato:
            nodo.derecha = self._eliminar_rec(nodo.derecha, dato)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            temp = self._minimo(nodo.derecha)
            nodo.dato = temp.dato
            nodo.derecha = self._eliminar_rec(nodo.derecha, temp.dato)
        return nodo

    def _minimo(self, nodo):
        while nodo.izquierda:
            nodo = nodo.izquierda
        return nodo