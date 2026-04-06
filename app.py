import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the trained model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model(r"securelens_model.h5", compile=False)
    return model

model = load_model()

# Initialize session state for storing posts
if "posts" not in st.session_state:
    st.session_state["posts"] = []

st.title("SecureLens AI Moderation System")
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Upload & Post", "See Posts"])

if menu == "Upload & Post":
    st.header("📤 Upload & Post an Image")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Preprocess the image for the model
        image = image.resize((224, 224))  # Resize to model input size
        image_array = np.array(image) / 255.0  # Normalize pixel values
        image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension

        # Make a prediction
        prediction = model.predict(image_array)
        clothing_coverage = float(prediction[0][0]) * 100  # Convert to percentage

        # Display result
        st.write(f"👕 Clothing Coverage: **{clothing_coverage:.2f}%**")

        # Eligibility check
        if clothing_coverage < 20:
            st.error("🚫 This image is **NOT** eligible to post (Too much exposed skin).")
        else:
            st.success("✅ This image is **eligible** to post.")
            if st.button("📤 Post"):
                # Store image in session state (simulating posting)
                st.session_state["posts"].append(image)
                st.success("✅ Successfully posted!")

elif menu == "See Posts":
    st.header("📸 Your Posted Images")

    if st.session_state["posts"]:
        for img in st.session_state["posts"]:
            st.image(img, use_column_width=True)
    else:
        st.write("No posts yet. Upload and post an image first! 👆")