from flask import Flask, request, jsonify, render_template

import moscow_apart_predict_server

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/calculate', methods=['POST'])
def calculate_price():
    data = request.data

    price = float(moscow_apart_predict_server.predict_apartment_price(apartment_data_json=data))

    return jsonify({'price': round(price, 2)})

if __name__ == '__main__':
    app.run(debug=True)
