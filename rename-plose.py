from pathlib import Path
from datetime import datetime
from glob import glob

# === PARAMETERS ===
directory = Path("/gws/pw/j07/ncas_obs_vol1/amf/processing/ncas-cam-12/teamx")  # <-- Change this
location = "plose"
version = "v1.0"
camera_number = "12"

# === RENAMING LOGIC ===
for file in directory.rglob("*.jpg"):
    try:
        # Get the filename without extension
        stem = file.stem

        # Expected format: "YYYY-MM-DDTHH:MM:SS-amof-cam-X"
        timestamp_str = stem.split("-amof-cam")[0]

        # Parse the timestamp
        dt = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S")

        # Construct the new filename
        new_name = (
            f"ncas-cam-{camera_number}_{location}_"
            f"{dt.strftime('%Y%m%d-%H%M%S')}_photo_{version}.jpg"
        )

        # Rename the file
        file.rename(file.with_name(new_name))
        print(f"Renamed: {file.name} -> {new_name}")

    except Exception as e:
        print(f"Skipping {file.name}: {e}")

