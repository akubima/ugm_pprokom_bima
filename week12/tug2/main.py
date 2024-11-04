from interface.menu import menu
try:
    menu()
except KeyboardInterrupt:
    print('Keyboard Interrupted')
    exit()
except Exception as e:
    print('Error:', e)
    exit()