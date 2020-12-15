from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return 'This is for managing health'

app.run(port=3002, debug=True)
