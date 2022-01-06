#!/usr/bin/env python

from PIL import Image
import helpers
import modeling
import preprocess
import pandas as pd
import random
import streamlit as st

def make_prediction(
    cleaned_img
):
    if None in cleaned_img:
        st.header("No Face was found in the provided image!")
        st.image(Image.open("resources/no_face.jpeg"))
    else:
        st.header("Here is the image you've selected.")
        st.subheader("(passed through a MTCNN face recognition model)")
        st.image(cleaned_img)

        prediction = modeling.predict(cleaned_img, labels, model)
        st.header(f"""{prediction.label.replace("_", " ")} is the most likely person.""")
        st.subheader(f"(Confidence: {prediction.confidence})")
        if prediction.label == "Robert_Beatty":
            image_base64 = helpers.img_to_bytes("resources/robert_resume.jpeg")
            link="https://docs.google.com/document/d/1iGtDjwRcILFmo6pw9rNcCMFhKNNyJiSoNm5s1VxrJUs/edit?usp=sharing"
            html = f"<a href='{link}'><img src='data:image/png;base64,{image_base64}' target='_blank'></a>"
            st.markdown(html, unsafe_allow_html=True)
        elif prediction.label == "Linus_Sebastian":
            output_image = Image.open("resources/linus_dont_do_it.jpeg")
            st.image(output_image)
        else:
            pass

if __name__ == "__main__":
    model  = modeling.load_model()
    labels = helpers.load_label_dict()

    st.title("Welcome To My Facial Image Classifier!")
    instructions = """
        Either upload your own image or select from the sidebar to get a preconfigured image.
        The image you select or upload will be fed through the Deep Neural Network in real-time
        and the output will be displayed to the screen. In the sidebar you can find the list of people
        included in the facial recognition model.
    """
    st.write(instructions)

    file = st.file_uploader("Upload An Image")
    if file:
        cleaned_img = preprocess.extract_image_to_nparray(file)
    else:
        person_name = st.sidebar.selectbox(
            "Person",
            labels.values(),
        )
        if person_name == "Robert_Beatty":
            file_name = f"resources/robert{random.randint(1, 2)}.jpg"
            cleaned_img = preprocess.extract_image_to_nparray(file_name)
        else:
            try:
                url = helpers.get_random_image_url(person_name)
                cleaned_img = preprocess.extract_image_to_nparray(url, "url")
            except:
                st.header("Failed to get content from random image URL. Please try again.")
                cleaned_img = [None]

    make_prediction(cleaned_img)