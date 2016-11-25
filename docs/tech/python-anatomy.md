# Python programming language

** TODO ** Use Mau Mau as to introduce the other tools and libraries

## Anatomy of a Python project

**TODO**

## Flask (Micro Web Framework)

For creating web applications.

Hello World in Flask:

    from flask import Flask
    app = Flask(__name__)
    
    @app.route("/")
    def hello():
        return "Hello World!"
    
    if __name__ == "__main__":
        app.run()

## TinyDB (simple Database)

For storing your 
