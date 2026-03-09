for multiplicar in range(1, 11):
    print(f"Tabla de multiplicar del {multiplicar}:")
    for multiplicando in range(1, 11):
        resultado = multiplicar * multiplicando
        print(f"{multiplicar} x {multiplicando} = {resultado}")
        print()  # Imprime una línea en blanco para separar las tablas
        