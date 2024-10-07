from flask import Flask, render_template, request
import calcula as cl
import formulas as fm

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
            
            button = request.form.get('button')
            
            if button == "quadrado":
                quadrado = request.form.get("side")
                display = fm.square_area(float(quadrado))
                
            elif button == "circulo":
                circulo = request.form.get("radius")
                display = fm.circle_area(float(circulo))
                
            elif button == "triangulo":
                base_triangle = request.form.get("base_triangle")
                heigth_triangle = request.form.get("heigth_triangle")
                triangulo = [base_triangle, heigth_triangle]
                if triangulo[0] and triangulo[1]:
                    display = fm.triangle_area(float(triangulo[0]),float(triangulo[1]))
                else:
                    display = ""
                    
            elif button == "trapezio":
                base_trapezoid = request.form.get("base_trapezoid") 
                heigth_trapezoid = request.form.get("heigth_trapezoid") 
                Base_trapezoid = request.form.get("Base_trapezoid") 
                trapezio = [base_trapezoid, heigth_trapezoid, Base_trapezoid]
                if trapezio[0] and trapezio[1] and trapezio[2]:
                    display = fm.trapezoid_area(float(trapezio[0]), float(trapezio[1]),float(trapezio[2]))
                else:
                    display = ""
                    
            elif button == "retangulo":
                base_rectangle = request.form.get("base_rectangle")
                heigth_rectangle = request.form.get("heigth_rectangle")
                retangulo = [base_rectangle, heigth_rectangle]
                if retangulo[0] and retangulo[1]:
                    display = fm.rectangle_square_area(float(retangulo[0]),float(retangulo[1]))
                else:
                    display = ""
                    
            elif button == "losango":
                width_diamond = request.form.get("width_diamond")
                heigth_diamond = request.form.get("heigth_diamond")
                losango = [width_diamond,heigth_diamond]
                if losango[0] and losango[1]:
                    display = fm.diamond_area(float(losango[0]),float(losango[1]))
                else:
                    display = ""
            else:
                display = ""  
                
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