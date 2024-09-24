from flask import Flask, render_template, request
import math as mt 
import formulas as fm

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def calculadora():
    try:
        display = ""
        
        if request.method == 'POST':
            button = request.form.get('button')
            current_display = request.form.get('display', '')
        
            display = fm.identify_button(button,current_display,display)
        
        return render_template("main.html", display=display)
    except Exception as e:
        return "<h1>ERROR</h1>", e
    
@app.route("/Calculadora_Cientifica",  methods=['GET','POST'])
def Calculadora_Cientifica(): 
    try:
        display = ""
        
        if request.method == 'POST':
            button = request.form.get('button')
            current_display = request.form.get('display', '')  
            
            display = fm.identify_button(button,current_display,display)
            
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
            
            elif "mod()" in current_display:
                try:
                    numero = int(current_display.split("mod")[0])
                    divisor = int(current_display.split("mod(")[1])
                    display = fm.mod(numero,divisor)
                except:
                    display = ""
                    
             
        return render_template("Calculadora_Cientifica.html", display=display)
    except Exception as e:
        return "<h1>ERROR</h1>", e

@app.route('/Area', methods=['GET','POST'])
def page_area():
    return render_template('Khan_Academy/Area.html')

@app.route("/pitagoras", methods=['GET','POST'])
def page_pitagoras():
    return render_template("Khan_Academy/pitagoras.html")


if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    # else:
    #                 try:
    #                     numero = int(current_display)
    #                     divisor = int(current_display.split("mod")[1])
    #                     display = fm.mod(numero,divisor)
    #                 except:
    #                     display = ""