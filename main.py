from rag import responder

def main():

    print("=" * 60)
    print("Asistente BK - Reglamento Interno")
    print("Escribe 'salir' para terminar.")
    print("=" * 60)

    while True:

        pregunta = input("\nPregunta: ")

        if pregunta.lower() in ["salir", "exit", "quit"]:
            print("\n¡Hasta luego!")
            break

        respuesta = responder(pregunta)

        print("\nRespuesta:\n")
        print(respuesta)


if __name__ == "__main__":
    main()