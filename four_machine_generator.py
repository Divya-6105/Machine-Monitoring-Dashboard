import pandas as pd
import time
import random
from datetime import datetime
import os

file_path = "four_machine_data.csv"

print("IoT Sensor Monitoring System Started...")

# Create CSV if it does not exist
if not os.path.exists(file_path):

    df = pd.DataFrame(columns=[

        "Timestamp",

        "Machine1_RPM",
        "Machine1_Vibration",
        "Machine1_Temperature",

        "Machine2_RPM",
        "Machine2_Vibration",
        "Machine2_Temperature",

        "Machine3_RPM",
        "Machine3_Vibration",
        "Machine3_Temperature",

        "Machine4_RPM",
        "Machine4_Vibration",
        "Machine4_Temperature"

    ])

    df.to_csv(file_path, index=False)

while True:

    try:

        data = pd.read_csv(file_path)

        # Same RPM range
        m1_rpm = random.randint(2800,3200)
        m2_rpm = random.randint(2800,3200)
        m3_rpm = random.randint(2800,3200)
        m4_rpm = random.randint(2800,3200)

        # vibration
        m1_vib = round(random.uniform(0.2,0.8),2)
        m2_vib = round(random.uniform(1.0,1.5),2)
        m3_vib = round(random.uniform(0.3,0.9),2)
        m4_vib = round(random.uniform(1.8,2.5),2)

        # temperature
        m1_temp = random.randint(35,45)
        m2_temp = random.randint(55,70)
        m3_temp = random.randint(38,48)
        m4_temp = random.randint(80,95)

        new_row = {

            "Timestamp": datetime.now().strftime("%H:%M:%S"),

            "Machine1_RPM": m1_rpm,
            "Machine1_Vibration": m1_vib,
            "Machine1_Temperature": m1_temp,

            "Machine2_RPM": m2_rpm,
            "Machine2_Vibration": m2_vib,
            "Machine2_Temperature": m2_temp,

            "Machine3_RPM": m3_rpm,
            "Machine3_Vibration": m3_vib,
            "Machine3_Temperature": m3_temp,

            "Machine4_RPM": m4_rpm,
            "Machine4_Vibration": m4_vib,
            "Machine4_Temperature": m4_temp
        }

        data = pd.concat(
            [data, pd.DataFrame([new_row])],
            ignore_index=True
        )

        data.to_csv(file_path, index=False)

        print("Real-Time Sensor Data Captured Successfully")

    except Exception as e:

        print("Waiting for file...", e)

    time.sleep(5)