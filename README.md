# VIdeo_converter
Este es un ejemplo de trabajo para los estudios en Python que es convertir un video en internet en un formato MP4, realizarlo en línea y con la posibilidad de poder  bajarlo a una carpeta determinada.
“Este es un caso solo para estudiar la forma de programación en Python, en ningún caso sobrepasa a atenta con la propiedad intelectual bajo la norma y Licencia MIT”

Se toma como ejemplo la plataforma de Youtube utilizando video de libre uso.

Requisitos Funcionales:
1.	Recibir un link de video de internet como entrada
2.	Convertir el video a formato MP4
3.	Permitir la descarga del archivo convertido
4.	Manejo de errores y logging
5.	Selección de directorio de destino para guardar el archivo
6.	Ejecución en línea (web)
Tecnologías Recomendadas:
1.	Backend: Python 
o	pytube: Para descargar videos de YouTube
o	Flask: Framework web ligero
o	logging: Para manejo de logs
o	moviepy: Para manipulación de videos
2.	Frontend: 
o	HTML/CSS
o	JavaScript
o	Bootstrap para el diseño
Razones de la selección:
•	Python tiene excelentes bibliotecas para manipulación de videos
•	Flask es ligero y perfecto para aplicaciones web simples
•	Fácil integración con bibliotecas de procesamiento de video
•	Multiplataforma




Estructura de Archivos
proyecto/
├── app.py
├── templates/
│   └── index.html
├── downloads/
└── logs/

PASO 1: Preparación del Entorno
1.	Primero, crea un nuevo directorio para el proyecto:
bash
mkdir youtube_converter  
cd youtube_converter  
2.	Crea un entorno virtual (recomendado):
bash
python -m venv venv  
pip install --upgrade pytube   
# Para Windows:  
venv\Scripts\activate  
  
# Para Linux/Mac:  
source venv/bin/activate  
3.	Instala las dependencias necesarias:
bash
Copy Code
pip install flask pytube  
pip install yt-dlp
PASO 2: Estructura del Proyecto
Crea la siguiente estructura de directorios:
bash
Copy Code
mkdir templates  
mkdir downloads  
mkdir logs  
PASO 3: Crear los Archivos
1.	Crea el archivo app.py en el directorio principal:
 
PASO 4: Ejecutar la Aplicación
1.	Asegúrate de estar en el directorio del proyecto y que el entorno virtual esté activado.
2.	Ejecuta la aplicación:
bash
Copy Code
python app.py  
3.	Abre tu navegador y ve a:
http://localhost:5000  
Uso del programa:
1.	Pega una URL de YouTube válida en el campo de entrada
2.	Haz clic en "Convertir"
3.	Espera a que el proceso termine
4.	Cuando esté listo, aparecerá el botón de descarga
5.	Haz clic en "Descargar MP4" para obtener tu video
Características implementadas:
•	Interfaz web responsive
•	Indicador de carga durante la conversión
•	Manejo de errores con mensajes claros
•	Sistema de logging completo
•	Nombres de archivo seguros y únicos
•	Descarga directa del archivo convertido
Los archivos de log se guardarán en:
logs/youtube_converter.log  
Los videos descargados se guardarán en:
downloads/  
Consideraciones importantes:
1.	Asegúrate de tener una conexión a Internet estable
2.	Los videos muy grandes pueden tardar más en procesarse
3.	Algunos videos pueden estar restringidos y no ser descargables
4.	El programa maneja automáticamente caracteres especiales en los nombres de archivo


 
