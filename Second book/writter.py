import content
import keyboard
import mouse
import time

keyboard.wait("f5")
for each in content.giveContent():
    time.sleep(0.1)
    keyboard.write(each[1:])
    time.sleep(0.2)
    mouse.click("left")
