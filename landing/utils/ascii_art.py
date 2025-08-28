from pyfiglet import Figlet
from landing.config import Config

def build_title(name: str) -> str:
    figlet = Figlet(font="ansi_shadow", width=100, justify="center")
    ascii_art = figlet.renderText(name)
    return ascii_art

def get_banner(name: str) -> str:
    title = build_title(name)
    banner = f'''
\n
{title}
A simple microlanding app build with Flask.
v{Config.APP_VERSION}
    '''
    return banner