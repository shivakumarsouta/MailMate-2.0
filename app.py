import streamlit as st
from agents.email_agent import (
    summarize_email,
    generate_subject_line,
    generate_email_response,
)
from utils.email_sender import send_email

st.set_page_config(page_title="MailMate 2.0", page_icon= "favicon.ico", layout="wide")
st.title("📨 MailMate 2.0: AI Powered Email Assistant")

st.markdown("""
<style>
textarea {
    resize: none !important;
    height: 250px !important;
    width: 550px !important;
    overflow-y: auto !important;
}
</style>
""", unsafe_allow_html=True)

# ---- Session State ----
for key in ["summary", "draft_reply", "draft_subject", "email_analyzed", "email_sent"]:
    if key not in st.session_state:
        st.session_state[key] = ""

col1, col2 = st.columns(2)
with col1:
    # ---- Input Email ----
    st.subheader("Incoming Email")
    email_text = st.text_area("Paste the email you want to reply here 👇🏻:")

with col2:
    # ---- Additional Settings ----
    st.subheader("Response Settings")

    recipient = st.text_input("Recipient Email")
    tone = st.selectbox("Tone", ["Professional", "Friendly", "Apologetic", "Persuasive"])
    length = st.selectbox("Reply Length", ["Short", "Medium", "Long"])

    auto_subject = st.checkbox("Auto-generate subject", value=True)

st.markdown("---")

col11, col12 = st.columns(2)
with col11:
    if st.button("🔍 Summarize Email"):
        if not email_text.strip():
            st.warning("Please paste the email first.")
        else:
            with st.spinner("Analyzing..."):
                st.session_state.summary = summarize_email(email_text)
                st.session_state.email_analyzed = True

    if st.session_state.summary:
        st.success("Email analyzed successfully!")
        st.write("### 📌 Summary:")
        st.markdown(st.session_state.summary)
with col12:
    # ---- Generate Reply ----
    if st.button("💡 Generate Reply"):
        if not email_text.strip():
            st.warning("Paste the incoming email first.")
        elif not recipient:
            st.warning("Enter recipient email.")
        else:
            with st.spinner("Generating reply..."):
                st.session_state.draft_reply = generate_email_response(
                    email_text, tone, length
                )
                if auto_subject:
                    st.session_state.draft_subject = generate_subject_line(email_text, tone)

    # ---- Edit & Send ----
    if st.session_state.draft_reply:
        st.success("Reply generated successfully!")
        st.subheader("✍🏻 Review and Send")

        subject_input = st.text_input(
            "📌 Subject", value=st.session_state.draft_subject or "Response to your email"
        )
        body_input = st.text_area(
            "Email draft:", value=st.session_state.draft_reply, height=220
        )

        colA, colB, colC = st.columns([2, 3, 2])

        with colA:
            if st.button("📧 Send Email"):
                with st.spinner("Sending..."):
                    if send_email(recipient, subject_input, body_input):
                        st.session_state.email_sent = True
                        st.balloons()
                        st.session_state.summary = ""
                        st.session_state.draft_reply = ""
                        st.session_state.draft_subject = ""

        with colC:
            if st.button("🗑️ Discard Draft"):
                st.session_state.draft_reply = ""
                st.session_state.summary = ""
                st.session_state.email_sent = False
                st.success("Draft removed.")

        if st.session_state.get("email_sent"):
            st.success("Email sent successfully! 🎉")