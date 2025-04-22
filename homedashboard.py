import streamlit as st
from services.event_logger import EventLogger
from dashboard_hub import create_hub
from datetime import datetime
from collections import Counter
import pandas as pd
import altair as alt

st.set_page_config(page_title="Smart Home Dashboard", layout="wide")
st.title("🏠 Smart Home Automation Dashboard")

# --- Cache hub so it doesn't reinitialize on each rerun
@st.cache_resource
def get_hub():
    return create_hub()

hub = get_hub()
logger = EventLogger()

# --- Sensor Trigger Buttons ---
st.subheader("🚨 Simulate Sensor Activity")

col1, col2 = st.columns(2)

with col1:
    if st.button("🏃 Trigger Motion Sensor"):
        event = {
            "type": "motion",
            "location": "Living Room",
            "timestamp": datetime.now().isoformat()
        }
        hub.notify(event)
        st.success("Motion sensor triggered.")
        st.rerun()

with col2:
    if st.button("🔥 Trigger Smoke Sensor"):
        event = {
            "type": "smoke",
            "location": "Kitchen",
            "escalate": True,
            "timestamp": datetime.now().isoformat()
        }
        hub.notify(event)
        st.success("Smoke sensor triggered.")
        st.rerun()

# --- Event Log Table ---
st.subheader("📜 Event & Action Log")

logs = logger.get_events_history()

if logs:
    st.dataframe(logs, use_container_width=True)
else:
    st.info("No events logged yet.")

# --- Clear Button ---
if st.button("🗑️ Clear Log"):
    logger.clear_history()
    st.success("Event log cleared.")
    st.rerun()

# --- Alarm Control Panel ---
st.subheader("🔐 Alarm Control Panel")

alarm = hub.get_device("alarm")
status = alarm.get_status()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Status", "ARMED" if status["is_armed"] else "DISARMED")

with col2:
    st.metric("Triggered", "🚨 YES" if status["is_triggered"] else "✅ NO")

with col3:
    st.metric("Sensitivity", f'{status["sensitivity"]}/100')

# Arm/Disarm toggle
alarm_control = st.radio("Choose Alarm State:", ["Arm", "Disarm"], horizontal=True)

if alarm_control == "Arm" and not status["is_armed"]:
    alarm.arm()
    st.success("🔒 Alarm is now armed.")
    hub.event_logger.log_action("alarm", "Manually armed", {"source": "UI"})
    st.rerun()

elif alarm_control == "Disarm" and status["is_armed"]:
    alarm.disarm()
    st.success("🔓 Alarm is now disarmed.")
    hub.event_logger.log_action("alarm", "Manually disarmed", {"source": "UI"})
    st.rerun()

# Sensitivity slider
new_sensitivity = st.slider("🔧 Adjust Alarm Sensitivity", 0, 100, status["sensitivity"])

if new_sensitivity != status["sensitivity"]:
    alarm.set_sensitivity(new_sensitivity)
    st.success(f"🎚️ Sensitivity set to {new_sensitivity}")
    hub.event_logger.log_action("alarm", "Sensitivity updated", {"new_value": new_sensitivity})
    st.rerun()

# --- Event Type Analytics ---
st.subheader("📊 Event Type Breakdown")

sensor_events = [e for e in logs if "type" in e]
if sensor_events:
    type_counts = Counter(e["type"] for e in sensor_events)
    df = pd.DataFrame({
        "Event Type": list(type_counts.keys()),
        "Count": list(type_counts.values())
    })

    col1, col2 = st.columns(2)

    with col1:
        st.altair_chart(
            alt.Chart(df).mark_bar().encode(
                x="Event Type",
                y="Count",
                color="Event Type"
            ).properties(title="Sensor Event Frequency"),
            use_container_width=True
        )

    with col2:
        st.altair_chart(
            alt.Chart(df).mark_arc().encode(
                theta="Count",
                color="Event Type",
                tooltip=["Event Type", "Count"]
            ).properties(title="Sensor Event Pie Chart"),
            use_container_width=True
        )
else:
    st.info("No sensor event data to visualize.")
