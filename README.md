# 🍔 Asistente BK

Asistente BK es un asistente inteligente basado en una arquitectura **RAG (Retrieval-Augmented Generation)** diseñado para responder preguntas sobre el **Reglamento Interno de Trabajo de Burger King Colombia**.

En lugar de responder únicamente con el conocimiento del modelo de lenguaje, el asistente recupera primero la información más relevante desde una base vectorial utilizando embeddings y posteriormente genera una respuesta fundamentada en el contenido del reglamento.

---

## 🚀 Características

- 📄 Consulta el Reglamento Interno de Trabajo de Burger King Colombia.
- 🧠 Arquitectura RAG.
- 🔍 Recuperación semántica mediante embeddings.
- 📦 Base vectorial utilizando Pinecone.
- 🤖 Respuestas generadas con Gemini.
- 🌐 Interfaz web desarrollada con Streamlit.
- ❌ Evita alucinaciones indicando cuando la información no existe en el reglamento.

---

# 🏗 Arquitectura

```text
                 Usuario
                    │
                    ▼
          Interfaz Streamlit
                    │
                    ▼
               Retriever
                    │
                    ▼
              Pinecone Vector DB
                    │
          Recupera documentos
                    │
                    ▼
           Prompt + Contexto
                    │
                    ▼
             Gemini 2.5 Flash
                    │
                    ▼
               Respuesta
```

---

# ⚙ Tecnologías

- Python
- LangChain
- Pinecone
- Google Gemini
- HuggingFace Embeddings
- multilingual-e5-small
- Streamlit

---

# 📚 Flujo del sistema

1. El usuario realiza una pregunta.
2. La pregunta es convertida en un embedding.
3. Pinecone busca los fragmentos más similares.
4. Los fragmentos recuperados se incorporan al prompt.
5. Gemini genera la respuesta utilizando únicamente ese contexto.
6. La respuesta es enviada al usuario.

---

# 🧠 Procesamiento del documento

El reglamento se divide automáticamente utilizando **RecursiveCharacterTextSplitter**, respetando la estructura del documento (capítulos, artículos y saltos de línea).

Cada fragmento:

- se convierte en un embedding mediante **multilingual-e5-small**
- se almacena en Pinecone
- posteriormente puede recuperarse mediante búsqueda semántica.

---

# 🔍 Modelo de embeddings

Se utiliza:

```
intfloat/multilingual-e5-small
```

Este modelo permite obtener representaciones vectoriales multilingües optimizadas para tareas de recuperación de información (Information Retrieval).

---

# 🤖 Modelo de lenguaje

Las respuestas son generadas mediante:

```
Gemini 2.5 Flash
```

El modelo recibe únicamente los fragmentos recuperados por Pinecone para reducir alucinaciones y responder exclusivamente con información presente en el reglamento.

---

# 🌐 Interfaz

La aplicación cuenta con una interfaz desarrollada en Streamlit que permite realizar consultas de manera sencilla.

Características:

- historial de conversación
- mensajes tipo chat
- manejo de errores de la API
- respuesta en tiempo real

---

# 💻 Instalación

Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/AsistenteBK.git
```

Entrar al proyecto

```bash
cd AsistenteBK
```

Crear entorno virtual

```bash
python -m venv venv
```

Activarlo

Windows

```bash
venv\Scripts\activate
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

Crear un archivo

```
my_keys.py
```

con las llaves correspondientes.

```python
GEMINI_API_KEY="..."
PINECONE_API_KEY="..."
```

Ejecutar

```bash
streamlit run app.py
```

---

# 🎯 Ejemplos de preguntas

- ¿Cuánto dura el descanso del personal operativo?
- ¿Cómo se implementará la reducción de la jornada laboral?
- ¿Cuántos descansos obligatorios existen?
- ¿Qué documentos debo presentar para ingresar a la empresa?
- ¿Cómo funciona el período de prueba?

---

# 🚧 Mejoras futuras

- Memoria conversacional.
- Citas automáticas de artículos.
- Re-ranking de documentos.
- Recuperación híbrida (BM25 + Embeddings).
- Soporte para múltiples documentos.
- Panel administrativo para actualizar la base de conocimiento.

---

# 👨‍💻 Autor

**Andrés Gutiérrez**

Tecnólogo en Desarrollo de Software

Intereses:

- Inteligencia Artificial
- LangChain
- Sistemas RAG
- Java & Spring Boot
- Backend Development

GitHub:
```
https://github.com/ampezxd
```
