#!/usr/bin/env python3
import http.server
import socketserver
import urllib.request
import os

class ProxyHandler(http.server.SimpleHTTPRequestHandler):
    BASE_URL = "https://santanajoiaspremium.com.br"

    def do_GET(self):
        # Se for index.html local, serve
        if self.path == "/" or self.path == "/index.html":
            return super().do_GET()

        # Para tudo mais, busca do site original
        try:
            url = self.BASE_URL + self.path
            print(f"Buscando: {url}")

            with urllib.request.urlopen(url, timeout=10) as response:
                content = response.read()
                content_type = response.headers.get('Content-Type', 'text/html')

                self.send_response(200)
                self.send_header('Content-Type', content_type)
                self.send_header('Content-Length', len(content))
                self.end_headers()
                self.wfile.write(content)
                return
        except Exception as e:
            print(f"Erro: {e}")
            self.send_error(404)

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    PORT = 8000

    with socketserver.TCPServer(("", PORT), ProxyHandler) as httpd:
        print(f"✅ Servidor proxy rodando em http://localhost:{PORT}")
        print("Servindo index.html local e buscando tudo mais do site original")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n✅ Servidor parado")
