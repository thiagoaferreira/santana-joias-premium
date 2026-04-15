#!/usr/bin/env python3
import http.server
import socketserver
import os
import requests
from urllib.parse import urlparse

class ProxyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Caminho do arquivo local
        local_path = self.translate_path(self.path)

        # Se o arquivo existe localmente, serve dele
        if os.path.exists(local_path) and os.path.isfile(local_path):
            return super().do_GET()

        # Caso contrário, tenta buscar do site original
        try:
            url = f"https://santanajoiaspremium.com.br{self.path}"
            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                self.send_response(200)
                self.send_header('Content-type', response.headers.get('Content-Type', 'text/html'))
                self.end_headers()
                self.wfile.write(response.content)
                return
        except:
            pass

        # Se não encontrar, retorna 404
        self.send_error(404, f"File not found: {self.path}")

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    PORT = 8000
    Handler = ProxyHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"✅ Servidor proxy rodando em http://localhost:{PORT}")
        print("Servindo arquivos locais e buscando do site original quando necessário")
        httpd.serve_forever()
