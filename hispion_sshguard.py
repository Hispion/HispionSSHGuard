#!/usr/bin/env python3
"""
HispionSSHGuard
A lightweight SSH configuration auditor by hispion.

This tool checks the SSH daemon configuration file for common security settings.
"""

import sys
import argparse

# Define the required configuration settings and their expected values.
REQUIRED_SETTINGS = {
    "PermitRootLogin": "no",
    "PasswordAuthentication": "no",
    "Protocol": "2",
    "PubkeyAuthentication": "yes",
}

def parse_sshd_config(filepath):
    config = {}
    try:
        with open(filepath, "r") as file:
            for line in file:
                # Remove whitespace and ignore blank lines or comments
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                parts = line.split(None, 1)
                if len(parts) == 2:
                    key, value = parts
                    # Save the last occurrence of the key in the configuration
                    config[key] = value.strip()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading '{filepath}': {e}", file=sys.stderr)
        sys.exit(1)
    return config

def audit_config(config, required_settings):
    errors = []
    for key, expected in required_settings.items():
        actual = config.get(key)
        if actual is None:
            errors.append(f"Setting '{key}' not found (expected: {expected}).")
        elif actual.lower() != expected.lower():
            errors.append(f"Setting '{key}' is '{actual}' (expected: {expected}).")
    return errors

def get_arguments():
    parser = argparse.ArgumentParser(description="Audit SSH daemon configuration for security settings.")
    parser.add_argument(
        "-f", "--file",
        default="/etc/ssh/sshd_config",
        help="Path to the SSH configuration file (default: /etc/ssh/sshd_config)"
    )
    return parser.parse_args()

def main():
    args = get_arguments()
    config = parse_sshd_config(args.file)
    errors = audit_config(config, REQUIRED_SETTINGS)
    
    if errors:
        print("HispionSSHGuard Audit Results:")
        for error in errors:
            print(f" - {error}")
        sys.exit(1)
    else:
        print("HispionSSHGuard: All required SSH configuration settings are correctly set.")
        sys.exit(0)

if __name__ == "__main__":
    main()
