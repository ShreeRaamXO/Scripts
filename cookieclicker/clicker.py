import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, Key, KeyCode

mouse = Controller()

# Define keys
START_KEY = KeyCode(char='`')  # Press ` to start clicking
STOP_KEY = KeyCode(char='1')  # Press 1 to stop clicking and exit

is_clicking = False
is_running = True

def click_loop():
    global is_clicking
    while is_running:
        if is_clicking:
            mouse.click(Button.left, 1)
            time.sleep(0.1)  # Adjust click speed here

def on_press(key):
    global is_clicking, is_running
    if key == START_KEY:
        is_clicking = not is_clicking  # Toggle clicking
        print("Clicking:", "Started" if is_clicking else "Stopped")
    elif key == STOP_KEY:
        is_running = False
        return False  # Stop the listener

if __name__ == "__main__":
    print("Autoclicker running. Press ` to toggle clicking. Press 1 to exit.")
    with Listener(on_press=on_press) as listener:
        click_loop()
        listener.join()
