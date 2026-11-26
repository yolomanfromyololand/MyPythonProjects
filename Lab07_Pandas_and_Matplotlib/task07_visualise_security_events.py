# Author: Yaroslav
# Date: 2026-11-16
# Purpose: Bring Pandas and Matplotlib together: count the events in your sample with value_counts(), and show your data in one figure with two charts side by side.

import matplotlib.pyplot as plt
import pandas as pd

STUDENT_ID = 110153269
SAMPLE_SIZE = 50


# ---------- Provided code: copy as is ----------
def load_log(filename):
    try:
        log = pd.read_csv(filename)
        print("Loaded", filename, "with", log.shape[0], "events")
        return log
    except FileNotFoundError:
        print("Error: the file", filename, "was not found.")
        return None


def select_my_events(log, student_id, size):
    my_log = log.sample(n=size, random_state=student_id)
    my_log = my_log.sort_values("EventID").reset_index(drop=True)
    print("Student ID:", student_id)
    print("Events selected:", my_log.shape[0])
    print()
    return my_log
# ---------- End of provided code ----------


def build_charts(my_log, student_id, filename):
    service_counts = my_log["Service"].value_counts()
    plt.figure(figsize=(10, 4))

    # Left chart - done for you
    plt.subplot(1, 2, 1)
    plt.bar(service_counts.index, service_counts.values, color="blue")
    plt.title("Events per Service")
    plt.xlabel("Service")
    plt.ylabel("Number of events")

    # Right chart
    # 1. Select the right chart with plt.subplot(1, 2, 2)
    plt.subplot(1, 2, 2)
    # 2. Draw a red histogram of my_log["Hour"] with 6 bins and black edges
    plt.hist(my_log["Hour"], bins=6, color="red", edgecolor="black")
    # 3. Title "Events by Hour", x-axis label "Hour of day", y-axis label "Number of events"
    plt.title("Events by Hour")
    plt.xlabel("Hour of day")
    plt.ylabel("Number of events")

    # 4. Add the figure title: plt.suptitle("Firewall Events - Student " + str(student_id))
    plt.suptitle("Firewall Events - Student " + str(student_id))
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    print("Saved", filename)
    # 5. Print the most common service (use service_counts.idxmax())
    print("Most common service:", service_counts.idxmax())


def main():
    log = load_log("security_log.csv")
    if log is None:
        return
    my_log = select_my_events(log, STUDENT_ID, SAMPLE_SIZE)
    build_charts(my_log, STUDENT_ID, "security_charts.png")


main()

# HTTPS is the most common service in my sample, with 17 events.
# The busiest histogram bin contains hours 4-7, with 13 events.
# There are events in the middle of the night, including 2 at hour 0 and 2 at hour 2.
