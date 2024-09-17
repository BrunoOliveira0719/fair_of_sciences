import math as mt 

def calculator_basic(expression):
    return str(eval(expression))

def infinite(num):
    return mt.isfinite(num)

def combination(k, n):
    return mt.comb(k, n)

def percentage(num):
    return str(num/100)

def pi():
    return str(mt.pi)

def sen(num):
    return str(mt.sin(mt.radians(num)))

def cos(num):
    return str(mt.cos(num))

def tg(num):
    return str(mt.tan(mt.radians(num)))

def square_root(num):
    return str(mt.sqrt(num))

def log(num):
    return str(mt.log10(num))

def IN(num):
    return str(mt.log(num))

def factorial(num):
    return str(mt.factorial(num))

def radians_degrees(num):
    return mt.degrees(num)

def degrees_radians(num):
    return mt.radians(num)

def triangle_area(base, heigth):
    return base * heigth / 2

def rectangle_area(base, heigth):
    return base * heigth

#financial sector
def ROI(revenue, expenses):
    return (revenue - expenses) / expenses

#phamaceutical sector
def dose_medication(weigth):
    return weigth * 2


def identify_button(button,current_display, display):
    if button == "=":
        try:
            display = calculator_basic(current_display)
            return display
        except Exception as e:
            display = ""
            return display
    elif button in ["del","CE"]:
        if button == "del":
            display = current_display[:-1]
            return display
        else:
            display = ""
            return display
    elif button == "%":
        try:
            numero = int(current_display)
            display = percentage(numero)
            return display
        except:
            display = ''
            return display
        
    else:
        display = current_display + button
        return display