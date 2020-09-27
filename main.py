import environment
import vacuum

def menu():
    print(
        "Bienvenido al entorno de aspiradora. Escoge una opción: "
        "\t 1. Ambiente aleatorio"
        "\t 2. Ambiente personalizado"
    )

    opt = int(input("Ingrese una opcion: "))
    while opt < 0 or opt > 2:
        print("Opción no válida, escoge de nuevo")
        opt = int(input("Ingrese una opcion: "))
    return opt


def main():
    # Declaramos un entorrno
    environment = environment.Environment()

    opt = menu()
    if opt == 1:
        environment.createRandom()
    else:
        environment.createCustom()
    print("Este es tu nuevo ambiente: ")
    print(environment.matrix)

    vacuum = vacuum.VacuumCleaner()
    vacuum.environment = environment


if __name__ == "__main__":
    main()
