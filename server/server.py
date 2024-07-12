# server.py

import os
import subprocess

class Server:
    def __init__(self, name, ram, cpu, server_type):
        self.name = name
        self.ram = ram
        self.cpu = cpu
        self.server_type = server_type
        self.server_directory = f'/data/data/com.termux/files/home/{name}'

    def create(self):
        os.makedirs(self.server_directory, exist_ok=True)
        self.download_server_jar()
        self.generate_start_script()

    def download_server_jar(self):
        if self.server_type.lower() == 'paper':
            server_url = 'https://papermc.io/api/v2/projects/paper/versions/1.19.4/builds/274/downloads/paper-1.19.4-274.jar'
        elif self.server_type.lower() == 'spigot':
            server_url = 'https://download.getbukkit.org/spigot/spigot-1.19.4.jar'
        else:
            raise ValueError('Unknown server type. Choose "Paper" or "Spigot".')

        file_path = os.path.join(self.server_directory, 'server.jar')
        subprocess.run(['wget', '-O', file_path, server_url], check=True)

    def generate_start_script(self):
        start_script = f"""#!/bin/bash
cd {self.server_directory}
java -Xmx{self.ram}M -Xms{self.ram}M -jar server.jar nogui
"""
        with open(os.path.join(self.server_directory, 'start.sh'), 'w') as f:
            f.write(start_script)
        os.chmod(os.path.join(self.server_directory, 'start.sh'), 0o755)

    def start(self):
        subprocess.run([f'{self.server_directory}/start.sh'], shell=True, check=True)

    def restart(self):
        self.stop()
        self.start()

    def stop(self):
        subprocess.run(['pkill', '-f', f'{self.server_directory}/server.jar'], check=True)
