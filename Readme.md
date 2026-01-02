# PyShield: Automated Secret Scanner

## Overview
PyShield is a lightweight Static Application Security Testing (SAST) tool written in Python. It recursively scans a local directory structure to detect hardcoded secrets, API keys, and sensitive credentials before they are pushed to a version control system.

This tool is designed for DevSecOps workflows, using proper exit codes to integrate with CI/CD pipelines and Git hooks.

## Key Features
* **Zero Dependencies:** Runs using only the Python standard library (os, re, sys, argparse).
* **Recursive Scanning:** Automatically walks through the entire directory tree.
* **Smart Filtering:** Automatically ignores .git directories, images, and binary files to reduce false positives.
* **Exit Codes:** Returns Exit Code 1 if secrets are found (breaking the build) and Exit Code 0 if clean.
* **Line-Level Reporting:** Precise output showing the file path and line number where the secret was detected.

## Supported Signatures
The scanner uses Regular Expressions to detect the following patterns:
* AWS Access Keys (AKIA...)
* AWS Secret Keys
* Google API Keys
* Private RSA Keys
* Hardcoded Email Addresses
* Credit Card Numbers

## Prerequisites
* Python 3.x
* No external libraries (pip install) are required.

## Usage

### 1. Clone the repository
```bash
 git clone https://github.com/ChiefYasser/Pyshiled.git
cd pyshield

 
2. Run the scanner
You can point the scanner at any directory. To scan the current directory, use a dot (.):
python scanner.py .
To scan a specific project folder:
python scanner.py /path/to/my/project