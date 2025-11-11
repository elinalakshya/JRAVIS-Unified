#!/bin/bash
set -e
echo "=== wrapper start ==="
echo "Working dir: $(pwd)"
echo "--- root listing ---"
ls -la
echo "------ searching for generate_reports.py ------"
FOUND=$(find "$(pwd)" -maxdepth 6 -type f -name generate_reports.py | head -n 1)
if [ -z "$FOUND" ]; then
  echo "ERROR: generate_reports.py NOT FOUND"
  exit 2
fi
echo "Found: $FOUND"
echo "=== running script ==="
python "$FOUND"
