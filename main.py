def obtener_numero_natural():
    """Solicita y valida la entrada de un número natural positivo"""
    while True:
        try:

            numero = int(input("Ingrese un número natural positivo: "))
            if numero <= 0:
                raise ValueError("El número debe ser un natural positivo.")
            return numero
        except ValueError as e:
            print(f"Entrada no válida: {e}. Por favor, intente nuevamente.")


def calcular_divisores(numero):
    """Calcula los divisores de un número natural"""
    divisores = [i for i in range(1, numero + 1) if numero % i == 0]
    return divisores


def main():
    numero = obtener_numero_natural()

    divisores = calcular_divisores(numero)

    print(f"Los divisores de {numero} son: {divisores}")


if __name__ == "__main__":
    main()
