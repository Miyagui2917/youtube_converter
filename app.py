from flask import Flask, render_template, request, send_file, jsonify
import os
import logging
from datetime import datetime
import yt_dlp

app = Flask(__name__)

# Configuración del logging
def setup_logging():
    log_filename = f'logs/youtube_converter_{datetime.now().strftime("%Y%m%d")}.log'
    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def setup_directories():
    """Crear directorios necesarios si no existen"""
    dirs = ['downloads', 'logs']
    for dir in dirs:
        if not os.path.exists(dir):
            os.makedirs(dir)

def download_video(url):
    """Función para descargar video usando yt-dlp"""
    try:
        # Configuración de opciones para yt-dlp
        ydl_opts = {
            'format': 'mp4',
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'quiet': True,
            'noplaylist': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            logging.info(f"Video descargado exitosamente: {filename}")
            return {
                'success': True,
                'filename': filename,
                'title': info.get('title', 'Video sin título')
            }

    except Exception as e:
        logging.error(f"Error al descargar el video: {str(e)}")
        return {
            'success': False,
            'error': str(e)
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_video():
    try:
        youtube_url = request.form['url']
        logging.info(f"Iniciando conversión del video: {youtube_url}")

        # Descargar el video
        result = download_video(youtube_url)

        if result['success']:
            return jsonify({
                'status': 'success',
                'message': f'Video "{result["title"]}" convertido exitosamente',
                'filename': result['filename']
            })
        else:
            return jsonify({
                'status': 'error',
                'message': f'Error en la conversión: {result["error"]}'
            }), 500

    except Exception as e:
        error_message = f"Error inesperado: {str(e)}"
        logging.error(error_message)
        return jsonify({
            'status': 'error',
            'message': error_message
        }), 500

@app.route('/download/<path:filename>')
def download_file(filename):
    try:
        return send_file(filename, as_attachment=True)
    except Exception as e:
        logging.error(f"Error en la descarga: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': 'Error al descargar el archivo'
        }), 500

@app.errorhandler(Exception)
def handle_error(error):
    message = str(error)
    logging.error(f"Error no manejado: {message}")
    return jsonify({
        'status': 'error',
        'message': message
    }), 500

if __name__ == '__main__':
    setup_directories()
    setup_logging()
    app.run(debug=True)