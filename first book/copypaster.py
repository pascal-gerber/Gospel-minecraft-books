import keyboard
import mouse
import time
import content

bibletext = content.giveout()
number = 0
skip = 0
limitnumb = 101
skipnumb = 0

block = chr(9632)
pages = bibletext.split("$")

keyboard.wait("f5")
for each in pages:
    skip += 1
    if skip < skipnumb:
        continue
    if number == limitnumb:
        keyboard.wait("f5")
        number = 0
    number += 1
    time.sleep(0.1)
    keyboard.write(each[1:])
    time.sleep(0.2)
    mouse.click("left")
