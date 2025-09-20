# NLP Course Lab Repository

Este repositorio contiene mis laboratorios y ejercicios prácticos del curso de Procesamiento de Lenguaje Natural (NLP).

## 📚 Contenido del Curso

### Módulos Principales
- **Fundamentos de NLP**: Tokenización, normalización, y preprocesamiento de texto
- **Análisis Morfológico**: Stemming, lemmatización, y análisis de palabras
- **Modelos de Lenguaje**: N-gramas, modelos estadísticos y probabilísticos
- **Análisis Semántico**: Word embeddings, Word2Vec, GloVe
- **Clasificación de Texto**: Análisis de sentimientos, categorización de documentos
- **Modelos Avanzados**: Transformers, BERT, GPT
- **Aplicaciones Prácticas**: Chatbots, traducción automática, resumen de texto

## 🛠️ Tecnologías Utilizadas

- **Python**: Lenguaje principal de programación
- **NLTK**: Natural Language Toolkit
- **spaCy**: Librería industrial de NLP
- **scikit-learn**: Machine learning y clasificación
- **Transformers (Hugging Face)**: Modelos pre-entrenados
- **Pandas & NumPy**: Manipulación y análisis de datos
- **Matplotlib & Seaborn**: Visualización de datos
- **Jupyter Notebooks**: Desarrollo interactivo

## 📁 Estructura del Repositorio

```
nlp/
├── lab01_fundamentos/          # Introducción y preprocesamiento
├── lab02_tokenization/         # Técnicas de tokenización
├── lab03_morphology/           # Análisis morfológico
├── lab04_ngrams/              # Modelos de N-gramas
├── lab05_embeddings/          # Word embeddings
├── lab06_classification/       # Clasificación de texto
├── lab07_sentiment/           # Análisis de sentimientos
├── lab08_transformers/        # Modelos transformer
├── datasets/                  # Conjuntos de datos utilizados
├── utils/                     # Funciones auxiliares
└── requirements.txt           # Dependencias del proyecto
```

## 🚀 Configuración del Entorno

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

## 📖 Cómo Usar Este Repositorio

1. **Navega por los laboratorios**: Cada carpeta `lab##_*` contiene ejercicios específicos
2. **Ejecuta los notebooks**: Abre Jupyter Notebook y explora los archivos `.ipynb`
3. **Experimenta con los datos**: Utiliza los datasets en la carpeta `datasets/`
4. **Consulta las utilidades**: Revisa funciones comunes en `utils/`

## 🎯 Laboratorios Destacados

### Lab 01: Fundamentos
- Limpieza y normalización de texto
- Manejo de encoding y caracteres especiales
- Expresiones regulares para NLP

### Lab 05: Word Embeddings
- Implementación de Word2Vec desde cero
- Comparación de diferentes modelos de embeddings
- Visualización en espacios dimensionales reducidos

### Lab 08: Transformers
- Fine-tuning de modelos BERT
- Implementación de tareas de clasificación
- Análisis de atención en transformers

## 📊 Datasets Utilizados

- **Corpus de noticias en español**
- **Reviews de productos (Amazon)**
- **Tweets para análisis de sentimientos**
- **Corpus literario clásico**
- **Documentos científicos**

## 🔗 Recursos Adicionales

- [Documentación NLTK](https://www.nltk.org/)
- [spaCy Documentation](https://spacy.io/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Papers with Code - NLP](https://paperswithcode.com/area/natural-language-processing)

## 📝 Notas del Curso

- Cada laboratorio incluye ejercicios teóricos y prácticos
- Los notebooks contienen explicaciones detalladas y comentarios
- Se incluyen ejemplos en español y otros idiomas
- Los proyectos finales integran múltiples técnicas aprendidas

## 🤝 Contribuciones

Este repositorio es para fines educativos. Las mejoras y sugerencias son bienvenidas a través de issues y pull requests.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---

**Autor**: Ciro  
**Curso**: Procesamiento de Lenguaje Natural  
**Última actualización**: $(date)