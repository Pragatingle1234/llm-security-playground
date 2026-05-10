import streamlit as st


def apply_theme() -> None:
    st.set_page_config(
        page_title="LLM Prompt Injection Security Playground",
        page_icon="🛡️",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=JetBrains+Mono:wght@400;600&display=swap');

            :root {
                --bg: #060b13;
                --panel: rgba(14, 24, 40, 0.86);
                --panel-soft: rgba(18, 31, 52, 0.72);
                --text: #eaf2ff;
                --muted: #8ea7c3;
                --accent: #26d0ce;
                --accent-2: #1a83ff;
                --danger: #ff6b6b;
                --warn: #ffb454;
                --ok: #53e08d;
            }

            html, body, [class*="css"] {
                font-family: 'Space Grotesk', sans-serif;
                color: var(--text);
            }

            .stApp {
                background:
                    radial-gradient(circle at 10% 10%, rgba(38, 208, 206, 0.16), transparent 34%),
                    radial-gradient(circle at 85% 20%, rgba(26, 131, 255, 0.18), transparent 38%),
                    linear-gradient(145deg, #050912 0%, #0a1525 50%, #071020 100%);
            }

            [data-testid="stSidebar"] {
                background: linear-gradient(180deg, rgba(8,16,28,.95) 0%, rgba(10,22,39,.95) 100%);
                border-right: 1px solid rgba(84, 124, 171, 0.25);
            }

            .soc-card {
                background: var(--panel);
                border: 1px solid rgba(105, 145, 195, 0.24);
                border-radius: 14px;
                padding: 16px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
                backdrop-filter: blur(8px);
            }

            .kpi {
                font-size: 0.9rem;
                color: var(--muted);
                margin-bottom: 6px;
                text-transform: uppercase;
                letter-spacing: 0.08em;
            }

            .kpi-value {
                font-size: 1.8rem;
                font-weight: 700;
                color: var(--text);
                line-height: 1;
            }

            .severity-low { color: #8fe3ff; }
            .severity-medium { color: var(--warn); }
            .severity-high { color: #ff8d66; }
            .severity-critical { color: var(--danger); font-weight: 700; }

            .tiny {
                color: var(--muted);
                font-size: 0.85rem;
            }

            .stButton>button {
                border-radius: 10px;
                border: 1px solid rgba(140, 178, 221, 0.35);
                background: linear-gradient(135deg, rgba(33, 73, 132, 0.65), rgba(24, 115, 153, 0.65));
                color: #f4f8ff;
                font-weight: 600;
            }

            .stTextInput>div>div>input,
            .stTextArea textarea {
                background: rgba(8, 18, 33, 0.88);
                border: 1px solid rgba(90, 132, 181, 0.35);
                color: var(--text);
            }

            [data-testid="stMetric"] {
                background: var(--panel-soft);
                border: 1px solid rgba(95, 135, 182, 0.25);
                border-radius: 12px;
                padding: 12px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
