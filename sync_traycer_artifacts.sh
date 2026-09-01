#!/bin/sh
# Mirror the Traycer epic's artifact store into the repo.
# Traycer keeps artifacts in its own store (~/.traycer/epics/<id>/artifacts);
# there is no CLI export, so this is a plain one-way copy. Re-run any time.
#
# The artifacts reference local files by absolute path. This repository is
# public, so the mirror is scrubbed on the way in: $HOME is rewritten to "~"
# so the operator's home-directory path (and username) is not published.
# Paths stay human-readable and still resolve for anyone with the repo.
set -eu

EPIC=${TRAYCER_EPIC_ID:-c443d91e-b0d5-43ff-a31b-805574ab7771}
SRC="$HOME/.traycer/epics/$EPIC/artifacts"
DEST="$(cd "$(dirname "$0")" && pwd)/traycer_artifacts"

[ -d "$SRC" ] || { echo "no artifact store at $SRC" >&2; exit 1; }

mkdir -p "$DEST"
rsync -a --delete --exclude '.DS_Store' "$SRC"/ "$DEST"/

# Scrub absolute home paths from the mirrored text. Portable in-place edit:
# GNU sed wants -i, BSD/macOS sed wants -i ''. Write to a temp file instead.
scrubbed=0
for f in $(grep -rl "$HOME" "$DEST" 2>/dev/null || true); do
    sed "s|$HOME|~|g" "$f" > "$f.tmp" && mv "$f.tmp" "$f"
    scrubbed=$((scrubbed + 1))
done

files=$(find "$DEST" -name '*.md' | wc -l | tr -d ' ')
printf 'epic:     %s\nsource:   ~/.traycer/epics/%s/artifacts\nsynced:   %s\nfiles:    %s\nscrubbed: %s (absolute home paths rewritten to ~)\n' \
    "$EPIC" "$EPIC" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$files" "$scrubbed" \
    > "$DEST/SYNC_PROVENANCE.txt"

# Fail loudly rather than silently publishing a path the scrub missed.
if grep -rq "$HOME" "$DEST" 2>/dev/null; then
    echo "WARNING: home paths still present after scrub:" >&2
    grep -rl "$HOME" "$DEST" >&2
    exit 2
fi

echo "synced $files artifacts -> $DEST ($scrubbed files scrubbed)"
