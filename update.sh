#!/bin/bash

# This is a script to update the repository

# Update local repository by force.
git fetch --all
git reset --hard origin/master

echo "The repository has been successfully updated.
The script now closing"

sleep 3