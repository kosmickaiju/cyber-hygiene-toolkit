import argparse

def main():
    parser = argparse.ArgumentParser(description="Cyber Hygiene Toolkit")
    parser.add_argument('--check-password', action='store_true', help="Check if a password has been leaked")
    parser.add_argument('--scan-ports', action='store_true', help="Check for open ports on localhost")
    parser.add_argument('--summary', action='store_true', help="Run all hygiene checks and print results")
    
    args = parser.parse_args()

    if args.check_password:
        from scanners import password_checker
        password_checker.password_check()
    if args.scan_ports:
        from scanners import port_scanners
        port_scanners.run_scan()
    if args.summary:
        run_summary()

# prints results for all tests and provides suggestions on how to improve cyber hygiene - currently password checker, port scanner
def run_summary():
    from scanners import password_checker, port_scanners
    # run password check
    print(f'✰✰✰✰✰✰ Your Cyber Hygiene Summary ✰✰✰✰✰✰ \n')
    password = input("Enter your password to see if it's been pwned... ")
    count = password_checker.check_pwned_password(password)
    if count:
        print(f'Uh oh! This password has been found {count} times in data breaches.')
    else:
        print(f'Good news! This password was not found in any known breaches... yet.')
    #run port scan
    open_ports = port_scanners.run_scan()
    if open_ports:
        print(f"\n {len(open_ports)} open port(s) found: {open_ports}")
    else:
        print("\n All clear! No open ports found.")
    # print personalized suggestions based on scan results
    if count or open_ports:
        print(f'✰✰✰✰✰✰ Your Personalized Cyber Hygiene Suggestions ✰✰✰✰✰✰ \n')
        if count:
            print(f'Looks like one of your passwords got pwned! Check out this site about good password practices to avoid being pwned again: https://www.cisa.gov/secure-our-world/use-strong-passwords')
        if open_ports:
            print(f'It seems that you have a few ports open on your device. No worries though - these are all essential ports that need to be open to the Internet for you to use your computer. However, make sure that you have a firewall installed and keep your software/operating system updated to avoid potential attacks!')

if __name__ == "__main__":
    main()