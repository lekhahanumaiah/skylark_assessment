from sheets import get_all_records

# ----------- Spreadsheet IDs -----------
PILOT_SHEET_ID = "1uLnm4zmPOuSah-CKnY4YFXOutmkHtwSPCA4QUxr7QbY"
DRONE_SHEET_ID = "1aM93GY9E_K1f8s0pas22BweWbfZbHwoelXya57eR_Ds"
MISSION_SHEET_ID = "1U8GKthSykmfo1hokIfAE5mWmX0kxnoMjHAEzLdM1e-M"


# ---------------- PILOT MATCH ----------------
def match_pilot(mission_id):
    pilots = get_all_records(PILOT_SHEET_ID)

    for pilot in pilots:
        if pilot.get("status", "").lower() == "available":
            return f"Pilot {pilot.get('pilot_id')} assigned to {mission_id}"

    return "No available pilot"


# ---------------- DRONE MATCH ----------------
def match_drone(mission_id):
    drones = get_all_records(DRONE_SHEET_ID)

    for drone in drones:
        if drone.get("status", "").lower() == "available":
            return f"Drone {drone.get('drone_id')} assigned to {mission_id}"

    return "No available drone"
