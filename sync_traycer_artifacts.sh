#!/bin/sh
# Mirror the Traycer epic's artifact store into the repo.
# Traycer keeps artifacts in its own store (~/.traycer/epics/<id>/artifacts);
# there is no CLI export, so this is a plain one-way copy. Re-run any time.
set -eu

EPIC=${TRAYCER_EPIC_ID:-c443d91e-b0d5-43ff-a31b-805574ab7771}
SRC="$HOME/.traycer/epics/$EPIC/artifacts"
DEST="$(cd "$(dirname "$0")" && pwd)/traycer_artifacts"

[ -d "$SRC" ] || { echo "no artifact store at $SRC" >&2; exit 1; }

mkdir -p "$DEST"
rsync -a --delete --exclude '.DS_Store' "$SRC"/ "$DEST"/
printf 'epic:    %s\nsource:  %s\nsynced:  %s\nfiles:   %s\n' \
    "$EPIC" "$SRC" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
    "$(find "$DEST" -name '*.md' | wc -l | tr -d ' ')" > "$DEST/SYNC_PROVENANCE.txt"
echo "synced $(find "$DEST" -name '*.md' | wc -l | tr -d ' ') artifacts -> $DEST"
