from flask import Flask, render_template, request
import calcula as cl

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def calculadora():
    try:
        display = ""
        
        if request.method == 'POST':
            button = request.form.get('button')
            current_display = request.form.get('display', '')
        
            display = cl.identify_button(button,current_display,display)
        
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
            
            display = cl.identify_button_scientific(button,current_display,display)
            
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