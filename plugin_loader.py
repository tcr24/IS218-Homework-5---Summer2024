import importlib
import os

class PluginLoader:
    def __init__(self, plugins_dir='plugins'):
        self.plugins_dir = plugins_dir

    def load_plugins(self):
        plugins = {}
        for filename in os.listdir(self.plugins_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = filename[:-3]
                module = importlib.import_module(f'{self.plugins_dir}.{module_name}')
                command_name = module_name.capitalize() + 'Command'
                command_class = getattr(module, command_name)
                plugins[module_name] = command_class()
        return plugins
