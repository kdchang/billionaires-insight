from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def get_index():
    return render_template('index.html')

@app.route('/data/billionaires')
def get_billionaires_data():
    year = request.args.get('year')
    if year not None:
        with open('./static/data/' + year + '.json') as f:
            data = f.read()
        return data
    else:
        return {}

if __name__ == '__main__':
    app.run()