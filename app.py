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
        return f"<h1>ERROR</h1> {e}"
    
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
        return f"<h1>ERROR</h1> {e}"

@app.route('/Area', methods=['GET','POST'])
def page_area():
    try:
        display = ""
        
        if request.method == 'POST':
            quadrado = request.form.get("side")
            circulo = request.form.get("radius")
            base_triangle = request.form.get("base_triangle")
            heigth_triangle = request.form.get("heigth_triangle")
            triangulo = [base_triangle, heigth_triangle]
            
            trapezio = []
            base_rectangle = request.form.get("base_rectangle")
            heigth_rectangle = request.form.get("heigth_rectangle")
            retangulo = [base_rectangle, heigth_rectangle]
            width_diamond = request.form.get("width_diamond")
            heigth_diamond = request.form.get("heigth_diamond")
            Losango = [width_diamond,heigth_diamond]
            
            cl.identify_function_area(quadrado,circulo,triangulo,trapezio,retangulo,Losango)
        
        return render_template('Khan_Academy/Area.html', display=display)
    
    except Exception as e:
        return f"<h1>ERROR</h1> {e}"
    

@app.route("/pitagoras", methods=['GET','POST'])
def page_pitagoras():
    try:
        display = ""
        
        if request.method == 'POST':
            cateto_A = request.form.get('catetoA', '').strip()
            cateto_B = request.form.get('catetoB', '').strip()
            hipotenusa = request.form.get('hipotenusa', '').strip()

            display = cl.identify_function_pitagoras(cateto_A, cateto_B, hipotenusa)

        return render_template("Khan_Academy/pitagoras.html", display=display)
    
    except Exception as e:
        return f"<h1>ERROR</h1> {e}"
    
@app.route("/formulas", methods=['GET','POST'])
def page_formulas():
    display = ""
    return render_template("Khan_Academy/formulas.html", display=display)


if __name__ == "__main__":
    app.run(debug=True)