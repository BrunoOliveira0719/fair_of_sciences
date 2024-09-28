import formulas as fm

def identify_button(button,current_display, display):
    if button == "=":
        try:
            display = fm.calculator_basic(current_display)
        except Exception as e:
            display = ""
    elif button in ["del","CE"]:
        if button == "del":
            display = current_display[:-1]
        else:
            display = ""
    elif button == "%":
        try:
            if "+" in current_display:
                base, percentage_int = current_display.split("+")
                porcentagem = int(percentage_int.strip().rstrip("%"))
                numero = float(base.strip())
                

                display = str(numero + fm.percentage(numero,porcentagem))
        except:
            display = ''
    else:
        display = current_display + button
    return display
    

def identify_button_scientific(button,current_display, display):          
    if button in ["pi","raiz","fatorial"]:
        if button == "pi":
            display = current_display + fm.pi()
        elif button == "raiz":
            try:
                numero = int(current_display)
                display = fm.square_root(numero)
            except:
                display = ""
        else:
            try:
                numero = int(current_display)
                display = fm.factorial(numero)
            except: 
                display = ""
                        
    elif button in ["e","abs"]:
        if button == "e":
            display = fm.e()
        else:
            try:
                numero = int(current_display)
                display = fm.ABS(numero)
            except:
                display = ""
                        
    elif button in ["log","in"]:
        try:
            numero = int(current_display)
            if button == "in":
                display = fm.IN(numero)
            else:
                display = fm.log(numero)
        except:
            display = ""
                   
    elif button in ["sen","cos","tg"]:
        try:
            numero = float(current_display)
            if button == "sen":
                display = fm.sen(numero)
            elif button == "cos":
                display = fm.cos(numero)
            else:
                display = fm.tg(numero)
        except:
            display = ""
            
    elif "mod" in current_display:
        try:
            numero = int(current_display.split("mod")[0])
            divisor = identify_button_scientific(button,current_display, display)
            display = fm.mod(numero,divisor)
        except:
            display = ""
    return display
                    