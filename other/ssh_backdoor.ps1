param (
    [Parameter(Mandatory=$true)]
    [string]$password,

    [Parameter(Mandatory=$false)]
    [ValidateSet("rsa", "ecdsa", "ed25519", "dsa")]
    [string]$algorithm = "rsa",

    [switch]$help
)

function Show-Help {
    "Usage: .\YourScriptName.ps1 [-password] <password> [-algorithm] <algorithm> [-help]"
    "Parameters:"
    "  -password    Mandatory. Specifies the passphrase for the SSH key."
    "  -algorithm   Optional. Specifies the algorithm for the SSH key. Default is 'rsa'."
    "               Supported values are rsa, ecdsa, ed25519, dsa."
    "  -help        Shows this help message."
    exit
}

if ($help) {
    Show-Help
}

# Ensure the .ssh directory exists
$sshDir = "$env:USERPROFILE\.ssh"
if (-not (Test-Path -Path $sshDir)) {
    New-Item -ItemType Directory -Force -Path $sshDir
}

# Generate SSH key pair with the provided passphrase and algorithm
ssh-keygen -t $algorithm -f "$sshDir\id_$algorithm" -q -N $password

# Add the public key to authorized_keys
$publicKeyPath = "$sshDir\id_$algorithm.pub"
$authorizedKeysPath = "$sshDir\authorized_keys"
if (-not (Test-Path -Path $authorizedKeysPath)) {
    Get-Content -Path $publicKeyPath | Out-File -FilePath $authorizedKeysPath
} else {
    $publicKeyContent = Get-Content -Path $publicKeyPath
    if (-not (Select-String -Path $authorizedKeysPath -Pattern $publicKeyContent)) {
        Add-Content -Path $authorizedKeysPath -Value $publicKeyContent
    }
}

# Optional: Start the SSH service if not already running and set it to start automatically
if (Get-WindowsCapability -Online | Where-Object { $_.Name -like 'OpenSSH.Server*' -and $_.State -eq 'Installed' }) {
    Set-Service -Name 'sshd' -StartupType 'Automatic' -Status 'Running'
}

# Optional: Configure the Windows Firewall to allow SSH connections if not already configured
$firewallRuleName = "SSH"
if (-not (Get-NetFirewallRule -Name $firewallRuleName -ErrorAction SilentlyContinue)) {
    New-NetFirewallRule -Name $firewallRuleName -DisplayName "SSH" -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
}
