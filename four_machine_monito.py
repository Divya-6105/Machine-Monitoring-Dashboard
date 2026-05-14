import pandas as pd
import matplotlib.pyplot as plt
from collections import deque
import time

file_path = "four_machine_data.csv"

history = {

    "Machine1_RPM": deque(maxlen=12),
    "Machine2_RPM": deque(maxlen=12),
    "Machine3_RPM": deque(maxlen=12),
    "Machine4_RPM": deque(maxlen=12)
}

plt.ion()

fig, axs = plt.subplots(2,2, figsize=(13,8))

fig.suptitle(
    "IoT Based Machine Health Monitoring Dashboard",
    fontsize=18
)

last_row_count = 0

print("Machine Health Monitoring System Started...")

while True:

    try:

        data = pd.read_csv(file_path)

        current_rows = len(data)

        if current_rows > last_row_count:

            row = data.iloc[-1]

            machines = [

                ("Machine1_RPM","Machine 1"),
                ("Machine2_RPM","Machine 2"),
                ("Machine3_RPM","Machine 3"),
                ("Machine4_RPM","Machine 4")
            ]

            for i,(rpm_col,name) in enumerate(machines):

                rpm = row[rpm_col]

                vibration_col = rpm_col.replace(
                    "RPM",
                    "Vibration"
                )

                temperature_col = rpm_col.replace(
                    "RPM",
                    "Temperature"
                )

                vibration = row[vibration_col]
                temperature = row[temperature_col]

                # prediction logic
                if vibration > 1.8 or temperature > 80:

                    status = "FAIL"
                    color = "red"

                elif vibration > 1.0 or temperature > 55:

                    status = "MEDIUM FAILURE"
                    color = "orange"

                else:

                    status = "WORKING GOOD"
                    color = "green"

                history[rpm_col].append(rpm)

                ax = axs[i//2][i%2]

                ax.clear()

                ax.plot(
                    history[rpm_col],
                    marker='o',
                    linewidth=3,
                    color=color
                )

                ax.set_title(

                    f"{name}\n"
                    f"Status: {status}\n"
                    f"RPM: {rpm} | "
                    f"Vibration: {vibration} | "
                    f"Temp: {temperature}°C",

                    fontsize=11
                )

                ax.set_xlabel("Time Step")
                ax.set_ylabel("RPM")

                ax.grid(True)

            plt.tight_layout(pad=3)

            plt.subplots_adjust(
                hspace=0.5,
                wspace=0.3
            )

            plt.pause(0.1)

            last_row_count = current_rows

    except Exception as e:

        print("Waiting for data...", e)

    time.sleep(2)