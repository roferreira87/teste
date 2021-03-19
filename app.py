from flask import Flask

app = Flask ('Teste')

@app.route('/ola')
def ola():
    return 'Olá mundo no flask'

app.run(debug=True)