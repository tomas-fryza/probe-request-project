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

print(f"Number of probe requests: {len(df):,}")

# Print basic information about a DataFrame
print(df.info())

# Print all columns of the first 5 lines of dataframe
pd.set_option('display.max_columns', None)
print(df.head())
```

## Dataset structure

The dataset consists of the following columns:

| **Name**     | **Description**                              |
|:-------------|:---------------------------------------------|
| `datetime`   | Timestamp                                    |
| `dst`        | Destination MAC                              |
| `src`        | *Source MAC                                  |
| `src_vendor` | Source vendor name                           |
| `randomized` | Randomized MAC?                              |
| `rssi`       | Received Signal Strength Indicator           |
| `idx`        | Index of received probe-request in PCAP file |
| `seq_num`    | Sequence number                              |
| `ch_freq`    | Frequency channel                            |
| `FCfield`    | Frame Control field                          |
| `ssid`       | *Service Set Identifier (Wi-Fi name)         |
| `dot11elt`   | Scapy layer according to IEEE 802.11         |
| `oui`        | Organization Unique Identifier               |
| `occupancy`  | Number of individuals present in the lab     |

*The `ssid` and a portion of the `src` MAC addresses were anonymized.

## Anonymized MACs

In the lab, there are several All-in-One computers with Wi-Fi. The following list of anonymized MACs must be removed from the dataset within the pre-processing operations.

```bash
dc:fb:48:68:be:e4
dc:fb:48:8c:71:fc
dc:fb:48:2a:52:e0
dc:fb:48:f5:c6:c2
dc:fb:48:e3:ab:78
dc:fb:48:00:51:90
dc:fb:48:75:d8:42
dc:fb:48:de:86:8d
dc:fb:48:dd:c6:0b
dc:fb:48:55:d5:78
dc:fb:48:c2:1d:64
40:ec:99:f9:34:a6
40:ec:99:8e:3f:63
40:ec:99:1f:3e:75
```
