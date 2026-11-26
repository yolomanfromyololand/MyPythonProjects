# Author: Yaroslav
# Date: 2026-11-12
# Purpose: Bring everything together: read data from a file, use exception handling to survive a missing file and bad lines, raise an exception for empty data, and analyse the data with NumPy and Boolean indexing.
import numpy as np


def load_packets(filename):
    values = []
    try:
        with open(filename, "r") as file:
            for line_number, line in enumerate(file, start=1):
                text = line.strip()
                try:
                    values.append(int(text))
                except ValueError:
                    print(f"Skipping line {line_number} - not a number: {text}")
    except FileNotFoundError:
        print("Error: the file", filename, "was not found.")
    return np.array(values)


def analyse_packets(packets, threshold):
    if packets.size == 0:
        raise ValueError("No packet data to analyse")

    large_packets = packets[packets > threshold]
    print("Packets loaded:", packets)
    print("Number of packets:", packets.size)
    print("Average size:", round(np.mean(packets), 2))
    print("Largest packet:", np.max(packets))
    print("Smallest packet:", np.min(packets))
    print(f"Packets larger than {threshold} bytes:", large_packets)
    print("Count of large packets:", large_packets.size)


def main():
    for filename in ["packets.txt", "missing.txt"]:
        print(f"=== Analysing {filename} ===")
        packets = load_packets(filename)
        try:
            analyse_packets(packets, 1000)
        except ValueError as exception:
            print("Error:", str(exception))
        print()


main()
