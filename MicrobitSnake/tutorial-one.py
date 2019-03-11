from microbit import *

# Displaying a Happy image for a second then sad and
# then clear the display with a second gap in between

display.show(Image.HAPPY)
sleep(1000)
display.show(Image.SAD)
sleep(1000)
display.clear()