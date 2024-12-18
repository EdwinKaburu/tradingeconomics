# Name: Edwin Kaburu
# Date: 12/17/2024
# TradingEconomics API Demo

from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
def main_default():
    return redirect('/mainPage/')


@app.route('/mainPage/')
def main_page():
    return render_template("Main.html")


if __name__ == '__main__':
    app.run()
