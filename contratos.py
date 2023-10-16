import pyautogui
from datos import *
from funciones import *

def reclamar_contrato (reclamo):
    
    completar_datos_principales('S10',reclamo)

    #CARGAR MANO DE OBRA
    position = pyautogui.locateCenterOnScreen('img/tercero.png', confidence=0.8)
    pyautogui.click(position)

    position = pyautogui.locateCenterOnScreen('img/e1.png', confidence=0.8)
    pyautogui.click(position)
    codigo = reclamo['codigo']
    pyautogui.write(codigos_contratos[codigo][1])
    pyautogui.press('enter')
    pyautogui.write(codigos_contratos[codigo][3])
    pyautogui.press('enter')
    #CARGAR MATERIAL
    position = pyautogui.locateCenterOnScreen('img/e2.png', confidence=0.8)
    pyautogui.click(position)

    pyautogui.write('MAT-OTROS')
    pyautogui.press('enter')
    pyautogui.write('MATERIALES')
    pyautogui.press('enter')
    pyautogui.write('1')
    pyautogui.press('enter', presses=2)
    pyautogui.press('down', presses=3)
    pyautogui.press('enter', presses=2)
    pyautogui.write(codigos_contratos[codigo][4])
    pyautogui.press('enter')
    #MARCAR CAUSAL
    position = pyautogui.locateCenterOnScreen('img/causal1.png', confidence=0.9)
    pyautogui.click(position)
    #COMPLETAR
    position = pyautogui.locateCenterOnScreen('img/completar.png', confidence=0.8)
    pyautogui.moveTo(position)
              


