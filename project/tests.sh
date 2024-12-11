#!/bin/bash

echo "Running Automated Tests for the Data Pipeline..."

# Run the tests
python3 ./project/tests.py

# Wait for user input to prevent the terminal from closing
echo "Press any key to exit."
read -n 1 -s