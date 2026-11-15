#!/bin/bash
# Build, QA, legal gate, then commit + push. Usage: ./deploy.sh [--launch] "commit message"
set -e; cd "$(dirname "$0")"
MODE=""; [ "$1" = "--launch" ] && { MODE="--launch"; shift; }
python3 _build/build.py $MODE
python3 _build/check.py $MODE
python3 _build/legal_gate.py check || { echo "LEGAL GATE HOLD: not deploying"; exit 3; }
git add -A && git commit -qm "${1:-Rebuild}" && git push -q origin main && echo pushed
