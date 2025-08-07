# Sistema de Web Scraping Modular

Un sistema completo y modular que demuestra técnicas comunes de web scraping utilizando diferentes bibliotecas de Python.

## Características

El sistema incluye ejemplos de:

- Extracción de texto y atributos de páginas HTML
- Manejo de headers y sesiones
- Navegación por múltiples páginas (paginación)
- Relleno y envío de formularios
- Interacción con JavaScript dinámico usando Selenium
- Descarga de archivos (imágenes, PDF, etc.)
- Manejo de errores y proxies
- Parsing con BeautifulSoup y lxml
- Guardado de datos en CSV y JSON
- Uso de user agents aleatorios y rotación de headers
- Uso de WebDriver (Chrome) en modo headless
- Respeto del archivo robots.txt y del crawl-delay

## Estructura del Proyecto

```
PVC-OLDIVO/
├── data/                     # Carpeta para almacenar datos extraídos
├── scrapers/                 # Módulos de extracción
│   ├── extractor_requests.py # Extractor usando requests + BeautifulSoup
│   ├── extractor_selenium.py # Extractor usando Selenium WebDriver
│   ├── extractor_urllib.py   # Extractor usando urllib
│   └── extractor_lxml.py     # Extractor usando lxml
├── templates/                # Templates de Flask (no usado por scrapers)
├── utils/                    # Utilidades comunes
│   └── utils.py              # Funciones de utilidad compartidas
├── main.py                   # Punto de entrada principal
├── app.py                    # Aplicación Flask (no relacionada con scrapers)
└── requirements.txt          # Requisitos del proyecto
```

## Requisitos

```
requests==2.31.0
beautifulsoup4==4.12.2
selenium==4.15.2
lxml==4.9.3
urllib3==2.0.7
webdriver-manager==4.0.1
fake-useragent==1.4.0
tqdm==4.66.1
pandas==2.1.1
python-dotenv==1.0.0
Flask==3.1.1
```

## Instalación

1. Clone el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/PVC-OLDIVO.git
   cd PVC-OLDIVO
   ```

2. Cree un entorno virtual y actívelo:
   ```bash
   python -m venv venv
   # En Windows
   venv\Scripts\activate
   # En macOS/Linux
   source venv/bin/activate
   ```

3. Instale las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

### Ejecutar todos los demos

```bash
python main.py
```

### Ejecutar un demo específico

```bash
python main.py --demo requests   # Demo con requests
python main.py --demo selenium   # Demo con Selenium
python main.py --demo urllib     # Demo con urllib
python main.py --demo lxml       # Demo con lxml
```

## Detalles de los Extractores

### RequestsExtractor (extractor_requests.py)

Utiliza la biblioteca `requests` junto con `BeautifulSoup` para:
- Realizar solicitudes HTTP
- Manejar cookies y sesiones
- Extraer información de páginas web
- Descargar archivos
- Enviar formularios

### SeleniumExtractor (extractor_selenium.py)

Utiliza `Selenium WebDriver` para:
- Automatizar la navegación web
- Interactuar con elementos JavaScript dinámicos
- Completar formularios
- Hacer clic en elementos
- Realizar desplazamientos (scrolling)
- Tomar capturas de pantalla

### UrllibExtractor (extractor_urllib.py)

Utiliza la biblioteca estándar `urllib` junto con `BeautifulSoup` para:
- Realizar solicitudes HTTP básicas
- Manejar cookies
- Descargar archivos
- Enviar datos de formulario

### LxmlExtractor (extractor_lxml.py)

Utiliza `lxml` para:
- Análisis rápido de HTML y XML
- Extraer datos con XPath
- Procesar tablas HTML
- Trabajar con feeds RSS

## Buenas Prácticas Implementadas

- Respeto del archivo robots.txt
- Retrasos aleatorios entre solicitudes
- Rotación de user agents
- Manejo de errores y excepciones
- Código modular y reutilizable
- Documentación detallada

## Notas

Este proyecto es para fines educativos. Asegúrese de respetar los términos de servicio de los sitios web que visita y utilizar estas técnicas de manera ética y responsable.

## Licencia

MIT
