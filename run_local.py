#!/usr/bin/env python3
import http.server
import socketserver
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, must-revalidate')
        super().end_headers()

with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"🚀 Servidor rodando em http://localhost:{PORT}")
    print(f"📁 Servindo de: {os.getcwd()}")
    print(f"Pressione Ctrl+C para parar")
    httpd.serve_forever()
