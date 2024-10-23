#!/usr/bin/python3

#importing modules
import nmap
import pyfiglet
import ipaddress

# Creating variable
scanner = nmap.PortScanner()

# Generate the ASCII art
welcome_message = pyfiglet.figlet_format("Welcome to Nmap Scanner")
print(welcome_message)

# Create a decorative line
decorative_line = "=" * 75
print(decorative_line)

# Ask for input from the user
while True:
    ip_add = input("Enter the IP you want to scan: ")
    try:
        # Validate the IP address
        ipaddress.ip_address(ip_add)
        print("Entered IP is:", ip_add)
        break  # Exit the loop if valid
    except ValueError:
        print("Invalid IP address format. Please enter a valid IPv4 address.")

# Define scan options in a dictionary
opt_dict = {
    "1": {"description": "SYN Scan (-sS)", "arguments": "-sS"},
    "2": {"description": "TCP Connect Scan (-sT)", "arguments": "-sT"},
    "3": {"description": "UDP Scan (-sU)", "arguments": "-sU"},
    "4": {"description": "Service Version Detection (-sV)", "arguments": "-sV"},
    "5": {"description": "OS Detection (-O)", "arguments": "-O"},
    "6": {"description": "Vulnerability Scan (-sV -sC)", "arguments": "-sV -sC"},
    "7": {"description": "All Scans", "arguments": "-sS -sT -sU -sV -O -sC"},
}

# Provide options for scanning types
print("\nSelect the type of scan you want to perform:")
for key, value in opt_dict.items():
    print(f"{key}. {value['description']}")

# Get user's choice
scan_choice = input("Enter your choice (1-7): ")

# Perform the chosen scan
if scan_choice in opt_dict:
    try:
        print(f"Executing scan: nmap {opt_dict[scan_choice]['arguments']} {ip_add}")
        scanner.scan(ip_add, arguments=opt_dict[scan_choice]["arguments"])
        
        # Print scan results
        print("\nScan Results:")
        print(scanner[ip_add])
    except nmap.PortScannerError as nmap_err:
        print(f"Nmap error: {nmap_err}")  # Print the Nmap-specific error
    except Exception as e:
        print(f"An error occurred: {e}")  # General error message
else:
    print("Invalid choice. Please select a number between 1 and 7.")
