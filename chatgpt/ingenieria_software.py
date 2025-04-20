"""
Este programa permite realizar consultas a la API de OpenAI (ChatGPT),
recordando la última consulta ingresada para reutilizarla fácilmente.
"""

# Importamos la biblioteca de OpenAI para usar ChatGPT
import openai

# Clave API de OpenAI
openai.api_key = "sk-proj-3-oj6Ajm_9dwhTNnCvxyNglgQsNePRYjLTItjPt_qUn15kKeeMYP" \
"TspdCP8QnYYmUgPBH7wYdZT3BlbkFJxMDKJvew2DlUTixdTMT-pd9eZrUPNlTEDc5i9nthLC570E" \
"oyqj6CJvptY13rgk95t_1McnhggA"
# Guardamos la última consulta ingresada por el usuario para que pueda volver a usarla más
#  tarde con la Flecha Arriba.
ULTIMA_CONSULTA = ""

def obtener_respuesta_chatgpt(cons):
    """
    Envía una consulta a ChatGPT y obtiene una respuesta.
    Parámetros:
        cons (str): La consulta que el usuario desea hacer a ChatGPT.
    Retorna:
        str: La respuesta generada por ChatGPT.
    """
    try:
        response = openai.ChatCompletion.create(
            # Llama a la API de OpenAI con el modelo GPT-4o-mini
            model="gpt-4o-mini-2024-07-18",  # Modelo elegido
            messages=[
                {"role": "system", "content": "Eres un asistente útil."},
                # Mensaje inicial que define el rol del asistente
                {"role": "user", "content": cons}  # Consulta del usuario
            ],
            max_tokens=150,  # Límite máximo de tokens en la respuesta
            temperature=0.7  # Nivel de aleatoriedad en las respuestas
        )
        return response['choices'][0]['message']['content'].strip()
    except openai.error.Timeout as e:
        # Maneja errores de tiempo de espera
        return f"Se agotó el tiempo de espera: {str(e)}"
    except openai.error.OpenAIError as e:
        # Maneja errores de la API de OpenAI
        return f"Error al interactuar con la API de OpenAI: {str(e)}"
    except ValueError as e:
        # Maneja errores específicos de valor (como parámetros incorrectos)
        return f"Error con los valores proporcionados: {str(e)}"
    except (KeyboardInterrupt, SystemExit) as e:
        return f"Proceso interrumpido: {str(e)}"
    # Caso general de error inesperado
    return "Error inesperado en el procesamiento."

def pedir_consulta(ultima_consulta):
    """
    Función auxiliar para simplificar la entrada del usuario.
    Si hay una consulta anterior, la ofrece como opción.
    Retorna:
        str: La consulta ingresada por el usuario o la última consulta.
    """
    # Si hay una consulta anterior, la ofrece como opción
    if ultima_consulta:
        print(f"Última consulta: '{ultima_consulta}'")  # Muestra la última consulta
        consulta = input("Introduce tu consulta (o presiona Enter para usar la última): ").strip()
        return consulta or ultima_consulta  # Si no escribe nada, se reutiliza la última
    # Si no hay una anterior, pide una nueva consulta
    return input("Introduce tu consulta: ").strip()

def consulta_usuario():
    """
    Esta función gestiona el ingreso de consultas del usuario,
    mostrando la última ingresada y permitiendo volver a usarla.
    """
    ultima_consulta = ""  # Localiza la variable aquí
    try:
        while True:
            consulta = pedir_consulta(ultima_consulta)  # Pasa la última consulta
            if not consulta:
                print("La consulta no puede estar vacía.")  # Mensaje al usuario solicitando
                continue  # Vuelve al inicio del bucle

            print(f"You: {consulta}")  # Mostramos lo que el usuario escribió
            try:
                # Intentamos obtener la respuesta de ChatGPT
                respuesta = obtener_respuesta_chatgpt(consulta)  # Obtiene la respuesta de ChatGPT
                print(f"chatGPT: {respuesta}")  # Muestra la respuesta
            except openai.error.Timeout as e:
                # Maneja errores de tiempo de espera
                print(f"Se agotó el tiempo de espera: {str(e)}")
            except openai.error.OpenAIError as e:
                # Maneja errores de la API de OpenAI
                print(f"Error al interactuar con la API de OpenAI: {str(e)}")
            except ValueError as e:
                # Maneja errores específicos de valor (como parámetros incorrectos)
                print(f"Error con los valores proporcionados: {str(e)}")
            except (KeyboardInterrupt, SystemExit) as e:
                # Maneja interrupciones o salida del sistema
                print(f"Proceso interrumpido o salida del sistema: {str(e)}")

        ultima_consulta = consulta  # Actualiza la última consulta
    except KeyboardInterrupt as e:
        # Captura interrupciones fuera del bucle principal
        print(f"Proceso interrumpido: {str(e)}")
    except SystemExit as e:
        # Captura la salida del sistema
        print(f"Salida del sistema: {str(e)}")

# Punto de entrada principal del programa
if __name__ == "__main__":
    consulta_usuario()
