import math as mt 

def calculator_basic(expression):
    return str(eval(expression))

def infinite(num):
    return mt.isfinite(num)

def combination(k, n):
    return mt.comb(k, n)

def percentage(num, porcentagem = 1):
    return str((num*porcentagem)/100)

def pi():
    return str(mt.pi)

def e():
    return str(mt.e)

def ABS(num):
    return str(abs(num))

def mod(num1,num2):
    return str(mt.fmod(num1,num2))

def sen(num):
    return str(mt.sin(mt.radians(num)))

def cos(num):
    return str(mt.cos(mt.radians(num)))

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
    return str(mt.degrees(num))

def degrees_radians(num):
    return str(mt.radians(num))

#areas
def triangle_area(base, heigth):
    return str((base * heigth) / 2)

def rectangle_square_area(base, heigth):
    return str(base * heigth)

def trapezoid_area(b_base, heigth, B_base):
    return str(((b_base + B_base)*heigth)/ 2)
    
def circle_area(ray):
    return str(pi()*(ray**2))

def diamond_area(D_diagonal, d_diagonal):
    return str((D_diagonal * d_diagonal)/ 2)

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
            if "+" in current_display:
                base, percentage_int = current_display.split("+")
                porcentagem = int(percentage_int.strip().rstrip("%"))
                numero = float(base.strip())
                

                display = str(numero + percentage(numero,porcentagem))
                return display
        except:
            display = ''
            return display
        
    else:
        display = current_display + button
        return display