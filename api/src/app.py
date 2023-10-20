from flask import Flask, render_template

app = Flask(__name__, template_folder='../views', static_folder='../views/public')

@app.route('/hello_world/')
def hello_world():
    return render_template('index.html')

@app.route('/test/')
def hello_world2():
    return {
        'message': 'Hello, World!'
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
