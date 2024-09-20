import pyautogui
import time


typegame = input(
    f" artifacts = [1] " " Calyx = [2] " "Stagnat Shadown = [3] " "Echo of War = [5] ")


# QUANTIDADE DE RESINA 40 POR RODADA


resina = input("Valor da resina: ")


if typegame == '1':

    # Artifacts
    if resina == '40':
        # 1 roll
        print("iniciando")
        desafio = pyautogui.locateOnScreen('img\START.png', confidence=0.7)
        pyautogui.click(desafio)
        time.sleep(10)
        autorum = pyautogui.locateOnScreen('img\RUN.png', confidence=0.5)
        pyautogui.click(autorum)
        time.sleep(144)
        pyautogui.alert(text='Concluido', title='Autorail', button='OK')

    if resina == '80':
        # 2 roll
        print("Iniciando [1/2]")
        desafio = pyautogui.locateOnScreen('iniciodef.png', confidence=0.7)
        pyautogui.click(desafio)
        time.sleep(10)
        autorum = pyautogui.locateOnScreen('autorun8.png', confidence=0.5)
        pyautogui.click(autorum)
        time.sleep(144)
        print("Tentativa [2/2]")
        tentardnv = pyautogui.locateOnScreen(
            'tentardnv.png', confidence=0.5)
        pyautogui.click(tentardnv)
        time.sleep(145)
        print("Sem Resina")

    if resina == '120':
        # 3 roll
        print("iniciando [1/3]")
        desafio = pyautogui.locateOnScreen('iniciodef.png', confidence=0.7)
        pyautogui.click(desafio)
        time.sleep(10)
        autorum = pyautogui.locateOnScreen('autorun8.png', confidence=0.5)
        pyautogui.click(autorum)
        time.sleep(144)

        print("Tentativa [2/3]")
        tentardnv = pyautogui.locateOnScreen(
            'tentardnv.png', confidence=0.5)
        pyautogui.click(tentardnv)
        time.sleep(145)

        print("Tentativa [3/3]")
        pyautogui.click(tentardnv)
        time.sleep(145)
        print("Sucesso.")

    if resina == '180':
        # 4 g
        print("Iniciando [1/4]")
        desafio = pyautogui.locateOnScreen('iniciodef.png', confidence=0.7)
        pyautogui.click(desafio)
        time.sleep(10)
        autorum = pyautogui.locateOnScreen('autorun8.png', confidence=0.5)
        pyautogui.click(autorum)
        time.sleep(144)

        print("Tentativa [2/4]")
        tentardnv = pyautogui.locateOnScreen(
            'tentardnv.png', confidence=0.5)
        pyautogui.click(tentardnv)
        time.sleep(145)

        print("Tentativa [3/4]")
        pyautogui.click(tentardnv)
        time.sleep(145)

        print("Tentativa [4/4]")
        pyautogui.click(tentardnv)
        time.sleep(145)
        print("Sucesso.")

    if resina == '200':
        # 5 g
        print("Iniciando [1/5]")
        desafio = pyautogui.locateOnScreen('iniciodef.png', confidence=0.7)
        pyautogui.click(desafio)
        time.sleep(10)
        autorum = pyautogui.locateOnScreen('autorun8.png', confidence=0.5)
        pyautogui.click(autorum)
        time.sleep(144)

        print("Tenativa [2/5]")
        tentardnv = pyautogui.locateOnScreen(
            'tentardnv.png', confidence=0.5)
        pyautogui.click(tentardnv)
        time.sleep(145)

        print("Tentativa [3/5]")
        pyautogui.click(tentardnv)
        time.sleep(145)

        print("Tentativa [4/5]")
        pyautogui.click(tentardnv)
        time.sleep(145)

        print("Tentativa [5/5]")
        pyautogui.click(tentardnv)
        time.sleep(145)
        print("Sucesso.")

    if resina == '240':
        # 6 g
        print("iniciando [1/6]")
        desafio = pyautogui.locateOnScreen('iniciodef.png', confidence=0.7)
        pyautogui.click(desafio)
        time.sleep(8)
        autorum = pyautogui.locateOnScreen('autorun8.png', confidence=0.5)
        pyautogui.click(autorum)
        time.sleep(140)

        print("Tentativa [2/6]")
        tentardnv = pyautogui.locateOnScreen(
            'tentardnv.png', confidence=0.5)
        pyautogui.click(tentardnv)
        time.sleep(140)

        print("Tentativa [3/6]")
        pyautogui.click(tentardnv)
        time.sleep(140)

        print("Tentativa [4/6]")
        pyautogui.click(tentardnv)
        time.sleep(145)

        print("Tentativa [5/6]")
        pyautogui.click(tentardnv)
        time.sleep(145)

        print("Tentativa [6/6]")
        pyautogui.click(tentardnv)
        time.sleep(145)

        print("Sucesso")

    elif resina == '0':
        print("Sem Resina: Tente novamente mais tarde.")


if typegame == '2':
    # Calyix Golden
    iniciar = pyautogui.locateOnScreen('desafiar2.png', confidence=0.9)
    pyautogui.click(iniciar)
    time.sleep(5)

if typegame == '3':

    print('encerrando')
