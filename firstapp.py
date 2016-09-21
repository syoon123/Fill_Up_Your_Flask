from flask import Flask
app = Flask(__name__)

@app.route('/')
def catinthehat():
    return "I was going to put a picture of the Cat in the Hat here but I got lazy and just put some text"

@app.route('/thing1')
def thingone():
    return "Same, but for Thing One :/"

@app.route('/thing2')
def thingtwo():
    return "Same, but for Thing Two :/"

if __name__ == '__main__':
    app.run()
