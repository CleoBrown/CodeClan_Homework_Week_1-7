from app import app
from flask import render_template
from models.game_list import games


@app.route("/")
def index():
    return "Hello World!"


@app.route("/orders")
def get_orders():
    return render_template(
        "index.html", title="Orders", batman=games, animal_crossing="Nintendo"
    )


@app.route("/orders/<index>")
def get_order(index):
    return render_template("order.html", title=f"Order {index}", game=games[int(index)])
