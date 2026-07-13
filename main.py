from orquestador import AgenteOrquestador

def main():
    agente = AgenteOrquestador()
    
    pregunta = """
    Como piensa Burger King implementar la reducción de la jpornada laboral"""


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

    mensaje = respuesta["messages"][-1]

    print("Respuesta:\n")
    print(mensaje.content)

    #texto = respuesta["messages"][-1].content
    #print(texto)

if __name__ == "__main__":
    main()