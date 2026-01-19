#!/usr/bin/python3
import nmap
import datetime
import sys
import socket

# Try to import pyfiglet for the banner, strictly optional
try:
    import pyfiglet
    has_figlet = True
except ImportError:
    has_figlet = False

def print_banner():
    """Prints a banner using pyfiglet if available, or plain text."""
    if has_figlet:
        print(pyfiglet.figlet_format("CyArt Scanner"))
    else:
        print("=" * 75)
        print("CyArt Scanner (pyfiglet not installed)")
        print("=" * 75)
    print("=" * 75)

def resolve_target(target):
    """
    Attempts to resolve hostname to IP. 
    Returns the IP if valid, or None if invalid.
    """
    try:
        return socket.gethostbyname(target)
    except socket.gaierror:
        return None

def main():
    scanner = nmap.PortScanner()
    print_banner()

    # --- 1. Input Handling (Accepts IP OR Hostname) ---
    while True:
        target_input = input("Enter the IP or Hostname to scan: ")
        target_ip = resolve_target(target_input)
        
        if target_ip:
            print(f"[*] Target Resolved: {target_input} -> {target_ip}")
            break
        else:
            print("[-] Invalid IP or Hostname. Please try again.")

    # --- 2. Full Menu (All 7 Options) ---
    # We map keys to a tuple: (Description, Nmap Arguments)
    opt_dict = {
        "1": ("SYN Scan (-sS)", "-sS"),
        "2": ("TCP Connect Scan (-sT)", "-sT"),
        "3": ("UDP Scan (-sU)", "-sU"),
        "4": ("Service Version Detection (-sV)", "-sV"),
        "5": ("OS Detection (-O)", "-O"),
        "6": ("Vulnerability Scan (-sV -sC)", "-sV -sC"),
        "7": ("Aggressive/All Scans (-A)", "-A") 
        # Note: -A is generally better/cleaner than -sS -sT -sU combined
    }

    print("\nSelect the type of scan you want to perform:")
    for key, (desc, _) in opt_dict.items():
        print(f"{key}. {desc}")

    scan_choice = input("Enter your choice (1-7): ")

    if scan_choice not in opt_dict:
        print("Invalid choice. Exiting.")
        sys.exit()

    selected_desc, selected_args = opt_dict[scan_choice]

    # --- 3. Perform Scan ---
    print(f"\n[*] Executing {selected_desc} on {target_ip}...")
    print("[*] This might take a while depending on the scan type...")
    
    try:
        # Run the scan. sudo is often needed for -sS, -sU, -O
        scanner.scan(target_ip, arguments=selected_args)
    except nmap.PortScannerError as e:
        print(f"[-] Nmap Error: {e}")
        print("[-] Hint: Try running with 'sudo python3 nmap_automation.py'")
        sys.exit(1)
    except Exception as e:
        print(f"[-] Unexpected Error: {e}")
        sys.exit(1)

    # --- 4. Generate Report Data (Formatted Table) ---
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Check if host is actually up
    if target_ip not in scanner.all_hosts():
        print("[-] Host seems down or blocked by firewall.")
        sys.exit()

    report_lines = []
    report_lines.append("=" * 75)
    report_lines.append(f"SCAN REPORT: {selected_desc}")
    report_lines.append(f"Time: {timestamp}")
    report_lines.append(f"Target: {target_input} ({target_ip})")
    report_lines.append("-" * 75)
    report_lines.append(f"{'PORT':<10} {'STATE':<10} {'SERVICE':<15} {'VERSION'}")
    report_lines.append("-" * 75)

    # Extract Data loop
    # We loop through protocols found (tcp/udp)
    for proto in scanner[target_ip].all_protocols():
        ports = scanner[target_ip][proto].keys()
        for port in sorted(ports):
            details = scanner[target_ip][proto][port]
            
            state = details['state']
            name = details['name']
            # Combine product + version for the last column
            version = details.get('product', '') + " " + details.get('version', '')
            version = version.strip()
            if not version:
                version = "Unknown"

            line = f"{port}/{proto:<5} {state:<10} {name:<15} {version}"
            report_lines.append(line)
            print(line) # Print to console

    report_lines.append("-" * 75)
    report_lines.append("Scan completed.")

    # --- 5. Save to File ---
    filename = "scan_report.txt"
    try:
        with open(filename, "w") as f:
            f.write("\n".join(report_lines))
        print(f"\n[+] Report successfully saved to {filename}")
    except IOError as e:
        print(f"[-] Could not save file: {e}")

if __name__ == "__main__":
    main()
