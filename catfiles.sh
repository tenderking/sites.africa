#!/bin/bash

# Directory to search for files
directory="./sites"

# Files and directories to exclude
exclude_patterns=(
  ".env"
  ".git"
  "README.md"
  "uv.lock"
  "catfiles.sh"
  __pycache__
)

# Add patterns from .gitignore
if [[ -f .gitignore ]]; then
  while IFS= read -r line || [[ -n "$line" ]]; do
    [[ $line =~ ^#.*$ || -z $line ]] && continue
    exclude_patterns+=("$line")
  done < .gitignore
fi

# Function to check if a file should be excluded
should_exclude() {
  local file="$1"
  for pattern in "${exclude_patterns[@]}"; do
    # Use bash pattern matching with **/ to match any level of subdirectories
    if [[ "$file" == *"/$pattern"* ]] || [[ "$file" == "$pattern" ]]; then
      return 0
    fi
  done
  return 1
}

# Find all files and process them
find "$directory" -type f -print0 | while IFS= read -r -d '' file; do
  if ! should_exclude "$file"; then
    echo "File: $file"
    echo "Content:"
    cat "$file"
    echo "--------------------------------------"
  fi
done
