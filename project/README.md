# NLP Course Lab Repository

Este repositorio contiene mis laboratorios y ejercicios prácticos del curso de Procesamiento de Lenguaje Natural (NLP), incluyendo el proyecto de digitalización y estructuración de un diccionario Quechua-Español / Español-Quechua.

## Contenido del Curso y Proyecto

### Módulos Principales
- **Fundamentos de NLP**: Tokenización, normalización, y preprocesamiento de texto
- **Análisis Morfológico**: Stemming, lemmatización, y análisis de palabras
- **Modelos de Lenguaje**: N-gramas, modelos estadísticos y probabilísticos
- **Análisis Semántico**: Word embeddings, Word2Vec, GloVe
- **Clasificación de Texto**: Análisis de sentimientos, categorización de documentos
- **Modelos Avanzados**: Transformers, BERT, GPT
- **Aplicaciones Prácticas**: Chatbots, traducción automática, resumen de texto
- **Diccionario Quechua-Español**: Extracción, parsing y estructuración de diccionario bilingüe

## Tecnologías Utilizadas

- **Python**: Lenguaje principal de programación
- **NLTK, spaCy, scikit-learn, Transformers**
- **PyMuPDF, pdfplumber**: Extracción de texto de PDF
- **Pandas & NumPy**: Manipulación y análisis de datos
- **Jupyter Notebooks**: Desarrollo interactivo

## Estructura del Repositorio

```
nlp/
├── datasets/                  # Conjuntos de datos utilizados
├── utils/                     # Funciones auxiliares
├── requirements.txt           # Dependencias del proyecto
project/
├── diccionario-qeswa-academia-mayor.pdf   # Fuente original
├── diccionario_quechua_extractor.ipynb    # Proceso de extracción y parsing
├── diccionario_utils.py                   # Librería de consulta
├── quechua_espanol.json                   # Diccionario estructurado Q-E
├── espanol_quechua.json                   # Diccionario estructurado E-Q
├── abreviaturas.json                      # Abreviaturas y metadatos
├── diccionario_raw.txt                    # Texto crudo extraído
├── seccion_quechua_espanol.txt            # Texto limpio Q-E
├── seccion_espanol_quechua.txt            # Texto limpio E-Q
├── informe.md                             # Documentación técnica
└── __pycache__/                           # Archivos temporales Python
```

## Configuración del Entorno

### Prerrequisitos
```bash
Python 3.8+
pip
Jupyter Notebook
```

### Instalación
1. Clona este repositorio:
```bash
git clone <repository-url>
cd nlp
```

2. Crea un entorno virtual:
```bash
python -m venv nlp_env
source nlp_env/bin/activate  # En Windows: nlp_env\Scripts\activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. Descarga recursos adicionales:
```bash
python -m spacy download es_core_news_sm
python -m nltk.downloader punkt stopwords
```

## Proyecto Diccionario Quechua-Español

- Extracción y limpieza de texto desde PDF académico
- Parsing avanzado para identificar lemas, categorías, variantes, sinónimos y ejemplos
- Generación de archivos JSON estructurados y librería Python para consultas
- Validación automática y manual de resultados

**Resultados:**
- Más de 13,000 entradas Quechua-Español y 5,000 Español-Quechua
- Consultas eficientes por lema, categoría y campo semántico
- Recurso digital reutilizable para NLP y preservación lingüística

