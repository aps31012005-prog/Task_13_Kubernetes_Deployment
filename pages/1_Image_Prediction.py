import streamlit as st
import requests
from PIL import Image


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Image Prediction",
    page_icon="🔮",
    layout="wide"
)


# ==========================================
# Flask API Configuration
# ==========================================

FLASK_API_URL = "http://127.0.0.1:5000/predict"


# ==========================================
# Page Title
# ==========================================

st.title("🔮 CIFAR-10 Image Prediction")

st.write(
    "Upload an image and the Streamlit frontend "
    "will send it to the Flask backend for real-time prediction."
)


# ==========================================
# Backend Status
# ==========================================

try:

    response = requests.get(
        "http://127.0.0.1:5000/",
        timeout=3
    )

    if response.status_code == 200:

        st.success("🟢 Flask API is connected and running.")

    else:

        st.warning("🟡 Flask API responded with an unexpected status.")

except requests.exceptions.RequestException:

    st.error(
        "🔴 Flask API is not running. "
        "Please start flask_api.py first."
    )


# ==========================================
# File Uploader
# ==========================================

uploaded_file = st.file_uploader(
    "📤 Upload an image",
    type=["jpg", "jpeg", "png"]
)


# ==========================================
# Prediction
# ==========================================

if uploaded_file is not None:

    # Open image for displaying in Streamlit
    image = Image.open(uploaded_file).convert("RGB")

    # Display uploaded image
    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🖼️ Uploaded Image")

        st.image(
            image,
            caption="Input Image",
            width=300
        )


    # ==========================================
    # Send Image to Flask API
    # ==========================================

    with st.spinner("🤖 Sending image to Flask API..."):

        try:

            # Move file pointer to beginning
            uploaded_file.seek(0)

            # Prepare image for HTTP request
            files = {
                "image": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    uploaded_file.type
                )
            }

            # Send POST request to Flask backend
            response = requests.post(
                FLASK_API_URL,
                files=files,
                timeout=30
            )


            # ==========================================
            # Process Flask Response
            # ==========================================

            if response.status_code == 200:

                result = response.json()

                predicted_class = result.get(
                    "predicted_class",
                    "Unknown"
                )

                confidence = result.get(
                    "confidence",
                    0
                )


                # ==========================================
                # Display Prediction
                # ==========================================

                with col2:

                    st.subheader("🤖 Prediction")

                    st.success(
                        f"Predicted Class: **{predicted_class}**"
                    )

                    st.metric(
                        "Confidence",
                        f"{confidence:.2f}%"
                    )


                # ==========================================
                # API Response
                # ==========================================

                st.markdown("---")

                st.subheader("📡 Flask API Response")

                st.json(result)


                # ==========================================
                # Integration Status
                # ==========================================

                st.success(
                    "✅ Streamlit → Flask → CNN Model → "
                    "Prediction workflow completed successfully."
                )


            else:

                st.error(
                    f"Flask API returned HTTP "
                    f"{response.status_code}"
                )

                try:

                    st.json(response.json())

                except Exception:

                    st.text(response.text)


        except requests.exceptions.ConnectionError:

            st.error(
                "❌ Could not connect to Flask API. "
                "Make sure flask_api.py is running on port 5000."
            )


        except requests.exceptions.Timeout:

            st.error(
                "⏱️ Flask API request timed out. "
                "Please try again."
            )


        except Exception as e:

            st.error(
                f"❌ An unexpected error occurred: {str(e)}"
            )


else:

    st.info(
        "👆 Please upload a JPG, JPEG, or PNG image to begin."
    )
