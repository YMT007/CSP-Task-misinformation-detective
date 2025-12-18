import streamlit as st
import random

st.set_page_config(page_title="Misinformation Detective", page_icon="🕵️")

st.title("🕵️ Misinformation Detective")
st.write("Evaluate public health information by judging reliability and identifying red flags.")

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

# ---------------- Posts ----------------
POSTS = [
    {"text": "This detox drink removes all toxins in 24 hours.",
     "reliability": "Misinformation",
     "flags": ["Exaggerated claims", "No credible source"]},

    {"text": "WHO states vaccines reduce the risk of severe disease.",
     "reliability": "Reliable",
     "flags": []},

    {"text": "My uncle cured diabetes naturally.",
     "reliability": "Uncertain",
     "flags": ["Anecdotal evidence", "No credible source"]},

    {"text": "Share now before doctors delete this cure!",
     "reliability": "Misinformation",
     "flags": ["Urgency to share", "Conspiracy framing"]},

    {"text": "A university study supports mask use.",
     "reliability": "Reliable",
     "flags": []},

    {"text": "This herb works better than vaccines.",
     "reliability": "Misinformation",
     "flags": ["No credible source", "Exaggerated claims"]},

    {"text": "This diet worked for me so it works for everyone.",
     "reliability": "Uncertain",
     "flags": ["Anecdotal evidence", "Oversimplified solution"]},

    {"text": "The government is hiding vaccine dangers.",
     "reliability": "Misinformation",
     "flags": ["Conspiracy framing"]},

    {"text": "Doctors recommend regular exercise.",
     "reliability": "Reliable",
     "flags": []},

    {"text": "One pill prevents all illnesses.",
     "reliability": "Misinformation",
     "flags": ["Exaggerated claims", "Oversimplified solution"]},

    {"text": "Share quickly before this post disappears.",
     "reliability": "Uncertain",
     "flags": ["Urgency to share"]},

    {"text": "Hospital guidelines explain flu prevention.",
     "reliability": "Reliable",
     "flags": []},

    {"text": "Everyone loses weight instantly using this trick.",
     "reliability": "Misinformation",
     "flags": ["Exaggerated claims"]},

    {"text": "A blogger says this supplement fixed everything.",
     "reliability": "Uncertain",
     "flags": ["No credible source"]},

    {"text": "Public health data shows vaccination success.",
     "reliability": "Reliable",
     "flags": []}
]

# ---------------- Session State Init ----------------
if "order" not in st.session_state:
    st.session_state.order = random.sample(POSTS, len(POSTS))
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.submitted = False

# ---------------- Red Flag Guide ----------------
if "show_guide" not in st.session_state:
    st.session_state.show_guide = False

if st.button("🚩 Show / Hide Red Flags Guide"):
    st.session_state.show_guide = not st.session_state.show_guide

if st.session_state.show_guide:
    st.markdown("### 🚩 Red Flags Guide")
    for flag, desc in RED_FLAGS.items():
        st.markdown(f"- **{flag}** — {desc}")

st.divider()

# ---------------- Game End ----------------
if st.session_state.index >= len(st.session_state.order):
    st.balloons()
    st.header("🎉 Game Complete")
    st.write(f"Final score: **{st.session_state.score} / 30**")

    if st.button("🔄 Restart Game"):
        st.session_state.order = random.sample(POSTS, len(POSTS))
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.submitted = False

    st.stop()

# ---------------- Current Case ----------------
post = st.session_state.order[st.session_state.index]

st.subheader(f"Case {st.session_state.index + 1} / 15")
st.write(post["text"])

reliability_choice = st.radio(
    "How reliable is this information?",
    ["Reliable", "Uncertain", "Misinformation"],
    key=f"rel_{st.session_state.index}"
)

flag_choices = st.multiselect(
    "Which red flags apply?",
    list(RED_FLAGS.keys()),
    key=f"flags_{st.session_state.index}"
)

# ---------------- Submit ----------------
if st.button("Submit", disabled=st.session_state.submitted):
    st.session_state.submitted = True

    round_score = 0
    if reliability_choice == post["reliability"]:
        round_score += 1

    if set(flag_choices) == set(post["flags"]):
        round_score += 1

    st.info(f"Correct reliability: **{post['reliability']}**")

    if post["flags"]:
        st.info(f"Correct red flags: {', '.join(post['flags'])}")
    else:
        st.info("No major red flags present.")

    st.success(f"You earned **{round_score} / 2 points** this round.")
    st.session_state.score += round_score

# ---------------- Next Case ----------------
if st.session_state.submitted:
    if st.button("➡️ Next Case"):
        st.session_state.index += 1
        st.session_state.submitted = False
