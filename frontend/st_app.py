import streamlit as st
import requests
import random

revert_label = {
    "0": "No Bias",
    "1": "Hate Speech",
    "2": "Fake News",
    "3": "Political Bias",
    "4": "Racial Bias",
    "5": "Gender Bias",
}

list = [
    "Women always wanted equality until it comes to paying the bills",
    "Why is it 7.50pm and I haven't eaten dinner. Women, take me back to the 70s.",
    "I don't trust my doctor because he's black",
    "Migrants do take our jobs",
    "Pope Francis Shocks World, Endorses Donald Trump for President, Releases Statement",
    "There are too many italian maggot in this country, and they need to leave",
    "Best tennis players in the world: from roger federer to serena williams",
]

BACKEND_URL = "https://toxicity-classifier-cwkm3of3qa-ew.a.run.app"
st.set_page_config(page_title="Toxicity Detector", page_icon="🤖")

if 'sentence' not in st.session_state:
    st.session_state.sentence = 'value'

st.image("https://nohatespeech.network/wp-content/uploads/2020/10/cropped-No-Hate-Speech-Logo-Transperent-1-1.png", width=400, caption="No Hate Speech")

st.divider()


st.markdown("#### Please select a sentence for **toxicity classification**.")
# dropdown = st.selectbox("Select a sentence", list)

if st.button("🔮 Example"):
    st.session_state.sentence = random.choice(list)
    st.text(st.session_state.sentence)

if st.button("🔮 Predict"):
    st.divider()
    response = requests.get(f"{BACKEND_URL}/predict?sentence={st.session_state.sentence}")
    y_pred = response.json()

    st.markdown(f'### 🤖 The sentence has `{revert_label.get(str(y_pred), "Other Bias")}`')
