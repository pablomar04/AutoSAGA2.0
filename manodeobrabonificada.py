import pyautogui
from datos import *
from funciones import *

def reclamar_manodeobra (reclamo):
    completar_datos_principales('11M', reclamo)
    #CARGAR MANO DE OBRA
    position = pyautogui.locateCenterOnScreen('img/tercero.png', confidence=0.8)
    pyautogui.click(position)

    position = pyautogui.locateCenterOnScreen('img/e1.png', confidence=0.8)
    pyautogui.click(position)
    codigo = reclamo['codigo']
    pyautogui.write(codigos_mo[codigo][1])
    pyautogui.press('enter')
    pyautogui.write(codigos_mo[codigo][3])
    pyautogui.press('enter')

    #MARCAR CAUSAL
    position = pyautogui.locateCenterOnScreen('img/causal2.png', confidence=0.9)
    pyautogui.click(position)
    #COMPLETAR
    position = pyautogui.locateCenterOnScreen('img/completar.png', confidence=0.8)
    pyautogui.moveTo(position)


