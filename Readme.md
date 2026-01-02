PyShield: Automated Secret Scanner
Category	Project Details
Project Name	PyShield (Simple Static Analysis Tool)
Description	A lightweight, Python-based Static Application Security Testing (SAST) tool designed to detect hardcoded secrets, API keys, and credentials in local directories before they are pushed to version control.
Language	Python 3.x (Standard Library only: os, re, argparse, sys)
DevSecOps Value	Shift-Left Security: Catch vulnerabilities locally.<br>CI/CD Ready: Uses exit codes to break builds on failure.<br>Automation: Can be used as a Git Pre-Commit Hook.
Key Features	• Recursive Scanning: Walks through all sub-directories.<br>• Smart Filtering: Ignores .git folders, images, and binaries.<br>• Regex Engine: Detects AWS Keys, Google Keys, RSA Keys, and generic passwords.<br>• Line-Level Reporting: Identifies exactly which file and line number failed.
<br>
Usage & Configuration	Instructions
Prerequisites	You only need Python installed. No external pip packages required.<br>python --version
How to Run	Run the script targeting a specific folder (or . for current dir):<br>python scanner.py /path/to/project
Example Output	If Secrets Found (Exit Code 1):<br>SECURITY CHECK FAILED: 2 SECRETS FOUND<br>[!] Found AWS Access Key in file './config.py' on line 12<br>Commit/Build Aborted due to security violations.<br><br>If Clean (Exit Code 0):<br>SECURITY CHECK PASSED: No secrets found.
Supported Patterns	The tool currently detects:<br>• AWS Access Keys (AKIA...)<br>• AWS Secret Keys<br>• Google API Keys<br>• Private RSA Keys<br>• Hardcoded Emails & Credit Card numbers
<br>
Integration (DevSecOps)	Setup Guide
Git Pre-Commit Hook	To run this automatically before every commit, add this to .git/hooks/pre-commit:<br>#!/bin/sh<br>python scanner.py .<br>if [ $? -ne 0 ]; then<br>echo "Security Check Failed."<br>exit 1<br>fi
CI/CD Pipeline	Can be added as a step in GitHub Actions or Jenkins:<br>- name: Run Secret Scanner<br>run: python scanner.py .