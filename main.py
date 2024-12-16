from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/calculate', methods=['POST'])
def calculate_price():
    data = request.json

    apartment_type = data.get('apartment_type')
    metro_station = data.get('metro_station')
    minutes_to_metro = int(data.get('minutes_to_metro'))
    number_of_rooms = int(data.get('number_of_rooms'))
    area = float(data.get('area'))
    living_area = float(data.get('living_area'))
    kitchen_area = float(data.get('kitchen_area'))
    floor = int(data.get('floor'))
    number_of_floors = int(data.get('number_of_floors'))
    renovation = data.get('renovation')


    price = 6.9

    return jsonify({'price': round(price, 2)})

if __name__ == '__main__':
    app.run(debug=True)
