from datetime import UTC, datetime
from typing import Dict, List

import pandas as pd
import streamlit as st


def init_state() -> None:
    if "security_logs" not in st.session_state:
        st.session_state.security_logs: List[Dict[str, str]] = []
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []


def log_event(result: Dict[str, object]) -> None:
    findings = result.get("findings", []) or []

    if not findings:
        st.session_state.security_logs.append(
            {
                "timestamp": result.get(
                    "timestamp", datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z")
                ),
                "attack_type": "None",
                "prompt": result.get("prompt", ""),
                "severity": "Low",
                "mitigation_action": "No mitigation required",
                "mode": result.get("mode", "Unknown"),
                "status": "Allowed",
            }
        )
        return

    for finding in findings:
        mitigation = _mitigation_from_type(finding.get("attack_type", "Unknown"))
        st.session_state.security_logs.append(
            {
                "timestamp": result.get(
                    "timestamp", datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z")
                ),
                "attack_type": finding.get("attack_type", "Unknown"),
                "prompt": result.get("prompt", ""),
                "severity": finding.get("severity", "Medium"),
                "mitigation_action": mitigation,
                "mode": result.get("mode", "Unknown"),
                "status": "Blocked" if result.get("blocked", False) else "Allowed",
            }
        )


def logs_df() -> pd.DataFrame:
    logs = st.session_state.get("security_logs", [])
    if not logs:
        return pd.DataFrame(
            columns=[
                "timestamp",
                "attack_type",
                "prompt",
                "severity",
                "mitigation_action",
                "mode",
                "status",
            ]
        )
    return pd.DataFrame(logs)


def _mitigation_from_type(attack_type: str) -> str:
    mapping = {
        "Prompt Injection": "Denylist + pattern filter",
        "Role Override": "Role override guard",
        "Data Exfiltration": "Sensitive data access blocker",
        "Instruction Hijacking": "Instruction hierarchy enforcement",
    }
    return mapping.get(attack_type, "Generic safeguard")
