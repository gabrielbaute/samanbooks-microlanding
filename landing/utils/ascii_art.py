from pyfiglet import Figlet
from colorama import Fore, Style, init
from landing.config import Config

init(autoreset=True)  # Inicializa colorama para soporte de colores en Windows

class Banner:
    def __init__(self, name: str):
        self.name = name
        self.description = f"A simple microlanding app build with Flask"
        self.banner = self.get_banner()
        
    def _build_title(self, name: str) -> str:
        """Genera el título en arte ASCII usando pyfiglet."""
        figlet = Figlet(font="ansi_shadow", width=100, justify="center")
        ascii_art = figlet.renderText(name)
        return ascii_art

    def get_banner(self) -> str:
        """Devuelve el banner como una cadena de texto."""
        title = self._build_title(self.name)
        banner = f'''{Fore.LIGHTGREEN_EX}{Style.BRIGHT}\n{title}\n{self.description} [v{Config.APP_VERSION}]'''
        return banner
    
    def print_banner(self) -> None:
        """Imprime el banner en la consola."""
        banner = self.banner
        print(banner)
        