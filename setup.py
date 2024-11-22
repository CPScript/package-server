import os
import http.server
import socketserver
import threading
import time
import shutil

PORT = 8080  # You can change the port if needed
DIRECTORY = "package"  # Add file here when the server starts

if not os.path.exists(DIRECTORY):
    os.makedirs(DIRECTORY)
    print(f"Created directory: {DIRECTORY}")
else:
    print(f"Directory already exists, please add your package if not added already: {DIRECTORY}")

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        super().do_GET()
        if self.path.endswith('.zip'):
            print(f"File {self.path} has been downloaded. Cleaning up...")
            try:
                os.remove(os.path.join(DIRECTORY, self.path[1:]))  
                shutil.rmtree(DIRECTORY)  
                print(f"Deleted {self.path} and directory {DIRECTORY}.")
            except Exception as e:
                print(f"Error during cleanup: {e}")
            finally:
                self.server.shutdown()

def start_server():
    os.chdir(DIRECTORY)  
    Handler = CustomHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port {PORT} from directory: {DIRECTORY}")
        httpd.serve_forever()

server_thread = threading.Thread(target=start_server)
server_thread.start()

time.sleep(1)
server_thread.join()
