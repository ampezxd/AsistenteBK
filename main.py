from orquestador import AgenteOrquestador

def main():
    agente = AgenteOrquestador()
    
    pregunta = """
    ¿Cuáles son los horarios de trabajo para los empleados de Burger King?"""


    respuesta = agente.agente.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": pregunta
                }
            ]
        }
    )

    texto = respuesta["messages"][-1].content
    print(texto)

if __name__ == "__main__":
    main()