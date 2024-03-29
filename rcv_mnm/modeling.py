import collections
import numpy as np
import os
import pandas as pd
import preprocess
import streamlit as st
import tensorflow as tf

@st.cache(allow_output_mutation=True)
def load_model(
    model_path: str = "models/latest_finetuned_mnm_model.h5",
):
    export_path = os.path.join(os.getcwd(), model_path)
    model = tf.keras.models.load_model(export_path)
    return model

def predict(
    image,
    labels_lookup: dict,
    model,
):
    prediction_probs = model.predict(image)
    Prediction       = collections.namedtuple("Prediction", ["label", "confidence"])

    prediction = Prediction(
        labels_lookup[np.argmax(prediction_probs[0])],
        np.max(prediction_probs[0]),
    )
    return prediction