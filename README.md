# nmap-scanner
The Python Nmap Scanner is a command-line tool designed for network reconnaissance and security assessment. Leveraging the power of the Nmap (Network Mapper) tool, this Python script allows users to scan target hosts, discover open ports, and gather valuable information about the services running on those ports. 

# Nmap Scanner Tool

Welcome to the Nmap Scanner Tool! This Python-based tool allows you to perform various network scans using Nmap. It's designed to be user-friendly and easy to use on Linux devices.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

## Features

- Perform different types of scans (SYN, TCP Connect, UDP, etc.)
- Service version detection and OS detection
- Easy-to-use interface with input validation
- ASCII art welcome message

## Requirements

To run this tool, you need:

- Python 3.x
- Nmap installed on your system
- Required Python packages:
  - `python-nmap`
  - `pyfiglet`

## Installation

Follow these steps to set up the Nmap Scanner Tool on your Linux device:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/nmap-scanner.git
   cd nmap-scanner
2. **Install Required Packages**: 
   You can install the required Python packages using pip. If you don't have pip installed, install it first.
    ```bash
    sudo apt install python3-pip   
    pip3 install python-nmap pyfiglet
3. **Install Nmap**:
 If Nmap is not installed, you can install it using:
    ```bash
    sudo apt install nmap

## Usage
Run the Tool: You can run the tool using Python:
    ```bash
    sudo python3 nmapScanner.py

## EXAMPLE OUTPUT:
  __     __            _                      _____                     _                     
  \ \   / /           | |                    / ____|                   | |                    
   \ \_/ /__  _   _ __| |_ __ _ _ __ ___    | (___  _ __   ___ _ __ __| | ___ _ __ ___  ___  
    \   / _ \| | | / _` | '__| '_ ` _ \    \___ \| '_ \ / _ \ '__/ _` |/ _ \ '__/ __|/ _ \ 
     | | (_) | |_| | (_| | |  | | | | | |   ____) | | | |  __/ | | (_| |  __/ |  \__ \  __/ 
     |_|\___/ \__,_|\__,_|_|  |_| |_| |_|  |_____/|_| |_|\___|_|  \__,_|\___|_|  |___/\___| 

==========================================================================

Enter the IP(s) you want to scan (comma-separated for multiple, or CIDR): 192.168.1.1
Entered IP(s): ['192.168.1.1']

Select the type of scan you want to perform:
1. SYN Scan (-sS)
2. TCP Connect Scan (-sT)
3. UDP Scan (-sU)
4. Service Version Detection (-sV)
5. OS Detection (-O)
6. Vulnerability Scan (-sV -sC)
7. All Scans (-sS -sT -sU -sV -O -sC)

Enter your choice (1-7): 4
Executing scan: nmap -sV 192.168.1.1

Scan Results for 192.168.1.1
{'tcp': {22: {'state': 'open', 'name': 'ssh', 'product': 'OpenSSH',
              'version': '7.6p1 Ubuntu 4'}, 
          80: {'state': 'open', 'name': 'http', 'product': 'nginx',
               'version': '1.14.0'}}}

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

