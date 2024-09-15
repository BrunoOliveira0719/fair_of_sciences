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

            if button == "=":
                try:
                    display = fm.calculator_basic(current_display)
                except Exception as e:
                    display = ""
            elif button == '...':
                pass
            elif button in ["del","CE"]:
                if button == "del":
                    display = current_display[:-1]
                else:
                    display = ""
            elif button in ["pi","raiz","fatorial"]:
                if button == "pi":
                    display = current_display + fm.pi()
                elif button == "raiz":
                    try:
                        numero = int(current_display)
                        display = fm.raiz(numero)
                    except:
                        display = ""
                else:
                    try:
                        numero = int(current_display)
                        display = fm.factorial(numero)
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
            else:
                display = current_display + button

        return render_template("main.html", display=display)
    except Exception as e:
        return "<h1>ERROR</h1>", e

if __name__ == "__main__":
    app.run(debug=True)