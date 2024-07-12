from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from server.server_manager import ServerManager
import sys
print(sys.path)


# Load the kv file directly
Builder.load_file('elhost.kv')

class MainScreen(Screen):
    pass

class CreateServerScreen(Screen):
    def create_server(self):
        server_name = self.ids.server_name.text
        ram = self.ids.ram.text
        cpu = self.ids.cpu.text
        server_type = self.ids.server_type.text

        # Create the server
        server_manager = ServerManager()
        server_manager.create_server(server_name, ram, cpu, server_type)
        
        # Transition to server management screen
        self.manager.current = 'server_management'

class ServerManagementScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.server_manager = ServerManager()

    def start_server(self):
        self.server_manager.start_server()

    def restart_server(self):
        self.server_manager.restart_server()

    def stop_server(self):
        self.server_manager.stop_server()

class ELhostApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(CreateServerScreen(name='create_server'))
        sm.add_widget(ServerManagementScreen(name='server_management'))
        return sm

if __name__ == '__main__':
    ELhostApp().run()
