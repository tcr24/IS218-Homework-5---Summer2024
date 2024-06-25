import logging
import os
from dotenv import load_dotenv

from HomeworkFive.command import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand  # Absolute import
from plugin_loader import PluginLoader

load_dotenv()

ENVIRONMENT = os.getenv('ENVIRONMENT')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logger.info(f"Running in {ENVIRONMENT} environment")

def main():
    loader = PluginLoader()
    loader.load_plugins()
    # Additional main logic here

if __name__ == "__main__":
    main()

class Calculator:
    def __init__(self, plugins_dir='plugins'):
        self.plugin_loader = PluginLoader(plugins_dir)
        self.commands = {
            'menu': self.show_menu,
            'exit': self.exit
        }
        self.load_plugins()
        self.commands.update({
            'add': AddCommand(),
            'subtract': SubtractCommand(),
            'multiply': MultiplyCommand(),
            'divide': DivideCommand(),
        })

    def load_plugins(self):
        plugins = self.plugin_loader.load_plugins()
        self.commands.update(plugins)

    def show_menu(self):
        logger.info("Available commands:")
        for command in self.commands:
            logger.info(f"- {command}")

    def exit(self):
        logger.info("Exiting calculator. Goodbye!")
        sys.exit(0)

    def run(self):
        self.show_menu()
        while True:
            user_input = input("Enter command: ").strip().split()
            if not user_input:
                continue
            command_name = user_input[0].lower()
            args = user_input[1:]
            command = self.commands.get(command_name)
            if command:
                try:
                    if command_name in ['menu', 'exit']:
                        command()
                    else:
                        result = command.execute(*args)
                        logger.info(f"Result: {result}")
                except Exception as e:
                    logger.error(f"Error: {e}")
            else:
                logger.error(f"Unknown command: {command_name}")

if __name__ == '__main__':
    calculator = Calculator()
    calculator.run()
