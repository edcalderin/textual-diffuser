from io import BytesIO

import streamlit as st
from src.inference import Inference


def app():
    st.header("Text-to-image Web App")
    st.subheader("Powered by Hugging Face")
    user_input = st.text_area(
        "Enter your text prompt below and click the button to submit."
    )

    option = st.selectbox(
        "Select model (in order of processing time)",
        (
            "nota-ai/bk-sdm-small",
            "CompVis/stable-diffusion-v1-4",
            "runwayml/stable-diffusion-v1-5",
            "prompthero/openjourney",
            "hakurei/waifu-diffusion",
            "stabilityai/stable-diffusion-2-1",
            "dreamlike-art/dreamlike-photoreal-2.0",
        ),
    )

    with st.form("my_form"):
        submit = st.form_submit_button(label="Submit text prompt")

    if submit:
        with st.spinner(text="Generating image ... It may take up to 1 hour."):
            image, duration = Inference(option).text2image(prompt=user_input)

            buf = BytesIO()
            image.save(buf, format="PNG")
            byte_im = buf.getvalue()

            hours, seconds = divmod(duration, 3600)
            minutes, seconds = divmod(seconds, 60)

            st.success(
                f"Processing time: {int(hours):0>2}:{int(minutes):0>2}:{seconds:05.2f}."
            )

            st.image(image)

            st.download_button(
                label="Click here to download",
                data=byte_im,
                file_name="generated_image.png",
                mime="image/png",
            )


if __name__ == "__main__":
    app()
