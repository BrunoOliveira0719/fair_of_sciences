from flask import Flask, render_template, request
import math as mt 
import formulas as fm

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculadora():
    display = ""
    
    if request.method == 'POST':
        button = request.form.get('button')
        current_display = request.form.get('display', '')

        if button == "=":
            try:
                display = str(eval(current_display))
            except Exception as e:
                display = ""
        elif button == "del":
            display = current_display[:-1]
        elif button == "pi":
            display = current_display + fm.pi()
        else:
            display = current_display + button

    return render_template("main.html", display=display)

if __name__ == "__main__":
    app.run(debug=True)