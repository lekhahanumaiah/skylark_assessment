from streamlit_autorefresh import st_autorefresh
import streamlit as st
from sheets import get_all_records
from coordinator import match_pilot, match_drone


# -------------------- Page Config --------------------
st.set_page_config(
    page_title="Skylark Drone Agent",
    layout="centered"
)

st.title("🚁 Skylark Drone Operations AI Agent")


# -------------------- Auto Refresh --------------------
st_autorefresh(interval=30000, key="dashboard_refresh")
st.caption("Auto-refreshes every 30 seconds")


# -------------------- Dashboard --------------------
st.markdown("## 📊 Live Operations Dashboard")

try:
    # ----------- Spreadsheet IDs -----------
    PILOT_SHEET_ID = "1uLnm4zmPOuSah-CKnY4YFXOutmkHtwSPCA4QUxr7QbY"
    DRONE_SHEET_ID = "1aM93GY9E_K1f8s0pas22BweWbfZbHwoelXya57eR_Ds"
    MISSION_SHEET_ID = "1U8GKthSykmfo1hokIfAE5mWmX0kxnoMjHAEzLdM1e-M"

    # ----------- Fetch Data -----------
    pilots = get_all_records(PILOT_SHEET_ID)
    drones = get_all_records(DRONE_SHEET_ID)
    missions = get_all_records(MISSION_SHEET_ID)

    # ----------- Debug Data (optional) -----------
    st.subheader("🔍 Debug Data")
    st.write("Pilots:", pilots)
    st.write("Drones:", drones)
    st.write("Missions:", missions)

    # -------------------- Pilot Counts --------------------
    pilot_available = sum(
        1 for p in pilots
        if p.get("status", "").strip().lower() == "available"
    )

    pilot_assigned = sum(
        1 for p in pilots
        if p.get("status", "").strip().lower() == "assigned"
    )

    # -------------------- Drone Counts --------------------
    drone_available = sum(
        1 for d in drones
        if d.get("status", "").strip().lower() == "available"
    )

    drone_assigned = sum(
        1 for d in drones
        if d.get("status", "").strip().lower() == "assigned"
    )

    # -------------------- Mission Counts --------------------
    urgent_priority = sum(
        1 for m in missions
        if m.get("priority", "").strip().lower() == "urgent"
    )

    high_priority = sum(
        1 for m in missions
        if m.get("priority", "").strip().lower() == "high"
    )

    standard_priority = sum(
        1 for m in missions
        if m.get("priority", "").strip().lower() == "standard"
    )

    # -------------------- Metrics Layout --------------------
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("👨‍✈️ Available Pilots", pilot_available)
        st.metric("👨‍✈️ Assigned Pilots", pilot_assigned)

    with col2:
        st.metric("🚁 Available Drones", drone_available)
        st.metric("🚁 Assigned Drones", drone_assigned)

    with col3:
        st.metric("🔴 Urgent Missions", urgent_priority)
        st.metric("🟠 High Priority", high_priority)
        st.metric("🟢 Standard", standard_priority)

except Exception as e:
    st.error("Dashboard failed to load")
    st.exception(e)


# -------------------- Command Section --------------------
st.markdown("### 🎯 Assign Resources")
st.markdown("Examples:")
st.markdown("- Assign pilot PRJ001")
st.markdown("- Assign drone PRJ001")

command = st.text_input("Enter Command")

if command:
    command_lower = command.lower().strip()

    try:
        if "assign pilot" in command_lower:
            mission_id = command.split()[-1]
            result = match_pilot(mission_id)
            st.success(result)

        elif "assign drone" in command_lower:
            mission_id = command.split()[-1]
            result = match_drone(mission_id)
            st.success(result)

        else:
            st.error("Invalid command format. Use: Assign pilot PRJ001")

    except Exception as e:
        st.error("Assignment failed")
        st.exception(e)
