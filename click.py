import pyautogui
import time

arquivar = 0

while arquivar <= 2:

    # trocar de janela
    pyautogui.keyDown('alt')
    pyautogui.press(['tab'])
    pyautogui.keyUp('alt')

    # ir ate o card e arquivar
    pyautogui.moveTo(1333, 104)
    time.sleep(2)
    pyautogui.rightClick(1333, 104)
    time.sleep(2)
    # pegar imagem da palavra arquivar
    img = pyautogui.locateCenterOnScreen('teste.png')
    pyautogui.click(img.x, img.y)

    # troca de janela
    pyautogui.keyDown('alt')
    pyautogui.press(['tab'])
    pyautogui.keyUp('alt')
    time.sleep(2)

    arquivar = arquivar + 1

print('####################### ACABOU! #######################')