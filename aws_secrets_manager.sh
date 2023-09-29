#!/bin/bash

# Get secret name from input param
SECRET_NAME="$1"

# Ensure AWS bin is in PATH, else specify full path in cmd
# Execute command and redirect output to stderr
aws secretsmanager get-secret-value --secret-id "$SECRET_NAME" 1>&2
