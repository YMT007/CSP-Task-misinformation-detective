import streamlit as st
import random

st.set_page_config(page_title="Misinformation Detective", page_icon="🕵️")

st.title("🕵️ Misinformation Detective")
st.write("Learn to respond to public health information by spotting red flags before sharing.")

# ---------------- Red Flags ----------------
RED_FLAGS = [
    ("No credible source", "No expert, study, or official organization is named."),
    ("Emotional language", "Uses fear or shock instead of clear facts."),
    ("Exaggerated claims", "Promises instant or 100% results."),
    ("Conspiracy framing", "Claims secret cover-ups without evidence."),
    ("Oversimplified solution", "One simple fix for a complex issue."),
    ("Urgency to share", "Pressures you to act or share immediately."),
    ("Anecdotal evidence", "Personal story instead of scientific data.")
]

if "show_flags" not in st.session_state:
    st.session_state.show_flags = False

if st.button("🚩 Show / Hide Red Flags Guide"):
    st.session_state.show_flags = not st.session_state.show_flags

if st.session_state.show_flags:
    st.markdown("### 🚩 Red Flags Guide")
    for flag, desc in RED_FLAGS:
        st.markdown(f"- **{flag}** — {desc}")

st.divider()

# ---------------- Game Prompts (15) ----------------
POSTS = [
    {"text": "This detox drink removes all toxins in 24 hours.", "best": "Flag", "why": "Exaggerated claim with no evidence."},
    {"text": "WHO states vaccines reduce severe disease risk.", "best": "Trust", "why": "Credible public health organization."},
    {"text": "My uncle cured diabetes naturally.", "best": "Question", "why": "Anecdotal evidence."},
    {"text": "Share now before doctors delete this cure!", "best": "Flag", "why": "Urgency and conspiracy framing."},
    {"text": "A university study supports mask use.", "best": "Trust", "why": "Based on scientific research."},
    {"text": "This herb works better than vaccines.", "best": "Flag", "why": "No reliable evidence."},
    {"text": "This diet worked for me so it works for everyone.", "best": "Question", "why": "One experience ≠ universal truth."},
    {"text": "The government is hiding vaccine dangers.", "best": "Flag", "why": "Serious claim without proof."},
    {"text": "Doctors recommend regular exercise.", "best": "Trust", "why": "Well-established medical advice."},
    {"text": "One pill prevents all illnesses.", "best": "Flag", "why": "Unrealistic promise."},
    {"text": "Share quickly before this post disappears.", "best": "Question", "why": "Pressures fast action."},
    {"text": "Hospital guidelines explain flu prevention.", "best": "Trust", "why": "Reliable institutional source."},
    {"text": "Everyone loses weight instantly using this trick.", "best": "Flag", "why": "Instant results are misleading."},
    {"text": "A blogger says this supplement fixed everything.", "best": "Question", "why": "No credible source."},
    {"text": "Public health data shows vaccination success.", "best": "Trust", "why": "Uses evidence and data."}
]

if "index" not in st.session_state:
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.order = random.sample(POSTS, len(POSTS))

post = st.session_state.order[st.session_state.index]

st.subheader(f"Case {st.session_state.index + 1} / 15")
st.write(post["text"])

choice = st.radio("What would you do?", ["Trust", "Question", "Flag"])

if st.button("Submit decision"):
    if choice == post["best"]:
        st.success("Good decision!")
        st.session_state.score += 1
    else:
        st.error("Not the best choice.")
    st.info(post["why"])
    st.session_state.index += 1

if st.session_state.index >= len(POSTS):
    st.balloons()
    st.header("Game Complete")
    st.write(f"Final score: {st.session_state.score} / 15")
    if st.button("Play again"):
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.order = random.sample(POSTS, len(POSTS))
