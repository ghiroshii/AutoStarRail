import pyautogui as og
import time


typegame = int(input("Artefatos [1]: / Calice [2]: /  "))
resina = int(input("Valor da resina: "))
timem = int(input("Digite o tempo medio: "))


if typegame == 1:

    # Start
    desafio = og.locateOnScreen('img/START.png', confidence=0.5)
    og.click(desafio)
    resina -= 40

    # Click in AutoRun
    time.sleep(10)
    autorum = og.locateOnScreen('img/RUN.png', confidence=0.5)
    og.click(autorum)
    time.sleep(timem)

    # TryAgain
    tentardnv = og.locateOnScreen('img/TRYA.png', confidence=0.7)
    og.click(tentardnv)

    while resina > 39:
        # Loop until the resin reaches 39
        time.sleep(timem)
        tentardnv = og.locateOnScreen('img/TRYA.png', confidence=0.7)
        og.click(tentardnv)
        resina -= 40
        print("Amount of resin remaining: ", resina)

    while resina < 40:
        print("a")

        break


if typegame == 2:

    # Start
    desafio = og.locateOnScreen('img/START.png', confidence=0.5)
    og.click(desafio)
    resina -= 60

   # Click in AutoRun
    time.sleep(10)
    autorum = og.locateOnScreen('img/RUN.png', confidence=0.5)
    og.click(autorum)
    time.sleep(timem)

    # TryAgain
    tentardnv = og.locateOnScreen('img/calyx.png', confidence=0.7)
    og.click(tentardnv)

    while resina > 59:
        # Loop until the resin reaches 39
        time.sleep(timem)
        tentardnv = og.locateOnScreen('img/calyx.png', confidence=0.7)
        og.click(tentardnv)
        resina -= 60
        print("Amount of resin remaining: ", resina)

    while resina < 60:
        print("FIM")
        break

if typegame == 3:
    print("em construção")
