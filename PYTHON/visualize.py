try:
    import pandas as pd
    import matplotlib.pyplot as plt
except ImportError as e:
    print(f"[!] ImportError: {e}")
    raise SystemExit(1)


def display_probes(filename, rssi_thr, interval="10min"):
    """Read .csv file and display the number of all Probe Requests in time

    Read .csv file and display the number of Probe Requests below the RSSI
    threshold, accumulated per time interval.

    :param filename:  Input .csv file
    :param rssi_thr:  Signal strength threshold
    :param interval:  Time interval in minutes, e.g. 10min

    :type filename:   str
    :type rssi_thr:   int
    :type interval:   str

    :return:          None
    """
    print("")  # New line only
    print(f"Read input file(s): {filename}")
    print(f"RSSI threshold: {rssi_thr} dBm")
    print(f"Create groups of {interval}... ", end="")

    csv_file1 = "../DATA/sc6-61/_CSV/position_1/"+filename
    csv_file2 = "../DATA/sc6-61/_CSV/position_2/"+filename

    # Load .csv file into a DataFrame
    df1 = pd.read_csv(csv_file1, sep=";", decimal=".")
    df2 = pd.read_csv(csv_file2, sep=";", decimal=".")

    # Convert timestamp to pandas datetime object
    df1["datetime"] = pd.to_datetime(df1["datetime"])
    df2["datetime"] = pd.to_datetime(df2["datetime"])

    # Group data by intervals and filter low RSSI values
    df_grp1 = df1[df1["rssi"] >= rssi_thr].groupby(
        pd.Grouper(key="datetime", freq=interval)).size().reset_index(name="count")
    df_grp2 = df2[df2["rssi"] >= rssi_thr].groupby(
        pd.Grouper(key="datetime", freq=interval)).size().reset_index(name="count")

    # Drop intervals with zero probe requests
    df_grp1 = (df_grp1.loc[df_grp1["count"] > 0]).reset_index(drop=True)
    df_grp2 = (df_grp2.loc[df_grp2["count"] > 0]).reset_index(drop=True)
    print("Done")

    # Figure size
    plt.figure(figsize=(12, 6), dpi=90, facecolor="white")

    # Plot values
    x1 = list(df_grp1.index.values)
    x2 = list(df_grp2.index.values)
    plt.plot(x1, df_grp1["count"], label="position 1")
    plt.plot(x2, df_grp2["count"], label="position 2")

    plt.title(f"Filename: {filename}, RSSI > {str(rssi_thr)} dBm")
    plt.xlabel("n [-]")
    plt.ylabel(f"Captured Probe Requests [PR/{interval}]")

    # Grid and legend
    plt.grid(axis="both", linestyle="--", alpha=.5)
    plt.legend()
    plt.tight_layout()

    # Save current figure to PNG
    print("Save figure to png file... ", end="")
    plt.savefig("Results/probe_density.png", bbox_inches="tight")
    print("Done")

    # Display open figure(s)
    plt.show()


def main():
    filename = "sc6-61_2024-03-14_ver-99.csv"
    display_probes(filename, rssi_thr=-88, interval="10min")


if __name__ == "__main__":
    main()
