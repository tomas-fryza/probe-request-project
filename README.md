# Probe request project

Wi-Fi probe requests collected in lab `sc6-61` at Brno Univ. of Technology and stored in both, CSV and PCAP (compatible with [Wireshark](https://www.wireshark.org/) or Python [Scapy](https://scapy.readthedocs.io/en/latest/index.html)) files. The two [simple sniffers](https://gitlab.com/tbravenec/esp32-probe-sniffer) of probe pequests using ESP32 as a networking device with connected SD card as a storage were used at `position_1` and `position_2`.

To work with PCAP files in Python, install the latest version of Scapy:

```bash
pip3 install scapy
```

To read a csv file in Python:

```python
import pandas as pd

df = pd.read_csv(<filename.csv>, sep=";", decimal=".")

# Print basic information about a DataFrame
print(df.info())

# Print all columns of the first 5 lines of dataframe
pd.set_option('display.max_columns', None)
print(df.head())

print(f"Number of probe requests: {len(df):,}")
```

The dataset consists of the following columns:

```csv
datetime;dst;src;src_vendor;randomized;rssi;idx;seq_num;ch_freq;FCfield;ssid;dot11elt;oui;occupancy
```

The `ssid` and a portion of the `src` MAC addresses were anonymized. The final column, `occupancy`, contains the number of individuals present in the laboratory.
