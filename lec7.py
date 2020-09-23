from flask import Flask, render_template, url_for
import os
import random

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(0, 10)
    
    return render_template("index.html",
        random_number = random_number
    )
    
app.run(
    debug = True,
    host = os.getenv("HOST", "0.0.0.0"),
    port = int(os.getenv("PORT", 8080))
    )