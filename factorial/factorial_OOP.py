class Factorial:
    def __init__(self):
        pass

    def factorial(self, num):
        """factorial de un solo número"""
        if num < 0:
            print(f"Factorial de un número negativo ({num}) no existe.")
            return None
        elif num == 0:
            return 1
        fact = 1
        while num > 1:
            fact *= num
            num -= 1
        return fact

    def run(self, min_val, max_val):
        """calcular los factoriales en el rango [min_val, max_val]"""
        for num in range(min_val, max_val + 1):
            print(f"El factorial de {num} es: {self.factorial(num)}")


if __name__ == "__main__":
    input_values = input("Ingrese el rango min-max (ejemplo: 4-8): ")

    try:
        min_val, max_val = map(int, input_values.split('-'))
        factorial_obj = Factorial()
        factorial_obj.run(min_val, max_val)
    except ValueError:
        print("Incorrecto. Pruebe con el rango min-max.")
