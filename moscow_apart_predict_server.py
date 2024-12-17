import json
import pandas as pd
from catboost import Pool
import pickle


def prepare_data(apartment_data_bytes, metro_coords_data_filename='metro_stations_dataset.csv'):
    apartment_data = json.loads(apartment_data_bytes.decode('utf-8'))

    df = pd.DataFrame([apartment_data])
    metro_coords_data = pd.read_csv(metro_coords_data_filename)

    metro_coords_data.drop(['lat', 'lon'], axis=1, inplace=True)
    df = pd.merge(df, metro_coords_data, on='Metro station', how='left')

    cat_features = ['Apartment type', 'Metro station', 'Renovation', 'District']
    predict_pool = Pool(data=df, cat_features=cat_features)
    return predict_pool


def predict_apartment_price(apartment_data_json, model_filename='moscow_aparts_predict_model.cb', metro_coords_data_filename='metro_stations_dataset.csv'):
    loaded_model = pickle.load(open(model_filename, 'rb'))
    predict_pool = prepare_data(apartment_data_json)
    predicted_price = loaded_model.predict(predict_pool)
    return predicted_price[0]
