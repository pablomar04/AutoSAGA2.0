import pyautogui
import re
import time

def existeCodigo(codigo, coleccion):    
    for codes in coleccion:
        if codes['codigo'] == codigo:
            return True
    return False

def cargarCabecera(orden, chasis, recepcion, kilometraje, reparacion, codigo, data):
    
    cabecera = None    
    if data is not None:
        cabecera = data [0]
    #position = pyautogui.locateCenterOnScreen('img/cc.png', confidence=0.8)
    #pyautogui.click(position)
    #pyautogui.press('down')
    #pyautogui.press('enter')
    #pyautogui.press('tab')

    position = pyautogui.locateCenterOnScreen('img/n-reclamacion.png', confidence=0.8)
    pyautogui.click(position)    
    pyautogui.write(orden, interval=0.05)
    pyautogui.press('tab')
    pyautogui.write(cabecera['cabecera']['tipo'], interval=0.05)
    
    position = pyautogui.locateCenterOnScreen('img/bastidor.png', confidence=0.8)
    pyautogui.click(position)
    pyautogui.write(chasis, interval=0.05)

    position = pyautogui.locateCenterOnScreen('img/recepcion.png', confidence=0.8)
    pyautogui.click(position)
    pyautogui.write(recepcion, interval=0.05)

    pyautogui.press('tab', presses=2,interval=0.05)
    pyautogui.write(kilometraje, interval=0.05)

    position = pyautogui.locateCenterOnScreen('img/at.png', confidence=0.8)
    pyautogui.click(position)
    pyautogui.write(cabecera['cabecera']['at'], interval=0.05)

    pyautogui.press('tab')
    pyautogui.write(cabecera['cabecera']['defecto'], interval=0.05)

    if (cabecera['cabecera']['ubicacion']!= ''):
        pyautogui.write(cabecera['cabecera']['ubicacion'], interval=0.05)
    else:
        pyautogui.press('tab')
    pyautogui.write(reparacion, interval=0.05)
    #if Inmovilizado / TPI
    #if criterios
    if (cabecera['cabecera']['criterio']!= ''):
        cadena = cabecera['cabecera']['criterio']
        criterios = re.split('\s', cadena)

        position = pyautogui.locateCenterOnScreen('img/criterio.png', confidence=0.8)
        
        for cr in criterios:
            pyautogui.click(position)
            pyautogui.write(cr, interval=0.05)
            time.sleep(1)
            pyautogui.press('enter')
       

    position = pyautogui.locateCenterOnScreen('img/proveedor.png', confidence=0.8)
    pyautogui.click(position)
    pyautogui.write(cabecera['cabecera']['proveedor'], interval=0.05)

    position = pyautogui.locateCenterOnScreen('img/comentarios.png', confidence=0.8)
    pyautogui.click(position)
    pyautogui.write(cabecera['cabecera']['comentarios'], interval=0.03)

def cargarLocal(data):
    
    objeto = None

    if data is not None:
        objeto = data [1]
    
    if "local" in objeto:
        
        position = pyautogui.locateCenterOnScreen('img/local.png', confidence=0.8)
        pyautogui.click(position)

        if "mo" in objeto['local']:
            for op in objeto['local']['mo']:
                position = pyautogui.locateCenterOnScreen('img/entrada1.png', confidence=0.8)
                pyautogui.click(position)

                if op['causal'] == 1:
                    position = pyautogui.locateCenterOnScreen('img/causal-local.png', confidence=0.8)
                    pyautogui.click(position)

                pyautogui.write(op['operacion'], interval=0.05)
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.write(op['ut'], interval=0.05)
                pyautogui.press('enter')
        
        if "material" in objeto['local']:
            for pieza in objeto['local']['material']:
                position = pyautogui.locateCenterOnScreen('img/entrada2.png', confidence=0.9)
                pyautogui.click(position)

                if pieza['causal'] == 1:
                    position = pyautogui.locateCenterOnScreen('img/causal-local.png', confidence=0.8)
                    pyautogui.click(position)

                pyautogui.write(pieza['codigo'], interval=0.05)
                pyautogui.press('tab')
                pyautogui.write(pieza['cantidad'], interval=0.05)
                pyautogui.press('enter')



def cargarTercero(data):
    
    objeto = None

    if data is not None:
        if len (data) == 3:
            objeto = data[2]
        elif len (data) == 2:
            objeto = data[1]

    if "tercero" in objeto:
        
        position = pyautogui.locateCenterOnScreen('img/tercero.png', confidence=0.8)
        pyautogui.click(position)

        if "emo" in objeto['tercero']:
            for op in objeto['tercero']['emo']:
                position = pyautogui.locateCenterOnScreen('img/entrada3.png', confidence=0.7)
                pyautogui.click(position)

                if op['causal'] == 1:
                    position = pyautogui.locateCenterOnScreen('img/causal-local.png', confidence=0.8)
                    pyautogui.click(position)

                pyautogui.write(op['operacion'], interval=0.05)
                pyautogui.press('enter', interval=0.05)
                pyautogui.write(op['importe'], interval=0.05)
                pyautogui.press('enter')
        
        if "ematerial" in objeto['tercero']:
            for pieza in objeto['tercero']['ematerial']:
                position = pyautogui.locateCenterOnScreen('img/entrada4.png', confidence=0.9)
                pyautogui.click(position)

                if pieza['causal'] == 1:
                    position = pyautogui.locateCenterOnScreen('img/causal-local.png', confidence=0.8)
                    pyautogui.click(position)

                pyautogui.write(pieza['codigo'], interval=0.05)
                pyautogui.press('tab')
                pyautogui.write(pieza['comentario'], interval=0.05)
                pyautogui.press('tab')
                pyautogui.write(pieza['cantidad'], interval=0.05)
                pyautogui.press('enter', presses=2)
                pyautogui.press('down', presses=3)
                pyautogui.press('enter', presses=2)
                pyautogui.write(pieza['importe'], interval=0.05)
                pyautogui.press('enter')

