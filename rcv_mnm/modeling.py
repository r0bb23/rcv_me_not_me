import collections
import numpy as np
import os
import pandas as pd
from rcv_mnm import preprocess
import streamlit as st
import tensorflow as tf

@st.cache(allow_output_mutation=True)
def load_model(
    model_path: str = "models/latest_finetuned_mnm_model.h5",
):
    model = tf.keras.models.load_model(model_path)
    return model

@st.cache()
def predict(
    image,
    labels_lookup: dict,
    model,
):
    """Transforming input image according to ImageNet paper
    The Resnet was initially trained on ImageNet dataset
    and because of the use of transfer learning, I froze all
    weights and only learned weights on the final layer.
    The weights of the first layer are still what was
    used in the ImageNet paper and we need to process
    the new images just like they did.
    This function transforms the image accordingly,
    puts it to the necessary device (cpu by default here),
    feeds the image through the model getting the output tensor,
    converts that output tensor to probabilities using Softmax,
    and then extracts and formats the top k predictions."""
    prediction_probs = model.predict(image)
    Prediction = collections.namedtuple("Prediction", ["label", "confidence"])

    prediction = Prediction(labels_lookup[np.argmax(prediction_probs[0])], np.max(prediction_probs[0]))
    return prediction