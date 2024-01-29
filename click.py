from pynput.mouse import Button, Controller
import time

"""
This script moves and clicks the mouse periodically to prevent the computer from going to sleep, or your Colab runtime from disconnecting.
"""

mouse = Controller()

while True:
    mouse.move(5, 0)
    mouse.click(Button.left, 1)
    time.sleep(6)
    mouse.move(-5, 0)
    mouse.click(Button.left, 1)
    time.sleep(6)

