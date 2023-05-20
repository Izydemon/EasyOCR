import easyocr as ocr
import streamlit as st
from PIL import Image
import numpy as np

#Title
st.title("Easy OCR")

pattern = st.text_input("Insert pattern", value="1234")

#image uploader
image = st.file_uploader(label = "Upload your image", type=['png', 'jpg','jpeg'])

@st.cache_data
def load_model():
    reader = ocr.Reader(["es"])
    return reader

reader = load_model()

if image is not None:

    input_image = Image.open(image)
    st.image(input_image)
    with st.spinner('Working...'):

        result = reader.readtext(np.array(input_image), allowlist='0123456789')

        result_text =[]

        for text in result:
            if len(text[1]) == len(pattern) and text[2] >= 0.5:
                result_text.append(text[1])

        st.write(result_text)
    st.success("Done!")
else:
    st.write("Upload an Image")