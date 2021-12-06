import sys
from userInterface import UserInterface


ui = UserInterface(sys.argv)

ui.initialize()
ui.run()