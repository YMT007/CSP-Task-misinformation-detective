import streamlit as st
import random

st.set_page_config(page_title="Misinformation Detective", page_icon="🕵️")

st.title("🕵️ Misinformation Detective")
st.write("Spot misinformation by identifying red flags in public health posts.")

# ---------------- Red Flags ----------------
RED_FLAGS = {
    "No credible source": "No expert, study, or official organization is named.",
    "Emotional language": "Uses fear, shock, or anger instead of facts.",
    "Exaggerated claims": "Promises instant or guaranteed results.",
    "Conspiracy framing": "Claims secrets or cover-ups without evidence.",
    "Oversimplified solution": "One simple fix for a complex issue.",
    "Urgency to share": "Pressures you to act or share immediately.",
    "Anecdotal evidence": "Personal story instead of scientific data."
}

# Toggle guide
if "show_guide" not in st.session_state:
    st.session_state.show_guide = False

if st.button("🚩 Show / Hide Red Flags Guide"):
    st.session_state.show_guide = not st.session_state.show_guide

if st.session_state.show_guide:
    st.markdown("### 🚩 Red Flags Guide")
    for flag, desc in RED_FLAGS.items():
        st.markdown(f"- **{flag}** — {desc}")

st.divider()

# ---------------- Game Posts (15) ----------------
POSTS = [
    {"text": "This detox drink removes all toxins in 24 hours.",
     "flags": ["Exaggerated claims", "No credible source"]},

    {"text": "WHO states vaccines reduce the risk of severe disease.",
     "flags": []},

    {"text": "My uncle cured diabetes naturally.",
     "flags": ["Anecdotal evidence", "No credible source"]},

    {"text": "Share now before doctors delete this cure!",
     "flags": ["Urgency to share", "Conspiracy framing"]},

    {"text": "A university study supports mask use.",
     "flags": []},

    {"text": "This herb works better than vaccines.",
     "flags": ["No credible source", "Exaggerated claims"]},

    {"text": "This diet worked for me so it works for everyone.",
     "flags": ["Anecdotal evidence", "Oversimplified solution"]},

    {"text": "The government is hiding vaccine dangers.",
     "flags": ["Conspiracy framing"]},

    {"text": "Doctors recommend regular exercise.",
     "flags": []},

    {"text": "One pill prevents all illnesses.",
     "flags": ["Exaggerated claims", "Oversimplified solution"]},

    {"text": "Share quickly before this post disappears.",
     "flags": ["Urgency to share"]},

    {"text": "Hospital guidelines explain flu prevention.",
     "flags": []},

    {"text": "Everyone loses weight instantly using this trick.",
     "flags": ["Exaggerated claims"]},

    {"text": "A blogger says this supplement fixed everything.",
     "flags": ["No credible source"]},

    {"text": "Public health data shows vaccination success.",
     "flags": []}
]

# ---------------- Session State ----------------
if "index" not in st.session_state:
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.order = random.sample(POSTS, len(POSTS))

post = st.session_state.order[st.session_state.index]

st.subheader(f"Case {st.session_state.index + 1} / 15")
st.write(post["text"])

choices = st.multiselect(
    "Which red flags apply? (Select all that apply)",
    list(RED_FLAGS.keys())
)

if st.button("Submit"):
    correct = set(post["flags"])
    selected = set(choices)

    if selected == correct:
        st.success("Correct! You identified the red flags accurately.")
        st.session_state.score += 1
    else:
        st.error("Not quite.")
        if correct:
            st.info(f"Correct red flags: {', '.join(correct)}")
        else:
            st.info("This post does not show major red flags.")

    st.session_state.index += 1

# ---------------- End Screen ----------------
if st.session_state.index >= len(POSTS):
    st.balloons()
    st.header("🎉 Game Complete")
    st.write(f"Final score: **{st.session_state.score} / 15**")

    if st.button("Play again"):
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.order = random.sample(POSTS, len(POSTS))
