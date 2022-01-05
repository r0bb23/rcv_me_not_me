from bs4 import BeautifulSoup
import base64
import io
import json
import random
import streamlit as st
import urllib

def img_to_bytes(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

@st.cache()
def load_label_dict(
    labels_path: str = "resources/labels.json"
):
    """Retrieves and formats the index to class label lookup dictionary needed to 
    make sense of the predictions. When loaded in, the keys are strings, this also
    processes those keys to integers."""
    with open(labels_path, "r") as f:
        labels = json.load(f)
    labels = {int(k): v for k, v in labels.items()}
    return labels

def get_random_image_url(
    label: str,
):
    query = label.split("_")
    query = '+'.join(query) + "+face"
    url   = "https://www.bing.com/images/search?q=" + query + "&qft=+filterui:imagesize-large&FORM=R5IR3"

    #add the directory for your image here
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    soup = BeautifulSoup(
        urllib.request.urlopen(
            urllib.request.Request(
                url,
                headers=header,
            )
        ),
        "html.parser"
    )

    ActualImages=[]
    for a in soup.find_all("a",{"class":"iusc"}):
        m = json.loads(a["m"])
        murl = m["murl"]
        ActualImages.append(murl)

    return random.choice(ActualImages)