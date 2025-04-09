from flask import Flask, request



app = Flask(__name__)
@app.route('/alkuluku/<l>')
def alkuluku(l):
    l = int(l)
    onAlku = True
    for jakaja in range (2,l):
        if l % jakaja == 0:
            onAlku = False
            break
        else:
            onAlku = True

    answer = {
        'Number': l,
        'IsPrime': onAlku

    }
    return  answer

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)