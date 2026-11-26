# Author: Yaroslav
# Date: 2026-11-16
# Purpose: Practice reading a CSV file and answering simple questions about your own sample of data with head(), shape, filtering, value_counts(), a calculated column and sort_values().

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


def analyse_events(my_log):
    print("First 5 events:")
    print(my_log.head(5))                      # done for you
    print()
    # 1. Print the number of rows and columns (use .shape)
    print("Rows and columns:", my_log.shape)
    # 2. Count the blocked events: keep the rows where my_log["Action"] == "BLOCKED",
    #    store them in blocked, and print blocked.shape[0]. Then print an empty line.
    blocked = my_log[my_log["Action"] == "BLOCKED"]
    print("Blocked events:", blocked.shape[0])
    print()
    # 3. Print the number of events per service (use my_log["Service"].value_counts())
    print("Events per service:")
    print(my_log["Service"].value_counts())
    print()
    # 4. Add a column named KB with the size in kilobytes, rounded to 1 decimal place
    #    (use my_log["KB"] = (my_log["Bytes"] / 1024).round(1)). Nothing to print here.
    my_log["KB"] = (my_log["Bytes"] / 1024).round(1)
    # 5. Print the 3 largest transfers - you will see your new KB column at the end
    #    (use my_log.sort_values("Bytes", ascending=False).head(3))
    print("3 largest transfers:")
    print(my_log.sort_values("Bytes", ascending=False).head(3))


def main():
    log = load_log("security_log.csv")
    if log is None:
        return
    my_log = select_my_events(log, STUDENT_ID, SAMPLE_SIZE)
    analyse_events(my_log)


main()
