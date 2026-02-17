def is_available(record):
    if "status" not in record:
        return False

    return record["status"].strip().lower() == "idle"
