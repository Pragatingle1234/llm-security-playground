import streamlit as st

from core.logging_utils import init_state
from modules import (
    chatbot,
    data_exfiltration,
    defense,
    home,
    instruction_hijacking,
    logs_dashboard,
    prompt_injection,
    role_override,
)
from ui.theme import apply_theme


PAGES = {
    "Home Dashboard": home.render,
    "Prompt Injection Simulator": prompt_injection.render,
    "Role Override Attack Demo": role_override.render,
    "Data Exfiltration Attack Demo": data_exfiltration.render,
    "Instruction Hijacking Demo": instruction_hijacking.render,
    "Defense / Mitigation Demo": defense.render,
    "Security Logs Viewer": logs_dashboard.render,
    "Chatbot Interface": chatbot.render,
}


def render_sidebar() -> tuple[str, str]:
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Select module", list(PAGES.keys()))

    st.sidebar.markdown("---")
    mode = st.sidebar.radio(
        "Assistant Mode",
        ["Vulnerable Mode", "Protected Mode"],
        index=1,
        help="Vulnerable mode simulates insecure behavior. Protected mode applies defenses.",
    )

    st.sidebar.markdown("---")
    st.sidebar.caption("LLM Security Playground")
    st.sidebar.write("Built for attack simulation and defense validation.")
    return page, mode


def main() -> None:
    apply_theme()
    init_state()

    page, mode = render_sidebar()

    if page == "Chatbot Interface":
        PAGES[page](mode)
    else:
        PAGES[page]()


if __name__ == "__main__":
    main()
