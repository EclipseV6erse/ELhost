# server_manager.py

from server import Server
import server; print(dir(server))
import sys; print(sys.path)

class ServerManager:
    def __init__(self):
        self.server = None

    def create_server(self, name, ram, cpu, server_type):
        self.server = Server(name, ram, cpu, server_type)
        self.server.create()

    def start_server(self):
        if self.server:
            self.server.start()

    def restart_server(self):
        if self.server:
            self.server.restart()

    def stop_server(self):
        if self.server:
            self.server.stop()
