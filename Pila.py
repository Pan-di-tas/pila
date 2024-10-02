class Pila:
    def __init__(self):
        # Inicializamos la pila como una lista vacía
        self.pila = []

    def esta_vacia(self):
        # Devuelve True si la pila está vacía, False si no
        return len(self.pila) == 0

    def apilar(self, item):
        # Agrega un elemento a la pila (al final de la lista)
        self.pila.append(item)

    def desapilar(self):
        # Elimina y devuelve el último elemento de la pila
        # Si la pila está vacía, muestra un mensaje de advertencia
        if self.esta_vacia():
            return "La pila está vacía, no se puede desapilar."
        return self.pila.pop()

    def ver_tope(self):
        # Devuelve el último elemento de la pila sin eliminarlo
        if self.esta_vacia():
            return "La pila está vacía."
        return self.pila[-1]

    def mostrar_pila(self):
        # Muestra el contenido actual de la pila
        return self.pila

# Ejemplo de uso
if __name__ == "__main__":
    pila = Pila()

    pila.apilar(10)
    pila.apilar(20)
    pila.apilar(30)

    print("Pila actual:", pila.mostrar_pila())
    print("Elemento en el tope:", pila.ver_tope())

    print("Desapilar:", pila.desapilar())
    print("Pila después de desapilar:", pila.mostrar_pila())

    print("Desapilar:", pila.desapilar())
    print("Pila después de desapilar:", pila.mostrar_pila())

    print("Desapilar:", pila.desapilar())
    print("Intentando desapilar de nuevo:", pila.desapilar())
