from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agentur')
def agentur():
    return redirect('http://agentur.ermine.at')

@app.route('/songlooping')
def songlooping():
    return redirect('http://songlooping.ermine.at')

@app.route('/soundscapes')
def soundscapes():
    return redirect('http://soundscapes.ermine.at')

@app.route('/3dprintwien')
def d3printwien():
    return redirect('http://3dprintwien.ermine.at')

if __name__ == '__main__':
    app.run(debug=True)
