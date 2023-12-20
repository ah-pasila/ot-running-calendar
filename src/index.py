"""index.py is used to start the Running calendar service
"""

from ui.ui import UI


def main():
    """main creates instance of user interface and executes the app
    """
    userinterface = UI()
    userinterface.execute_app()


if __name__ == "__main__":
    main()
