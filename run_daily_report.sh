#!/bin/bash
set -e
echo "=== JRAVIS Daily Report Wrapper ==="
echo "Working dir: $(pwd)"
TARGET=$(find . -maxdepth 6 -type f -name generate_reports.py | head -n 1)
if [ -z "$TARGET" ]; then
  echo "ERROR: generate_reports.py not found!"
  ls -R .
  exit 2
fi
echo "Found: $TARGET"
python "$TARGET"
