from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('inicio.html')
@app.route('/Hombres')
def Hombres():
    return render_template('Hombres.html')

@app.route('/Mujeres')
def Mujeres():
    return render_template('Mujeres.html')
if __name__ == '__main__':
    app.run(debug=True)