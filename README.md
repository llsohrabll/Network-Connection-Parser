# Network Connection Parser

## Overview

This Python script detects active TCP network connections on your machine, filters out non-established or local-only connections, and exports the results to CSV files for further analysis or visualization.

It supports Windows, Linux, and macOS systems.

## Features

- OS-aware command execution:
  - Uses `netstat -ano` on Windows
  - Uses `ss -ant` on Linux and macOS
- Filters for established TCP connections only
- Identifies internal (private) vs external IP addresses
- Outputs structured data into:
  - `NODE.csv` (list of unique IP addresses)
  - `EDGE.csv` (network connections between IPs)

## Output Files

| File Name              | Description |
|------------------------|-------------|
| `data/connections.txt` | Raw output of filtered TCP connections |
| `NODE.csv`             | List of unique IPs labeled as internal or external |
| `EDGE.csv`             | Detailed edges with source, target, protocol, and metadata |

## Usage

1. Ensure you have Python 3 installed.
2. Clone this repository or download the script file.
3. Run the script from your terminal:

   ```bash
   python script.py

After execution, the following files will be created:

data/connections.txt
NODE.csv
EDGE.csv
