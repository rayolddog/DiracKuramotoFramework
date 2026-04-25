#!/usr/bin/env bash
# build_pdfs.sh — render PAPER_UNIFIED.md and EQUATIONS.md to PDF
#
# Produces:
#   ManyClocks.pdf — the full paper, with TOC depth 3
#   equations.pdf  — the equation reference, with TOC depth 2
#
# Requires: pandoc, xelatex (TeX Live or MacTeX)
# Uses: pdf_header.tex (Unicode-to-LaTeX mappings)

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HEADER="${REPO_DIR}/pdf_header.tex"

# Check required tools
for cmd in pandoc xelatex; do
    if ! command -v "$cmd" >/dev/null 2>&1; then
        echo "Error: '$cmd' not found in PATH" >&2
        echo "Install pandoc and a TeX distribution (MacTeX on macOS, TeX Live on Linux)." >&2
        exit 1
    fi
done

if [[ ! -f "$HEADER" ]]; then
    echo "Error: $HEADER not found" >&2
    exit 1
fi

# Common pandoc options
PANDOC_OPTS=(
    --pdf-engine=xelatex
    -V geometry:margin=1in
    -V colorlinks=true
    --include-in-header="$HEADER"
)

# Build the paper
echo "Building ManyClocks.pdf from PAPER_UNIFIED.md..."
pandoc "${REPO_DIR}/PAPER_UNIFIED.md" \
    -o "${REPO_DIR}/ManyClocks.pdf" \
    --toc --toc-depth=3 \
    "${PANDOC_OPTS[@]}"

# Build the equations reference
echo "Building equations.pdf from EQUATIONS.md..."
pandoc "${REPO_DIR}/EQUATIONS.md" \
    -o "${REPO_DIR}/equations.pdf" \
    --toc --toc-depth=2 \
    "${PANDOC_OPTS[@]}"

# Report
echo
echo "Done:"
ls -lh "${REPO_DIR}/ManyClocks.pdf" "${REPO_DIR}/equations.pdf" \
    | awk '{print "  " $9 ": " $5}'
