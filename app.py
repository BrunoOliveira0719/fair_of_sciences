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
            current_display = request.form.get('display', '').replace(",",".")
        
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
            current_display = request.form.get('display', '').replace(",",".")
            
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
                quadrado = request.form.get("side").replace(",",".")
                if quadrado:
                    display = fm.square_area(float(quadrado))
                else:
                    display = ""
                
            elif button == "circulo":
                circulo = request.form.get("radius").replace(",",".")
                if circulo:
                    display = fm.circle_area(float(circulo))
                else:
                    display = ""
                
            elif button == "triangulo":
                base_triangle = request.form.get("base_triangle").replace(",",".")
                heigth_triangle = request.form.get("heigth_triangle").replace(",",".")
                triangulo = [base_triangle, heigth_triangle]
                if triangulo[0] and triangulo[1]:
                    display = fm.triangle_area(float(triangulo[0]),float(triangulo[1]))
                else:
                    display = ""
                    
            elif button == "trapezio":
                base_trapezoid = request.form.get("base_trapezoid").replace(",",".")
                heigth_trapezoid = request.form.get("heigth_trapezoid").replace(",",".")
                Base_trapezoid = request.form.get("Base_trapezoid").replace(",",".")
                trapezio = [base_trapezoid, heigth_trapezoid, Base_trapezoid]
                if trapezio[0] and trapezio[1] and trapezio[2]:
                    display = fm.trapezoid_area(float(trapezio[0]), float(trapezio[1]),float(trapezio[2]))
                else:
                    display = ""
                    
            elif button == "retangulo":
                base_rectangle = request.form.get("base_rectangle").replace(",",".")
                heigth_rectangle = request.form.get("heigth_rectangle").replace(",",".")
                retangulo = [base_rectangle, heigth_rectangle]
                if retangulo[0] and retangulo[1]:
                    display = fm.rectangle_square_area(float(retangulo[0]),float(retangulo[1]))
                else:
                    display = ""
                    
            elif button == "losango":
                width_diamond = request.form.get("width_diamond").replace(",",".")
                heigth_diamond = request.form.get("heigth_diamond").replace(",",".")
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
            cateto_A = request.form.get('catetoA', '').strip().replace(",",".")
            cateto_B = request.form.get('catetoB', '').strip().replace(",",".")
            hipotenusa = request.form.get('hipotenusa', '').strip().replace(",",".")

            display = cl.identify_function_pitagoras(cateto_A, cateto_B, hipotenusa)

        return render_template("Khan_Academy/pitagoras.html", display=display)
    
    except Exception as e:
        return f"<h1>ERROR</h1> {e}"
    
@app.route("/formulas", methods=['GET','POST'])
def page_formulas():
    display = ""
    return render_template("Khan_Academy/formulas.html", display=display)

@app.route('/circle', methods=['GET', 'POST'])
def page_circle():
    try:
        display = ''

        if request.method == 'POST':        
            button = request.form.get('button')
        
            if button == 'circle':
                radius = request.form.get('radius').replace(",",".")
                if radius:
                    display = fm.circle_area(float(radius))
                else:
                    display = ''

            elif button == 'circle_circumference':
                circumference = request.form.get('circumference').replace(",",".")
                if circumference:
                    display = fm.find_radius(float(circumference))
                else:
                    display = ''
                    
            elif button == 'circle_diameter':
                diameter = request.form.get('diameter').replace(',','.')
                if diameter:
                    display = fm.circle_area_diameter(float(diameter))
                else:
                    display = ''
            elif button == 'radius_circumference':
                radius_circumference = request.form.get('radius_circumference').replace(",",".")
                if radius_circumference:
                    display = fm.find_circumference_radius(float(radius_circumference))
                else:
                    display = ''
                    
            elif button == 'diameter_circumference':
                diameter_circumference = request.form.get('diameter_circumference').replace(',','.')
                if diameter_circumference:
                    display = fm.find_circumference_diameter(float(diameter_circumference))
                else:
                    display = ''
           
    except Exception as e:
        return f"<h1>ERROR</h1> {e}"
                        
    return render_template('Khan_Academy/circle.html', display=display)

if __name__ == "__main__":
    app.run(debug=True)