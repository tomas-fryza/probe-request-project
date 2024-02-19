# Probe request project

Wi-Fi probe requests collected in lab `sc6-61` at Brno Univ. of Technology and stored in both, CSV and PCAP (compatible with Wireshark or Scapy) files. The two [simple sniffers](https://gitlab.com/tbravenec/esp32-probe-sniffer) of probe pequests using ESP32 as a networking device with connected SD card as a storage were used at `position_1` and `position_2`.

The dataset consists of the following columns:

```csv
datetime;dst;src;src_vendor;randomized;rssi;idx;seq_num;ch_freq;FCfield;ssid;dot11elt;oui;truth
```

The `ssid` and a portion of the `src` MAC addresses were anonymized. The final column, `truth`, contains the number of individuals present in the laboratory.
