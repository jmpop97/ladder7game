import keyboard  # using module keyboard
import os
while True:  # making a loop

    key = keyboard.read_key()
    if key:  # if key 'q' is pressed
        os.system('cls')
        print(key)
    # finishing the loop
