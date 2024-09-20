import time
import pyautogui as pg

quantidade = int(input("Quantidade de comandas: "))


while quantidade > 0:

    # ENTRADA NA COMANDA
    comanda = pg.locateOnScreen('imgf/PRIMEIRO.png', confidence=0.3)
    pg.doubleClick(comanda)
    time.sleep(4)

    # TELA DE CONFERENCIA 1/2 LOG
    log = pg.locateOnScreen('imgf/SEGUNDO.png', confidence=0.5)
    pg.click(log)
    time.sleep(4)

    # TELA DE CONFERENCIA 2/2 X

    fechar = pg.locateOnScreen('imgf/TERCE.png', confidence=0.5)
    pg.click(fechar)
    time.sleep(4)

    # SCROLL
    pg.moveTo(comanda)
    pg.scroll(-10)
    time.sleep(3)

    quantidade -= 1
    print("Quantidade restante: ", quantidade)


while quantidade < 50:
    print("acabei")

    break


# deve apertar em cada comanda e enviar o log apertando no botao1 depois botao2 e crollar a pagina
# cada pagina tem 50 então o programa deve virar a pagina
