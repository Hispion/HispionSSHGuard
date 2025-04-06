# HispionSSHGuard

HispionSSHGuard is an SSH configuration auditor by hispion. It scans your OpenSSH daemon configuration file (default: `/etc/ssh/sshd_config`) and verifies basic security settings to help secure your SSH server.

## Features

- Checks that `PermitRootLogin` is set to `no`
- Verifies that `PasswordAuthentication` is set to `no`
- Ensures the SSH protocol is `2`
- Confirms that `PubkeyAuthentication` is set to `yes`

## Usage

1. Clone or download the repository.
2. Run the auditor:

   ```bash
   chmod +x hispion_sshguard.py
   ./hispion_sshguard.py
   ```