from flask import Flask, render_template, request
import pandas as pd
import pickle as pk
from urllib.parse import quote

app = Flask(__name__)

# Load model and data
model = pk.load(open('model.pkl', 'rb'))
cars_data = pd.read_csv('Cardetails.csv')

# Brand-model mapping
cars_data['brand'] = cars_data['name'].apply(lambda x: x.split()[0])
brand_models = cars_data.groupby('brand').apply(
    lambda df: [name.replace(df.name, '').strip() for name in df['name'].unique()]
).to_dict()

def get_car_image_url(brand, model):
    query = f"{brand} {model} car"
    return f"https://www.bing.com/images/search?q={quote(query)}"

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    image_link = None

    if request.method == "POST":
        brand = request.form["brand"]
        selected_model = request.form["model"]
        fuel = request.form["fuel"]
        seller_type = request.form["seller_type"]
        transmission = request.form["transmission"]
        owner = request.form["owner"]
        year = int(request.form["year"])
        km_driven = int(request.form["km_driven"])
        mileage = float(request.form["mileage"])
        engine = int(request.form["engine"])
        max_power = int(request.form["max_power"])
        seats = int(request.form["seats"])

        # Prepare input
        input_data_model = pd.DataFrame([[brand, year, km_driven, fuel, seller_type, transmission, owner,
                                          mileage, engine, max_power, seats]],
                                          columns=['name', 'year', 'km_driven', 'fuel', 'seller_type', 'transmission',
                                                   'owner', 'mileage', 'engine', 'max_power', 'seats'])

        input_data_model['owner'].replace(['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'],
                                          [1, 2, 3, 4, 5], inplace=True)
        input_data_model['fuel'].replace(['Diesel', 'Petrol', 'LPG', 'CNG'], [1, 2, 3, 4], inplace=True)
        input_data_model['seller_type'].replace(['Individual', 'Dealer', 'Trustmark Dealer'], [1, 2, 3], inplace=True)
        input_data_model['transmission'].replace(['Manual', 'Automatic'], [1, 2], inplace=True)
        input_data_model['name'].replace(list(brand_models.keys()), list(range(1, len(brand_models) + 1)), inplace=True)

        # Prediction
        car_price = model.predict(input_data_model)
        prediction = abs(int(car_price[0]))
        image_link = get_car_image_url(brand, selected_model)

    return render_template("index.html",
                           brand_models=brand_models,
                           brands=sorted(brand_models.keys()),
                           fuels=cars_data['fuel'].unique(),
                           sellers=cars_data['seller_type'].unique(),
                           transmissions=cars_data['transmission'].unique(),
                           owners=cars_data['owner'].unique(),
                           prediction=prediction,
                           image_link=image_link)

if __name__ == "__main__":
    app.run(debug=True)
