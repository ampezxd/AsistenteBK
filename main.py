from orquestador import AgenteOrquestador

def main():
    agente = AgenteOrquestador()
    
    pregunta = """
    ¿Como piensa Burger king implementar el nuevo reglamento de reducción de horas?"""


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