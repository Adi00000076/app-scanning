from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_app')
def run_app():
    # Path to the .exe file
    exe_path = "dist/app.exe"
    
    # Run the executable
    subprocess.Popen([exe_path])

    return "Application started!"

if __name__ == '__main__':
    app.run(debug=True)
