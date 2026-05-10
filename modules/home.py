import streamlit as st

from core.logging_utils import logs_df


def render() -> None:
    st.title("LLM Prompt Injection Security Playground")
    st.caption("Simulate adversarial prompts against LLM workflows and observe mitigations in real time.")

    df = logs_df()
    total_events = len(df)
    blocked = int((df["status"] == "Blocked").sum()) if total_events else 0
    critical = int((df["severity"] == "Critical").sum()) if total_events else 0

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            f"<div class='soc-card'><div class='kpi'>Total Events</div><div class='kpi-value'>{total_events}</div></div>",
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            f"<div class='soc-card'><div class='kpi'>Blocked Attempts</div><div class='kpi-value'>{blocked}</div></div>",
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            f"<div class='soc-card'><div class='kpi'>Critical Findings</div><div class='kpi-value'>{critical}</div></div>",
            unsafe_allow_html=True,
        )

    st.markdown("### Attack Simulation Modules")
    st.markdown(
        """
        - Prompt Injection Simulator
        - Role Override Attack Demo
        - Data Exfiltration Attack Demo
        - Instruction Hijacking Demo
        - Defense / Mitigation Console
        - SOC-style Security Logs Viewer
        """
    )

    st.info(
        "Use the sidebar to switch between Vulnerable Mode and Protected Mode, then test attack prompts "
        "across modules to compare outcomes."
    )
