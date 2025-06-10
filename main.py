import argparse

def main():
    parser = argparse.ArgumentParser(description="Cyber Hygiene Toolkit")
    parser.add_argument('--check-password', action='store_true', help="Check if a password has been leaked")
    parser.add_argument('--scan-ports', action='store_true', help="Check for open ports")
    
    args = parser.parse_args()

    if args.check_password:
        from scanners import password_checker
        password_checker.password_check()
    if args.scan_ports:
        from scanners import port_scanners
        port_scanners.port_scan()
        
if __name__ == "__main__":
    main()