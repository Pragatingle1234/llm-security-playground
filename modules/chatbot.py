import streamlit as st

from core.engine import evaluate_prompt
from core.logging_utils import log_event


def render(mode: str) -> None:
    st.subheader("Simulated LLM Chatbot")
    st.caption("Use this interface to test normal prompts and prompt injection attempts.")

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Try a safe or malicious prompt...")
    if not user_input:
        return

    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    result = evaluate_prompt(user_input, mode)
    log_event(result)

    with st.chat_message("assistant"):
        st.markdown(result["response"])
        st.caption(f"Mode: {mode} | Severity: {result['severity']} | Blocked: {result['blocked']}")

    st.session_state.chat_history.append(
        {
            "role": "assistant",
            "content": result["response"],
        }
    )
