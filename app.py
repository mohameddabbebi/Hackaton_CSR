from flask import Flask, render_template

# Initialiser Flask
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/speech')
def speech():
    return render_template('speech.html')

if __name__ == '__main__':
    app.run(debug=False)
