#!/bin/bash

if [ $# -eq 0 ]; then
  echo "Usage: $0 <username>"
  exit 1
fi

USERNAME=$1

if [ "$USERNAME" == "root" ]; then
  SSH_DIR="/root/.ssh"
else
  SSH_DIR="/home/${USERNAME}/.ssh"
fi

if ! id "$USERNAME" &>/dev/null; then
  echo "User $USERNAME does not exist."
  exit 1
fi

PRIVATE_KEY_FILE="${SSH_DIR}/id_rsa"
PUBLIC_KEY_FILE="${SSH_DIR}/id_rsa.pub"

mkdir -p "${SSH_DIR}"
chmod 700 "${SSH_DIR}"

if [ -f "${PRIVATE_KEY_FILE}" ] || [ -f "${PUBLIC_KEY_FILE}" ]; then
  echo "SSH key already exists: ${PRIVATE_KEY_FILE}"
  exit 1
fi

ssh-keygen -t rsa -b 4096 -f "${PRIVATE_KEY_FILE}" -N ''

chmod 600 "${PRIVATE_KEY_FILE}"
chmod 644 "${PUBLIC_KEY_FILE}"

cat "${PUBLIC_KEY_FILE}" >> "${SSH_DIR}/authorized_keys"
chmod 600 "${SSH_DIR}/authorized_keys"

echo "SSH key pair created."
echo "Public key:"
cat "${PUBLIC_KEY_FILE}"

echo "SSH service has been enabled and started."
echo "Now, paste this private key in an id_rsa file and run ssh ${USERNAME}@<IP> id_rsa"