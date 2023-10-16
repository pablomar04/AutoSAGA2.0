import pyautogui
from datos import *


def completar_datos_principales(tipo, reclamo):
    
    #position = pyautogui.locateCenterOnScreen('img/cc.png', confidence=0.8)
    #pyautogui.click(position)
    #position = pyautogui.locateCenterOnScreen('img/numero.png', confidence=0.8)
    #pyautogui.click(position)
    #pyautogui.press('Tab')

    position = pyautogui.locateCenterOnScreen('img/n-reclamacion.png', confidence=0.8)
    pyautogui.click(position)
    
    pyautogui.write(reclamo["orden"])
    pyautogui.press('Tab')
    pyautogui.write(tipo)

    position = pyautogui.locateCenterOnScreen('img/bastidor.png', confidence=0.8)
    pyautogui.click(position)

    pyautogui.write(reclamo["chasis"], interval=0.05)

    position = pyautogui.locateCenterOnScreen('img/recepcion.png', confidence=0.8)
    pyautogui.click(position)

    pyautogui.write(reclamo["recepcion"])
    pyautogui.press('Tab', presses=2)
    pyautogui.write(reclamo["kilometraje"])

    position = pyautogui.locateCenterOnScreen('img/at.png', confidence=0.8)
    pyautogui.click(position)

    codigo = reclamo["codigo"]

    if tipo == 'S10':
        pyautogui.write(codigos_contratos[codigo][0])
    elif tipo == '11M':
        pyautogui.write(codigos_mo[codigo][0])
    pyautogui.press('Tab')
    pyautogui.write('0010')
    pyautogui.press('Tab')
    pyautogui.write(reclamo["reparacion"])

    position = pyautogui.locateCenterOnScreen('img/proveedor.png', confidence=0.8)
    pyautogui.click(position)

    pyautogui.write('9AR')
    
    position = pyautogui.locateCenterOnScreen('img/comentarios.png', confidence=0.8)
    pyautogui.click(position)
    
    if tipo == 'S10':
        pyautogui.write(codigos_contratos[codigo][2])
    elif tipo == '11M':
        pyautogui.write(codigos_mo[codigo][2])
