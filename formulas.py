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

#pitagoras
def find_hipotenusa(cateto_a, cateto_b):
    return mt.sqrt(cateto_a**2 + cateto_b**2)

def find_cateto_A(hipotenusa, cateto_b):
    if hipotenusa <= cateto_b:
        raise ValueError("A hipotenusa deve ser maior que o cateto B.")
    return mt.sqrt(hipotenusa**2 - cateto_b**2)

def find_cateto_B(hipotenusa, cateto_a):
    if hipotenusa <= cateto_a:
        raise ValueError("A hipotenusa deve ser maior que o cateto A.")
    return mt.sqrt(hipotenusa**2 - cateto_a**2)

#areas
def square_area(lado):
    return str(lado*lado)

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

#sector
def primeiro_grau(a,b,display):
    x = (-1*b)/(-1*a)
    display = x
    return display

def segundo_grau(a,b,c,display):
    delta = b**2 - 4*a*c
    
    raiz = ((-1*b) + mt.sqrt(delta))/2*a
    raiz2 = ((-1*b) - mt.sqrt(delta))/2*a
    
    if delta == 0:
        display = f"x1,x2 = {raiz}"
    elif delta > 0:
        display = f"x1 = {raiz} e x2 = {raiz2}"
    elif delta < 0:
        display = "não tem raiz real"
    
    return display

def pa(a1,n,r,display):
    an = a1 + ((n-1)*r)
    display = an
    return display

def pg(a1,n,q,display):
    an = a1 * (q ** n-1)
    display = an
    return display
