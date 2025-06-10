import argparse

def main():
    parser = argparse.ArgumentParser(description="Cyber Hygiene Toolkit")
    parser.add_argument('--check-password', action='store_true', help="Check if a password has been leaked")
    
    args = parser.parse_args()

    if args.check_password:
        from scanners import password_checker
        password_checker.run_password_check()

if __name__ == "__main__":
    main()