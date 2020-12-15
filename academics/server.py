from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return 'This is for managing academics'

app.run(port=3000, debug=True)
