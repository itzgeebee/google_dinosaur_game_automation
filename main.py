# google dinosaur game automatation using pyautogui
import pyautogui  # pip install
import keyboard

pyautogui.FAILSAFE = False

while True:
    sc = pyautogui.screenshot()  # take a screenshot of the target screen
    screen = sc.getpixel((316, 157))  # get the pixel of the screen background

    # get the pixel of the obstacles
    tree1 = sc.getpixel((455, 224))
    tree2 = sc.getpixel((490, 224))
    tree3 = sc.getpixel((545, 224))
    tree4 = sc.getpixel((445, 230))

    # bird1 = sc.getpixel((481, 191))
    # bird2 = sc.getpixel((500, 189))
    # bird3 = sc.getpixel((510, 188))
    # bird4 = sc.getpixel((520, 172))

    # jump
    if tree1[0] != screen[0] or tree2[0] != screen[0] or tree3[0] != screen[0] or tree4[0] != screen[0]:
        pyautogui.press('space')

    if keyboard.is_pressed('q'):
        break
