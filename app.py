import csv
from flask import Flask, render_template, request

app = Flask(__name__)

data = [{"currency":"dolar amerykański","code":"USD","bid":4.0122,"ask":4.0932},{"currency":"dolar australijski","code":"AUD","bid":2.8500,"ask":2.9076},{"currency":"dolar kanadyjski","code":"CAD","bid":3.1340,"ask":3.1974},{"currency":"euro","code":"EUR","bid":4.5487,"ask":4.6405},{"currency":"forint (Węgry)","code":"HUF","bid":0.012555,"ask":0.012809},{"currency":"frank szwajcarski","code":"CHF","bid":4.3655,"ask":4.4537},{"currency":"funt szterling","code":"GBP","bid":5.3422,"ask":5.4502},{"currency":"jen (Japonia)","code":"JPY","bid":0.035512,"ask":0.03623},{"currency":"korona czeska","code":"CZK","bid":0.1790,"ask":0.1826},{"currency":"korona duńska","code":"DKK","bid":0.6117,"ask":0.6241},{"currency":"korona norweska","code":"NOK","bid":0.4413,"ask":0.4503},{"currency":"korona szwedzka","code":"SEK","bid":0.4444,"ask":0.4534},{"currency":"SDR (MFW)","code":"XDR","bid":5.6265,"ask":5.7401}]

pola = ['currency', 'code', 'bid', 'ask']
with open('file.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = pola, delimiter=';')
    writer.writeheader()
    for x in data:
        writer.writerow(x)

@app.route("/", methods=["GET", "POST"])
def select():
    if request.method == "POST":
        data2 = request.form
        currency = data2.get("id")
        sell = (data["ask"])
        amount = data2.get("ilosc")
        razem = sell * amount
        return razem

    return render_template("waluta.html")
