from flask import Flask, render_template, request, send_file
import os
import json
from importjson import processar_json_arquivo  # Importa apenas a função principal

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'outputs'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "Nenhum arquivo enviado."
    
    file = request.files['file']

    if file.filename == '':
        return "Nenhum arquivo selecionado."

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        try:
            resultados = processar_json_arquivo(filepath, app.config['OUTPUT_FOLDER'])
        
            return render_template('resultado.html', **resultados)

        except (ValueError, KeyError) as e:
            # Captura erros de validação (JSON mal formatado, colunas faltando)
            # vindos de importjson.py
            return f"Erro ao processar o arquivo: {str(e)}. Por favor, verifique o formato do JSON e se todas as colunas necessárias estão presentes."
        except Exception as e:
            # Captura outros erros inesperados
            return f"Ocorreu um erro inesperado durante o processamento: {str(e)}"
        # --- FIM DO BLOCO ATUALIZADO ---

# Rota de download permanece a mesma
@app.route('/download/<path:filename>')
def download(filename):
    return send_file(filename, as_attachment=True)

# Função desnecessária removida
# def detectar_tipo_json(filepath): ...

if __name__ == '__main__':
    app.run(debug=True)