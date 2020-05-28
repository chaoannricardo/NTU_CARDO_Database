#!/bin/bash

# This is a script to update the repository

# Update local repository by force.
git fetch --all
git reset --hard origin/master

# grep column_list from configuration.py
# head -n 99 configuration.py | tail -n 46 > column_list.txt
python configuration.py

echo "The repository has been successfully updated.
The script now closing"

sleep 3