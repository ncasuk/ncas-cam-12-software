#!/bin/bash

# Output directory
BASE_DIR="/data/amof-cam-2"

# Create base directory if it doesn't exist
mkdir -p "$BASE_DIR"

while true; do
    # Get current date and time
    DATE=$(date +"%Y%m%d")
    TIMESTAMP=$(date +"%Y-%m-%dT%H:%M:%S")

    # Create daily folder if it doesn't exist
    DAY_DIR="$BASE_DIR/$DATE"
    mkdir -p "$DAY_DIR"

    # Set image filename
    IMAGE_FILE="$DAY_DIR/$TIMESTAMP-amof-cam-2.jpg"

    # Capture image
    gphoto2 --capture-image-and-download --filename "$IMAGE_FILE"
    chown -R root:lecjlg /data/amof-cam-2
    chmod -R g+wr /data/amof-cam-2

    echo "Captured: $IMAGE_FILE"

    # Wait 5 seconds
    sleep 30
done

