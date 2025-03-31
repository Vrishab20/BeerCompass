import pickle

import pandas as pd
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from label_encoders import *
from similarity_utils import *

app = FastAPI()
with open("models/beer_classifier.pkl", "rb") as f:
    beer_classifier = pickle.load(f)
with open("models/cosine_similarity.pkl", "rb") as f:
    cosine_sim = pickle.load(f)

beer_data = pd.read_csv("models/frame.csv")
is_dark_encoder = IsDarkLabelEncoder()
country_encoder = CountryLabelEncoder()
availability_encoder = AvailabilityLabelEncoder()
flavor_encoder = FlavorLabelEncoder()
alcohol_lvl_encoder = AlcoholLabelEncoder()
beer_data["country"] = country_encoder.transform(beer_data["country"])
beer_data["availability"] = availability_encoder.transform(beer_data["availability"])
beer_data["flavor"] = flavor_encoder.transform(beer_data["flavor"])
beer_data["is_dark"] = is_dark_encoder.transform(beer_data["is_dark"])
beer_data["alcohol_lvl"] = alcohol_lvl_encoder.transform(beer_data["alcohol_lvl"])
print('here')

def encode_data(country, availability, score, flavor, is_dark, alcohol_level):
    is_dark = is_dark_encoder.transform([is_dark])[0]
    country = country_encoder.transform([country])[0]
    availability = availability_encoder.transform([availability])[0]
    flavor = flavor_encoder.transform([flavor])[0]
    alcohol_level = alcohol_lvl_encoder.transform([alcohol_level])[0]

    user_inputs = [country, availability, score, flavor, is_dark, alcohol_level]
    return user_inputs


@app.post("/")
async def fulfillment(request: Request):
    print('aaaaaaaaaaaaaaaaaaaa')
    payload = await request.json()
    print(payload)
    global beer_classifier
    global beer_data
    global cosine_sim

    intent_name = payload["queryResult"]["intent"]["displayName"]
    # print(intent_name)
    beer_names = []

    fulfillment_message = payload["queryResult"]["fulfillmentText"]
    rating_mapping = {"Excellent": 5, "Good": 4, "Average": 2.5, "Bad": 1}
    if intent_name == "FindBeerByUserRating Intent":
        payload = await request.json()
        print(beer_data)
        is_dark = payload["queryResult"]["outputContexts"][0]["parameters"][
            "beerappearance"
        ]
        country = payload["queryResult"]["outputContexts"][0]["parameters"][
            "beerregion"
        ]
        availability = payload["queryResult"]["outputContexts"][0]["parameters"][
            "beerseason"
        ][0]
        flavor = payload["queryResult"]["outputContexts"][0]["parameters"]["BeerFlavor"]
        alcohol_level = payload["queryResult"]["outputContexts"][0]["parameters"][
            "AlcoholLevel"
        ]
        score = rating_mapping[
            payload["queryResult"]["outputContexts"][0]["parameters"]["beerrating"][0]
        ]
        user_inputs = encode_data(
            country, availability, score, flavor, is_dark, alcohol_level
        )

        cluster_label = beer_classifier.predict([user_inputs])[0]
        filtered_data = filter_dataset(cluster_label, beer_data)
        top_indices = calculate_similarity(user_inputs, filtered_data)
        top_beers = get_top_beers(top_indices, filtered_data, n=5)
        fulfillment_message = payload["queryResult"]["fulfillmentText"]
        beer = list(set(top_beers))[0]
        return JSONResponse(
            content={
                "fulfillmentMessages": [{"text": {"text": [beer, fulfillment_message]}}]
            },
            headers={"Content-Type": "application/json"},
        )

