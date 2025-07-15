#!/bin/bash

DEVICE="/dev/sda1"
MOUNT_POINT="/var/www/modules" # Define your desired mount point here

# Check if the device exists
if [ -b "$DEVICE" ]; then
    echo "Device $DEVICE exists."

    # Check if the device is already mounted
    if mountpoint -q "$MOUNT_POINT"; then
        echo "$DEVICE is already mounted at $MOUNT_POINT."
    else
        echo "$DEVICE is not mounted. Attempting to mount..."
        # Create the mount point directory if it doesn't exist
        if [ ! -d "$MOUNT_POINT" ]; then
            sudo mkdir -p "$MOUNT_POINT"
            echo "Created mount point directory: $MOUNT_POINT"
        fi

        # Mount the device
        sudo mount "$DEVICE" "$MOUNT_POINT"

        # Check if the mount was successful
        if [ $? -eq 0 ]; then
            echo "$DEVICE successfully mounted at $MOUNT_POINT."
        else
            echo "Failed to mount $DEVICE."
        fi
    fi
else
    echo "Device $DEVICE does not exist."
fi
