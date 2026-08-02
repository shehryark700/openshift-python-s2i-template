import os
import json
import platform
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
import socket # Import socket to catch socket.error

class DashboardHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        
        # Collect dynamic cluster/pod runtime statistics
        stats = {
            "status": "UP",
            "timestamp": datetime.now().isoformat(),
            "target_file": os.getenv('APP_FILE', 'Not Set'),
            "pod_node_os": platform.system(),
            "python_version": platform.python_version(),
            "environment_dump": {k: v for k, v in os.environ.items() if "OPENSHIFT" in k or "KUBERNETES" in k}
        }
        
        # Return beautifully formatted JSON
        self.wfile.write(json.dumps(stats, indent=4).encode('utf-8'))

if __name__ == '__main__':
    ports_to_try = [8080, 8081] # List of ports to attempt
    server = None

    for port in ports_to_try:
        try:
            print(f"🚀 System Utility dashboard booting up on port {port}...")
            server = HTTPServer(('0.0.0.0', port), DashboardHandler)
            server.serve_forever()
            break # If server starts successfully, break the loop
        except OSError as e:
            if e.errno == 98: # Address already in use
                print(f"Port {port} is already in use. Trying next port...")
            else:
                print(f"An unexpected error occurred: {e}")
                break
        except Exception as e:
            print(f"An unexpected error occurred while starting server: {e}")
            break
    
    if not server:
        print("Failed to start the server on any available port.")