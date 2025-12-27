from nicegui import ui

ui.button('Hello NiceGUI').on('click', lambda: print('Button clicked!'))

ui.run()