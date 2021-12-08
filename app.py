import csv
from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

@app.route("/", methods =["GET", "POST"])
def calculate():
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    data = response.json()
    result = 0
    if request.method == "POST":
        amount = request.form["amount"]
        for  rate in data[0]["rates"]:
            if rate['code'] == request.form['code']:
                code = rate['code']
                if amount:
                    result = round((float(rate['ask'])) * float(amount), 2)
    if request.method == "GET":
        code = None
    

    return render_template("waluta.html",code=code,result=result)

@app.route("/zapis")
def zapis():
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    data = response.json()

    pola = ['currency', 'code', 'bid', 'ask']
    with open('file.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = pola, delimiter=';')
        writer.writeheader()
        for x in data[0]["rates"]:
            writer.writerow(x)
    return redirect("/")