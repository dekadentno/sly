# sly
Curation of open-source tools and scripts, now streamlined through Sly, a script tailored for red-teaming activities and OSCP preparation.

Sly, your lazy-but-smart script, automatically collects red-teaming and OSCP tools, saving you the tedious chore of hunting down each script every single time.

Use these tools strictly for research and ethical learning.

## Usage
```bash
# Clone the Sly repository
git clone https://github.com/dekadentno/sly.git

# Run the Sly script
cd sly
python3 sly.py

# or, if the script needs executable permission
chmod +x sly.py
./sly.py

# With default settings sly will put everything into the default "sly" directory
python3 sly.py 

# To specify a different destination directory
python3 sly.py -d /path/to/destination

# Or just run it with this neat one liner
curl -sSL https://raw.githubusercontent.com/dekadentno/sly/main/sly.py | python3 -
```

This script was designed and tested for Kali Linux and may not work on other systems because it uses paths specific to Kali.
```bash
mlay in ~/projects/sly on main ● ● λ cat /etc/os-release

PRETTY_NAME="Kali GNU/Linux Rolling"
NAME="Kali GNU/Linux"
VERSION_ID="2023.3"
VERSION="2023.3"
VERSION_CODENAME=kali-rolling
ID=kali
ID_LIKE=debian
HOME_URL="https://www.kali.org/"
SUPPORT_URL="https://forums.kali.org/"
BUG_REPORT_URL="https://bugs.kali.org/"
ANSI_COLOR="1;31"


mlay in ~/projects/sly on main ● ● λ uname -a

Linux kali 6.3.0-kali1-arm64 #1 SMP Debian 6.3.7-1kali1 (2023-06-29) aarch64 GNU/Linux
```

## Tools
| Tool Name | Platform | Purpose | Has multiple Architectures |
| --- | --- | --- | --- |
| Mimikatz | Windows | Credential dumping and manipulation | false |
| Unix-privesc-check | Linux | Checks for privilege escalation vectors | false |
| Seatbelt | Windows | Security checks and system enumeration | false |
| Ncat | Cross-platform | Enhanced version of Netcat | false |
| LinPEAS | Linux | Privilege escalation checks | false |
| WinPEAS | Windows | Windows privilege escalation checks | false |
| ADpeas | Windows | Active Directory enumeration | false |
| PrintSpoofer64 | Windows | Abusing print spooler services | false |
| GodPotato | Windows | Exploiting Windows BITS service | false |
| BloodHound | Windows | AD Trust analysis | false |
| PowerSploit | Windows | PowerShell-based exploitation | false |
| WPScan | Cross-platform | WordPress vulnerability scanner | false |
| linpeas | Cross-platform | Privilege escalation tools | true |
| winpeas | Cross-platform | Privilege escalation tools | true |
| Rubeus | Windows | Kerberos attack framework | false |
| PsTools | Windows | Suite of command-line Windows utilities | false |
| Kerbrute | Cross-platform | Brute-forcing Kerberos pre-auth | false |
| nc64.exe | Windows | 64-bit Netcat for Windows | false |
| PowerView | Windows | AD enumeration | false |
| SharpHound | Windows | Collecting AD data | false |
| Spray-Passwords.ps1 | Windows | Password spraying script | false |
| Sysinternals Suite | Windows | Volume Shadow Copy management | true |
| powercat.ps1 | Windows | PowerShell-based Netcat alternative | false |
| powerup.ps1 | Windows | PowerShell script for privilege escalation | false |
| spray-passwords.ps1 | Windows | Password spraying tool | false |
| DomainPasswordSpray.ps1 | Windows | Domain-wide password spraying tool | false |

## Disclaimer
See [Disclaimer](./DISCLAIMER.md).