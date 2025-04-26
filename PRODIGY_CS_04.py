from pynput.keyboard import Key, Listener
def on_press(key):
    try:
        print(f'Key {key.char} pressed')
    except AttributeError:
        print(f'Special key {key} pressed')
def on_release(key):
    print(f'Key {key} released')
    if key == Key.esc:
        # Stop listener
        return False
# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join() 
# This code uses the pynput library to listen for keyboard events. It prints the key pressed and released, and stops listening when the escape key is pressed.
# The Listener class is used to create a listener that runs in the background and captures keyboard events. The on_press and on_release functions are called when a key is pressed or released, respectively. The listener is started with the with statement, which ensures that it is properly cleaned up when finished.
# The listener will run until the escape key is pressed, at which point it will stop and exit the program.
# This code can be useful for creating keyboard shortcuts, logging key presses, or creating a custom keyboard input system. It is important to note that using this code to capture keystrokes without the user's consent may violate privacy laws and ethical guidelines.
# It is recommended to use this code responsibly and only for legitimate purposes.
