
import streamlit as st
import random

st.set_page_config(page_title="Misinformation Detective", layout="centered")

st.title("🕵️ Misinformation Detective")
st.caption("Investigate public health posts and stop misinformation from spreading")

posts = [
    {"text": "This supplement boosts immunity instantly. Doctors hate it.",
     "answer": "Misinformation",
     "flags": ["Emotional language", "Fake expert", "No sources"],
     "explanation": "No supplement can instantly boost immunity."},

    {"text": "Regular handwashing reduces the spread of infectious diseases.",
     "answer": "Reliable",
     "flags": [],
     "explanation": "Handwashing is strongly supported by scientific evidence."},

    {"text": "One study proves vaccines are dangerous.",
     "answer": "Misinformation",
     "flags": ["Cherry-picked data", "Overgeneralization"],
     "explanation": "Scientific conclusions require many studies."},

    {"text": "Antibiotics do not work against viral infections.",
     "answer": "Reliable",
     "flags": [],
     "explanation": "Antibiotics target bacteria, not viruses."},

    {"text": "Natural remedies are safer than medicine because they are natural.",
     "answer": "Misinformation",
     "flags": ["False assumption", "Overgeneralization"],
     "explanation": "Natural does not always mean safe."},

    {"text": "Vaccines contain microchips to track people.",
     "answer": "Misinformation",
     "flags": ["Conspiracy framing", "No sources"],
     "explanation": "There is no evidence vaccines contain tracking devices."},

    {"text": "Wearing masks can reduce the spread of respiratory viruses.",
     "answer": "Reliable",
     "flags": [],
     "explanation": "Masks reduce transmission of respiratory droplets."},

    {"text": "Drinking detox drinks removes all toxins from your body.",
     "answer": "Misinformation",
     "flags": ["Overgeneralization", "False cure"],
     "explanation": "The liver and kidneys already remove toxins."},

    {"text": "Mental health conditions can be treated with professional support.",
     "answer": "Reliable",
     "flags": [],
     "explanation": "Therapy and medical care are evidence-based treatments."},

    {"text": "Only elderly people can get seriously sick from viruses.",
     "answer": "Misinformation",
     "flags": ["Overgeneralization"],
     "explanation": "People of all ages can become seriously ill."},

    {"text": "Too much sugar intake increases the risk of health problems.",
     "answer": "Reliable",
     "flags": [],
     "explanation": "Excess sugar intake is linked to health risks."},

    {"text": "Essential oils can replace all modern medicine.",
     "answer": "Misinformation",
     "flags": ["Overgeneralization", "False cure"],
     "explanation": "Essential oils cannot replace medical treatment."},

    {"text": "Vaccination helps protect both individuals and communities.",
     "answer": "Reliable",
     "flags": [],
     "explanation": "Vaccines reduce disease spread and severity."},

    {"text": "If a health post makes you feel scared, it is more likely to be true.",
     "answer": "Misinformation",
     "flags": ["Emotional language"],
     "explanation": "Fear-based language is commonly used in misinformation."},

    {"text": "Checking information from official health organizations improves accuracy.",
     "answer": "Reliable",
     "flags": [],
     "explanation": "Official organizations base advice on scientific evidence."}
]

all_flags = [
    "Emotional language",
    "Fake expert",
    "No sources",
    "Overgeneralization",
    "Cherry-picked data",
    "Conspiracy framing",
    "False assumption",
    "False cure"
]

if "order" not in st.session_state:
    st.session_state.order = random.sample(range(len(posts)), len(posts))
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.show_feedback = False

if st.session_state.index < len(posts):
    post = posts[st.session_state.order[st.session_state.index]]

    st.subheader("🔎 Viral Health Post")
    st.info(post["text"])

    selected_flags = st.multiselect("🚩 Select all red flags:", all_flags)

    choice = st.radio("⚖️ Final decision:", ["Reliable", "Misinformation"])

    if st.button("Submit Investigation"):
        st.session_state.show_feedback = True

        for flag in selected_flags:
            if flag in post["flags"]:
                st.session_state.score += 2
            else:
                st.session_state.score -= 1

        if choice == post["answer"]:
            st.session_state.score += 3

    if st.session_state.show_feedback:
        st.markdown("---")
        st.write("**Correct answer:**", post["answer"])
        st.write("**Correct red flags:**", ", ".join(post["flags"]) if post["flags"] else "None")
        st.write("**Explanation:**", post["explanation"])
        st.write("**Score:**", st.session_state.score)

        if st.button("Next Case"):
            st.session_state.index += 1
            st.session_state.show_feedback = False

else:
    st.subheader("🏁 Investigation Complete")
    st.write(f"### Final Score: **{st.session_state.score}**")

    if st.button("Restart Game"):
        del st.session_state["order"]
