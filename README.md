# sly
Sly, your lazy-but-smart script, automatically collects red-teaming and OSCP tools, saving you the tedious chore of hunting down each script every single time. Tailored for red-teaming activities and OSCP preparation.

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

# With default settings, sly will put everything into the current working directory
python3 sly.py

# To specify a different destination directory
python3 sly.py -d /path/to/destination

# To specify a subdirectory within the current working directory
python3 sly.py -f subdirectory_name

# Combining both destination and subdirectory arguments (Note: subdirectory argument will be ignored in this case)
python3 sly.py -d /path/to/destination -f subdirectory_name

# Or just run it with this neat one-liner
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
| Tool Name | Platform | Purpose | 
| --- | --- | --- |
| Mimikatz | 🪟 | Credential dumping and manipulation |
| Unix-privesc-check | 🐧 | Checks for privilege escalation vectors |
| Seatbelt | 🪟 | Security checks and system enumeration |
| Ncat | 🪟 🐧 | Enhanced version of Netcat |
| LinPEAS | 🐧 | Privilege escalation checks |
| WinPEAS | 🪟 | Windows privilege escalation checks |
| ADpeas | 🪟 | Active Directory enumeration |
| PrintSpoofer64 | 🪟 | Abusing print spooler services |
| GodPotato | 🪟 | Exploiting windows BITS service |
| BloodHound | 🪟 | AD Trust analysis |
| PowerSploit | 🪟 | PowerShell-based exploitation |
| WPScan | 🪟 🐧 | WordPress vulnerability scanner |
| linpeas | 🪟 🐧 | Privilege escalation tools |
| winpeas | 🪟 🐧 | Privilege escalation tools |
| Rubeus | 🪟 | Kerberos attack framework |
| PsTools | 🪟 | Suite of command-line windows utilities |
| Kerbrute | 🪟 🐧 | Brute-forcing Kerberos pre-auth |
| nc64.exe | 🪟 | 64-bit Netcat for windows |
| PowerView | 🪟 | AD enumeration |
| SharpHound | 🪟 | Collecting AD data |
| Spray-Passwords.ps1 | 🪟 | Password spraying script |
| Sysinternals Suite | 🪟 | Volume Shadow Copy management |
| powercat.ps1 | 🪟 | PowerShell-based Netcat alternative |
| powerup.ps1 | 🪟 | PowerShell script for privilege escalation |
| spray-passwords.ps1 | 🪟 | Password spraying tool |
| DomainPasswordSpray.ps1 | 🪟 | Domain-wide password spraying tool |
| Ligolo-ng agent | 🪟 | Establish tunnels from a reverse TCP/TLS connection (agent) |
| Ligolo-ng proxy | 🐧 | Establish tunnels from a reverse TCP/TLS connection (proxy) |
| webshell.pHp |  | Simple PHP webshell |
| KeePass | 🪟 | Portable version of a popular password manager |
| pspy32 | 🐧 | Unprivileged Linux process snooping (32 bit) |
| pspy64 | 🐧 | Unprivileged Linux process snooping (64 bit) |
| suid3num.py | 🐧 | SUID bins enumeration, separate default bins from custom bins, cross-match those with bins in GTFO Bin's |
| OpenSSHesame.ps1 | 🪟 | Creates an SSH key pair and set up SSH access on Windows |
| ssh_backdoor.sh | 🐧 | Creates an SSH key pair and set up SSH access on Linux |
| automap.sh | 🐧 | Automate some Nmap scans. |
| SharpUp.exe | 🪟 | Part of GhostPack suite, C# port of PowerUp. |

## Disclaimer
See [Disclaimer](./DISCLAIMER.md).