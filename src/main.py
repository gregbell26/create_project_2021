import sys
from src.userInterface import UserInterface


ui = UserInterface(sys.argv)

ui.initialize()
exit(ui.run())
