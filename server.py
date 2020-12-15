from flask import Flask
import os

app=Flask(__name__)

@app.route('/')
def index():
    return f"This is for {os.environ.get('ID')} management"

app.run(port=3000, debug=True)
