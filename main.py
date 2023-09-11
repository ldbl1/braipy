from pynput import keyboard 


#
# 1 S | 4 L
# 2 D | 5 K
# 3 F | 6 J
#
#

pressed = {}
global releasing 
releasing = False

def on_press(key): 
    global releasing 
    releasing = True
    if key not in pressed: # Key was never pressed before
        pressed[key] = False
    
    if not pressed[key]: # Same logic
        pressed[key] = True
        #print('Key %s pressed' % key) 

def on_release(key):  # Same logic
    global releasing
    if releasing:
        releasing = False
        get_letra_desde_braille(pressed)

    pressed.pop(key)
    #print('Key %s released' %key) 

def get_letra_desde_braille(dict):
    lista = []
    for element in dict.keys():
        lista.append(element.char)
    #TODO mejorar esta puta mierda de if else
    if 's' in lista and 'd' in lista and 'f' in lista:
            print("l")
            releasing = False
    
    elif 's' in lista and 'd' in lista:
            print("b")
            releasing = False

    elif 's' in lista:
        
        print("a")
        releasing = False

with keyboard.Listener( on_press=on_press, on_release=on_release) as listener: 
    listener.join()
