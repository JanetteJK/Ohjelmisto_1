import json

from flask import Flask, request, Response

app = Flask(__name__)
@app.route('/summa/<l1>/<l2>')
def summa(l1, l2):
    try:
        summa = float(l1) + float(l2)
        tilakoodi = 200
        vastaus = {
            'status': tilakoodi,
            'luku 1': l1,
            'luku 2': l2,
            'summa': summa
        }
    except ValueError:
        tilakoodi = 400
        vastaus = {
            'status': tilakoodi,
            'kuvaus': 'Virheellinen yhteenlaskettava.'
        }

@app.errorhandler(404)
def sivua_ei_löydy(virhe):
    tilakoodi = 404
    vastaus = {
        'status': 404,
        'kuvaus': 'Virheellinen päätepiste.'
    }

    json_vastaus = json.dumps(vastaus)
    return Response(response=json_vastaus, status=tilakoodi, mimetype='application/json')


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000) #'localhost' nettiin 127.0.0.1:3000 = palvelin

