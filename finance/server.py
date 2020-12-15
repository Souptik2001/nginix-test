from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return 'This is for managing finance'

app.run(port=3001, debug=True)
