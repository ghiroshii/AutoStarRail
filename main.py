import pyautogui as pg
import time


typegame = int(input("Artifacts [1]: / Calyx [2]: /  "))
resin = int(input("Resin value: "))
timem = int(input("battle time: "))


def startgame():

    # Start
    desafio = pg.locateOnScreen('img/START.png', confidence=0.5)
    pg.click(desafio)

    # Click in AutoRun
    time.sleep(10)
    autorum = pg.locateOnScreen('img/RUN.png', confidence=0.5)
    pg.click(autorum)
    time.sleep(timem)


if typegame == 1:

    resin -= 40
    startgame()

    # TryAgain
    tentardnv = pg.locateOnScreen('img/TRYA.png', confidence=0.7)
    pg.click(tentardnv)

    while resin > 40:

        resin -= 40
        # Loop until the resin reaches 39
        time.sleep(timem)
        tentardnv = pg.locateOnScreen('img/TRYA.png', confidence=0.7)
        pg.click(tentardnv)
        print("Amount of resin remaining: ", resin)

    while resin < 40:
        print("end")

        break


if typegame == 2:

    resin -= 60
    startgame()

    # TryAgain
    tentardnv = pg.locateOnScreen('img/calyx.png', confidence=0.9)
    pg.click(tentardnv)

    while resin > 60:
        resin -= 60
        # Loop until the resin reaches 39
        time.sleep(timem)
        tentardnv = pg.locateOnScreen('img/calyx.png', confidence=0.9)
        pg.click(tentardnv)
        print("Amount of resin remaining: ", resin)

    while resin < 60:

        print("end")
        break

if typegame == 3:
    print("Soon")
