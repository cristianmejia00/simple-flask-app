from flask import Flask
import platform

app = Flask(__name__)

print('''
#####################
Running flask app!
#####################
''')

@app.route("/")
def hello_world():
    machine = platform.machine()
    version = platform.version()
    plat = platform.platform()

    return f'''<p>Machine: {machine}<br>
            Version: {version}<br>
            Platform: {plat}</p>'''

@app.route("/ok")
def health():
    return "<p>OK</p>"

if __name__ == "__main__":
    print('''
    =================
    main
    =================
    ''')
    app.run(debug = True, host='0.0.0.0', port=5000)
