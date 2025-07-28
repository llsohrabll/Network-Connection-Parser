Network Connection Parser
Overview
This script detects active TCP network connections on your system, filters out local or non-established connections, and exports the parsed data into CSV files for further analysis or visualization. It supports Windows, Linux, and macOS.

The output includes two files:

NODE.csv: List of unique IP addresses involved in connections, flagged as internal or external.

EDGE.csv: Details of connections between IPs, including protocol and connection type.

Features
Automatically detects the operating system and uses the appropriate network command:

netstat -ano on Windows

ss -ant on Linux/macOS

Filters for established TCP connections only

Parses source and destination IPs, ignoring localhost and unspecified addresses

Identifies whether IPs are internal (private ranges) or external

Outputs results into structured CSV files for use in graphing tools or further processing

Output Files
data/connections.txt: Raw filtered output from netstat or ss

NODE.csv: List of unique nodes (IP addresses), with a flag indicating whether each is internal

EDGE.csv: Directed edges showing which IPs are connected, the protocol used, and metadata for graphing

Usage
Clone the repository or copy the script locally.

Run the script using Python 3:

bash
Copy
Edit
python script.py
After execution, the following files will be generated in the same directory:

data/connections.txt

NODE.csv

EDGE.csv

Dependencies
This script uses only standard Python libraries:

subprocess

platform

os

No external packages are required.

Notes
The script excludes connections to/from 127.0.0.1 and 0.0.0.0.

Private IP ranges are flagged as internal:

10.0.0.0/8

172.16.0.0/12

192.168.0.0/16

Ensure Python has permission to run netstat or ss depending on your system.
