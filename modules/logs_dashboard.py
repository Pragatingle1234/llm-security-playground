import pandas as pd
import streamlit as st

from core.logging_utils import logs_df


def render() -> None:
    st.subheader("SOC Security Logs Dashboard")

    df = logs_df()
    if df.empty:
        st.info("No security events yet. Run simulations to populate the dashboard.")
        return

    total = len(df)
    blocked = int((df["status"] == "Blocked").sum())
    critical = int((df["severity"] == "Critical").sum())

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Events", total)
    c2.metric("Blocked Attacks", blocked)
    c3.metric("Critical Events", critical)

    attack_filter = st.multiselect(
        "Filter by attack type",
        options=sorted(df["attack_type"].unique().tolist()),
        default=sorted(df["attack_type"].unique().tolist()),
    )

    severity_filter = st.multiselect(
        "Filter by severity",
        options=["Low", "Medium", "High", "Critical"],
        default=["Low", "Medium", "High", "Critical"],
    )

    filtered = df[df["attack_type"].isin(attack_filter)] if attack_filter else df
    filtered = filtered[filtered["severity"].isin(severity_filter)] if severity_filter else filtered

    csv_data = filtered.to_csv(index=False).encode("utf-8")
    json_data = filtered.to_json(orient="records", indent=2).encode("utf-8")

    d1, d2 = st.columns(2)
    with d1:
        st.download_button(
            label="Export Logs as CSV",
            data=csv_data,
            file_name="security_logs.csv",
            mime="text/csv",
            width="stretch",
        )
    with d2:
        st.download_button(
            label="Export Logs as JSON",
            data=json_data,
            file_name="security_logs.json",
            mime="application/json",
            width="stretch",
        )

    st.markdown("### Attack Attempts")
    st.dataframe(filtered, width="stretch")

    st.markdown("### Event Distribution")
    sev_counts = filtered["severity"].value_counts().reindex(
        ["Low", "Medium", "High", "Critical"], fill_value=0
    )
    st.bar_chart(sev_counts)

    attack_counts = filtered["attack_type"].value_counts()
    st.bar_chart(attack_counts)

    # Keep timestamp sort stable when mixed events are added quickly.
    filtered_with_time = filtered.copy()
    filtered_with_time["ts"] = pd.to_datetime(filtered_with_time["timestamp"], errors="coerce")
    filtered_with_time = filtered_with_time.sort_values("ts")

    if not filtered_with_time.empty:
        timeline = filtered_with_time.set_index("ts").resample("1min").size()
        st.markdown("### Event Timeline")
        st.line_chart(timeline)
