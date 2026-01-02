import os 
import re  
import argparse
import sys 

# Scans a directory to prevent data loss or secret exposure
RULES = {
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "AWS Secret Key": r"(?i)aws(.{0,20})?['\"][0-9a-zA-Z/+]{40}['\"]",
    "Private RSA Key": r"-----BEGIN [A-Z]+ PRIVATE KEY-----",
    "Google API Key": r"AIza[0-9A-Za-z-_]{35}",
    "Email Address": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "Credit Card Number": r"\b(?:\d[ -]*?){13,16}\b"
}

def scan_file(filepath):
    # Scans a single file line-by-line for secrets
    found_secrets = []
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for line_number, line in enumerate(f, 1):
                for secret_name, regex_pattern in RULES.items():
                    if re.search(regex_pattern, line):
                        found_secrets.append(
                            f"[!] Found {secret_name} in file '{filepath}' on line {line_number}"
                        )
    except Exception as e:
        print(f"  Could not read or open this file {filepath}: {e}")
    return found_secrets

def start_scan(target_directory):
    # Recursively walks through a directory and scans valid files
    print(f"Scanning directory: {target_directory}...\n")
    all_issues = []

    for root, dirs, files in os.walk(target_directory):
        if ".git" in dirs:
            dirs.remove(".git")
            
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.exe', '.pyc', '.git')):
                continue
            full_path = os.path.join(root, filename)
            file_issues = scan_file(full_path)
            if file_issues:
                all_issues.extend(file_issues)
    return all_issues

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DevSecOps Simple Secret Scanner")
    parser.add_argument("path", help="The directory path to scan")
    args = parser.parse_args()
    
    if not os.path.exists(args.path):
        print(f"Error: The directory '{args.path}' does not exist.")
        sys.exit(1)
        
    findings = start_scan(args.path)
    
    if findings:
        print("\n" + "="*50)
        print(f"SECURITY CHECK FAILED: {len(findings)} SECRETS FOUND")
        print("="*50)
        for issue in findings:
            print(issue)
        print("\nCommit/Build Aborted due to security violations.")
        sys.exit(1)
    else:
        print("\n" + "="*50)
        print("SECURITY CHECK PASSED: No secrets found.")
        print("="*50)
        sys.exit(0)