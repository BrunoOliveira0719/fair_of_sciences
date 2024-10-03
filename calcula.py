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
        operacoes = ["-", "+", "*", "/"]
        try:
            for i in operacoes:
                if i in current_display:
                    num_list = current_display.split(i)
                    number = float(num_list[0]) 
                    por = float(num_list[1]) 
                    
                    
                    if i == "-":
                        display = str(number - (number * por / 100))
                    elif i == "+":
                        display = str(number + (number * por / 100))
                    elif i == "*":
                        display = str(number * (por / 100))
                    elif i == "/":
                        display = str(number / (por / 100))
                    
                    break
            else:
                display = fm.percentage(float(current_display))
        except Exception as e:
            display = ''
    else:
        display = current_display + button
    return display
    

def identify_button_scientific(button,current_display, display):   
    
    display = identify_button(button,current_display,display)
           
    if button in ["pi","raiz","fatorial"]:
        if button == "pi":
            display = current_display + fm.pi()
        elif button == "raiz":
            try:
                number = int(current_display)
                display = fm.square_root(number)
            except:
                display = ""
        else:
            try:
                number = int(current_display)
                display = fm.factorial(number)
            except:
                display = ""
                        
    elif button in ["e","abs"]:
        if button == "e":
            display = fm.e()
        else:
            try:
                number = int(current_display)
                display = fm.ABS(number)
            except:
                display = ""
                        
    elif button in ["log","in"]:
        try:
            number = int(current_display)
            if button == "in":
                display = fm.IN(number)
            else:
                display = fm.log(number)
        except:
            display = ""
                   
    elif button in ["sen","cos","tg"]:
        try:
            number = float(current_display)
            if button == "sen":
                display = fm.sen(number)
            elif button == "cos":
                display = fm.cos(number)
            else:
                display = fm.tg(number)
        except:
            display = ""
            
    return display

def identify_function_pitagoras(cateto_A, cateto_B, hipotenusa):
    try:
        msg_error = 'Preencha os dois campos'
        if not hipotenusa:
            if cateto_A and cateto_B:
                display = fm.find_hipotenusa(float(cateto_A), float(cateto_B))
            else:
                display = msg_error
            
        elif not cateto_A:
            if hipotenusa and cateto_B:
                display = fm.find_cateto_A(float(hipotenusa), float(cateto_B))
            else:
                display = msg_error
            
        elif not cateto_B:
            if hipotenusa and cateto_A:
                display = fm.find_cateto_B(float(hipotenusa), float(cateto_A))
            else:
                display = msg_error
             
    except Exception as e:
        display = ''
    return display