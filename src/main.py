from flask import Flask

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/gppartner/v1/api', methods=['GET', 'POST'])
def api():
    return "<b>dalva</b>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)