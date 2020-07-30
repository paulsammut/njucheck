#!/bin/bash

# This bash script needs to be sourced to work. It will prompt you for a password
# and decrypt and source the secrets.
# run it like this: . ./decrypt_secrets.sh

decrypted=$(openssl aes-256-cbc -d -in secrets_encrypted)

# Uncomment if you want to see your info
# echo "$decrypted"

eval "$decrypted"
