import environment
import vacuum


def menu():
    print(
        "Bienvenido al entorno de aspiradora. Escoge una opción: \n"
        "\t 1. Ambiente aleatorio\n"
        "\t 2. Ambiente personalizado\n"
    )

    opt = int(input("Ingrese una opcion: "))
    while opt < 0 or opt > 2:
        print("Opción no válida, escoge de nuevo")
        opt = int(input("Ingrese una opcion: "))
    return opt


def main():
    # Declaramos un entorrno
    environ = environment.Environment()

    opt = menu()
    if opt == 1:
        environ.createRandom()
    else:
        environ.createCustom()
    
    environ.clean()
    performance = environ.vacuum.performance()
    print(f'Performance: {performance}')


if __name__ == "__main__":

    main()
