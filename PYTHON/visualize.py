try:
    import pandas as pd
    import matplotlib.pyplot as plt
except ImportError as e:
    print(f"[!] ImportError: {e}")
    raise SystemExit(1)


def display_probes(filenames, rssi_thr, interval="10min"):
    """Read .csv file(s) and display the number of all Probe Requests in time

    Read .csv file(s) and display the number of Probe Requests below the RSSI
    threshold, accumulated per time interval.

    :param filenames:  Input .csv file(s)
    :param rssi_thr:   Signal strength threshold
    :param interval:   Time interval in minutes, e.g. 10min

    :type filenames:   list
    :type rssi_thr:    int
    :type interval:    str

    :return:           None
    """
    print("")  # New line only
    print(f"Read input file(s): {filenames}")

    # Load .csv file into a DataFrame
    csv_files1 = [f"../DATA/sc6-61/_CSV/position_1/{x}" for x in filenames]
    csv_files2 = [f"../DATA/sc6-61/_CSV/position_2/{x}" for x in filenames]
    df1 = pd.concat(
        (pd.read_csv(x, sep=";", decimal=".") for x in csv_files1),
        ignore_index=True)
    df2 = pd.concat(
        (pd.read_csv(x, sep=";", decimal=".") for x in csv_files2),
        ignore_index=True)
    # df1 = pd.read_csv(csv_file1, sep=";", decimal=".")
    # df2 = pd.read_csv(csv_file2, sep=";", decimal=".")

    # Convert timestamp to pandas datetime object
    df1["datetime"] = pd.to_datetime(df1["datetime"])
    df2["datetime"] = pd.to_datetime(df2["datetime"])
    print(f"Number of probe requests @ position1: {len(df1):,}, position2: {len(df2):,}")

    # Filter low RSSI values
    print(f"Remove data with RSSI < {rssi_thr} dBm... ", end="")
    df1 = df1[df1["rssi"] >= rssi_thr].reset_index(drop=True)
    df2 = df2[df2["rssi"] >= rssi_thr].reset_index(drop=True)
    print("Done")
    print(f"Number of probe requests @ position1: {len(df1):,}, position2: {len(df2):,}")

    # Group data by intervals
    print(f"Create groups of {interval}... ", end="")
    df_grp1 = df1.groupby(
        pd.Grouper(key="datetime", freq=interval)).size().reset_index(name="count")
    df_grp2 = df2.groupby(
        pd.Grouper(key="datetime", freq=interval)).size().reset_index(name="count")
    print("Done")

    print(f"Number of groups @ position1: {len(df_grp1):,}, position2: {len(df_grp2):,}")

    # Figure size
    plt.figure(figsize=(12, 6), dpi=90, facecolor="white")

    # Plot values
    plt.plot(df_grp1["datetime"], df_grp1["count"], label="position 1")
    plt.plot(df_grp2["datetime"], df_grp2["count"], label="position 2")
    plt.plot(df1["datetime"], df1["occupancy"], label="truth")

    plt.title(f"RSSI > {str(rssi_thr)} dBm")
    plt.xlabel("datetime")
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
    filenames = [
        "sc6-61_2024-03-13_ver-99.csv",
        "sc6-61_2024-03-14_ver-99.csv",
        "sc6-61_2024-03-15_ver-99.csv",
        "sc6-61_2024-03-16_ver-99.csv",
        "sc6-61_2024-03-17_ver-99.csv",
    ]
    display_probes(filenames, rssi_thr=-80, interval="2min")


if __name__ == "__main__":
    main()
