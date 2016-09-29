from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

def run_devserver():
    # log.info("serving on http://localhost:%s", 5000)
    app.run(port=5000)

if __name__ == '__main__':
    run_devserver()
