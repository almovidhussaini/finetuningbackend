import streamlit as st
import requests
import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


API_URL = os.getenv("API_URL")


# Page configuration
st.set_page_config(
    page_title="LLM Fine-Tuning Evaluation Platform",
    page_icon="🤖",
    layout="wide"
)


st.title("🤖 LLM Fine-Tuning Evaluation Platform")

st.write(
    "Compare Base Qwen3-4B vs Fine-tuned Qwen3-4B"
)


# Input box

prompt = st.text_area(
    "Enter your prompt:",
    height=150,
    placeholder="Example: Write a Python function for binary search"
)



if st.button("🚀 Compare Models"):

    if prompt.strip() == "":
        st.warning("Please enter a prompt")

    else:

        with st.spinner("Generating responses..."):

            try:

                response = requests.post(
                    f"{API_URL}/compare",
                    json={
                        "prompt": prompt
                    },
                    timeout=300
                )


                result = response.json()
                result = response.json()

                st.write("API RESPONSE:")
                st.json(result)


                # Create two columns

                col1, col2 = st.columns(2)


                # Base Model

                with col1:

                    st.subheader("🔵 Base Model")

                    st.write(
                        result["base_model"]["response"]
                    )

                    st.info(
                        f"Latency: {result['base_model']['latency_seconds']} seconds"
                    )


                # Fine tuned model

                with col2:

                    st.subheader("🟢 Fine-tuned Model")

                    st.write(
                        result["finetuned_model"]["response"]
                    )


                    st.success(
                        f"Latency: {result['finetuned_model']['latency_seconds']} seconds"
                    )


            except Exception as e:

                st.error(
                    f"API Error: {e}"
                )