#!/bin/bash

# This is a script to update the repository

# Update local repository by force.
git fetch --all
git reset --hard origin/master

echo "The repository is successfully updated."