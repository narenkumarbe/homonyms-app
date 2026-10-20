import streamlit as st

st.set_page_config(page_title="Homonyms Cards", layout="centered")

homonyms = [
    {
        "word": "Bat",
        "sentence1": "The bat flew out of the cave.",
        "sentence2": "He bought a new cricket bat."
    },
    {
        "word": "Bank",
        "sentence1": "I deposited money in the bank.",
        "sentence2": "We sat on the river bank."
    },
    {
        "word": "Bark",
        "sentence1": "The dog began to bark.",
        "sentence2": "The tree's bark is rough."
    },
    {
        "word": "Match",
        "sentence1": "Our team won the match.",
        "sentence2": "He lit a candle with a match."
    },
    {
        "word": "Ring",
        "sentence1": "She wore a gold ring.",
        "sentence2": "I heard the phone ring."
    },
    {
        "word": "Watch",
        "sentence1": "My watch is expensive.",
        "sentence2": "Please watch the road carefully."
    },
    {
        "word": "Light",
        "sentence1": "Turn on the light.",
        "sentence2": "This bag is very light."
    },
    {
        "word": "Well",
        "sentence1": "I am feeling well today.",
        "sentence2": "They found water in the well."
    },
    {
        "word": "Pupil",
        "sentence1": "The pupil answered the teacher's question.",
        "sentence2": "The doctor examined the pupil of his eye."
    },
    {
        "word": "Spring",
        "sentence1": "Flowers bloom in spring.",
        "sentence2": "The machine contains a metal spring."
    }
]

# Initialize current card index
if "card_index" not in st.session_state:
    st.session_state.card_index = 0

current = homonyms[st.session_state.card_index]

st.title("📚 Nikhilesh's English Activity")

# Card
st.markdown(
    f"""
    <div style="
        max-width:700px;
        margin:auto;
        padding:40px;
        border-radius:20px;
        background:linear-gradient(135deg,#4f46e5,#7c3aed);
        color:white;
        text-align:center;
        box-shadow:0px 8px 20px rgba(0,0,0,0.3);
    ">
        <h1>{current['word']}</h1>
        <hr style="border:1px solid rgba(255,255,255,0.3)">
        <p style="font-size:22px; line-height:1.7;">
            {current['sentence1']}            
        </p>
        <p style="font-size:22px; line-height:1.7;">            
            {current['sentence2']}
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")
st.write(f"Card {st.session_state.card_index + 1} of {len(homonyms)}")

# Navigation buttons
col1, col2, col3 = st.columns([1,2,1])

with col1:
    if st.button("⬅ Previous"):
        st.session_state.card_index = (
            st.session_state.card_index - 1
        ) % len(homonyms)
        st.rerun()

with col3:
    if st.button("Next ➡"):
        st.session_state.card_index = (
            st.session_state.card_index + 1
        ) % len(homonyms)
        st.rerun()