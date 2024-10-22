import os

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero."

def main():
    operacion = os.getenv("OPERACION", "suma")  # Valor por defecto: suma
    a = float(os.getenv("A", 0))
    b = float(os.getenv("B", 0))

    if operacion == "suma":
        resultado = suma(a, b)
    elif operacion == "resta":
        resultado = resta(a, b)
    elif operacion == "multiplicacion":
        resultado = multiplicacion(a, b)
    elif operacion == "division":
        resultado = division(a, b)
    else:
        resultado = "Operación no válida."

    print(f"El resultado de la operación es: {resultado}")
  

if __name__ == "__main__":
    main()
