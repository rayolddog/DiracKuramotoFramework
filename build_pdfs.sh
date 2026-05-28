#!/usr/bin/env bash
# build_pdfs.sh — render PAPER_UNIFIED.md, AB_VISIBILITY_PAPER.md,
# COSMIC_EXPANSION_PAPER.md, DISCRETIZATION_AS_SYNC_PAPER.md, and EQUATIONS.md to PDF
#
# Produces:
#   ManyClocks.pdf         — pandoc render of PAPER_UNIFIED.md, TOC depth 3
#   AB_visibility.pdf      — pandoc render of AB_VISIBILITY_PAPER.md, TOC depth 2
#   CosmicExpansion.pdf    — pandoc render of COSMIC_EXPANSION_PAPER.md, TOC depth 2
#   CosmicExpansion.tex    — pandoc-generated LaTeX source from COSMIC_EXPANSION_PAPER.md
#   DiscretizationAsSync.pdf — pandoc render of DISCRETIZATION_AS_SYNC_PAPER.md, TOC depth 2
#   equations.pdf          — pandoc render of EQUATIONS.md, TOC depth 2
#   equations.tex          — pandoc-generated LaTeX source from EQUATIONS.md
#   paper.tex              — pandoc-generated LaTeX source from PAPER_UNIFIED.md
#   paper.pdf              — two-pass xelatex compile of paper.tex
#
# Requires: pandoc, xelatex (TeX Live or MacTeX)
# Uses: pdf_header.tex (Unicode-to-LaTeX mappings)
#       tests/ (for figures referenced from PAPER_UNIFIED.md without a path)

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

# Build the AB visibility companion paper
echo "Building AB_visibility.pdf from AB_VISIBILITY_PAPER.md..."
pandoc "${REPO_DIR}/AB_VISIBILITY_PAPER.md" \
    -o "${REPO_DIR}/AB_visibility.pdf" \
    --toc --toc-depth=2 \
    "${PANDOC_OPTS[@]}"

# Build the cosmic expansion companion paper
echo "Building CosmicExpansion.pdf from COSMIC_EXPANSION_PAPER.md..."
pandoc "${REPO_DIR}/COSMIC_EXPANSION_PAPER.md" \
    -o "${REPO_DIR}/CosmicExpansion.pdf" \
    --toc --toc-depth=2 \
    "${PANDOC_OPTS[@]}"

# Regenerate CosmicExpansion.tex from COSMIC_EXPANSION_PAPER.md (standalone LaTeX source)
echo "Regenerating CosmicExpansion.tex from COSMIC_EXPANSION_PAPER.md..."
pandoc "${REPO_DIR}/COSMIC_EXPANSION_PAPER.md" \
    -s -o "${REPO_DIR}/CosmicExpansion.tex" \
    --toc --toc-depth=2 \
    "${PANDOC_OPTS[@]}"

# Build the discretization-as-sync companion paper
echo "Building DiscretizationAsSync.pdf from DISCRETIZATION_AS_SYNC_PAPER.md..."
pandoc "${REPO_DIR}/DISCRETIZATION_AS_SYNC_PAPER.md" \
    -o "${REPO_DIR}/DiscretizationAsSync.pdf" \
    --toc --toc-depth=2 \
    "${PANDOC_OPTS[@]}"

# Build the equations reference
echo "Building equations.pdf from EQUATIONS.md..."
pandoc "${REPO_DIR}/EQUATIONS.md" \
    -o "${REPO_DIR}/equations.pdf" \
    --toc --toc-depth=2 \
    "${PANDOC_OPTS[@]}"

# Regenerate equations.tex from EQUATIONS.md (standalone LaTeX source)
echo "Regenerating equations.tex from EQUATIONS.md..."
pandoc "${REPO_DIR}/EQUATIONS.md" \
    -s -o "${REPO_DIR}/equations.tex" \
    --toc --toc-depth=2 \
    "${PANDOC_OPTS[@]}"

# Regenerate paper.tex from PAPER_UNIFIED.md (standalone LaTeX source)
echo "Regenerating paper.tex from PAPER_UNIFIED.md..."
pandoc "${REPO_DIR}/PAPER_UNIFIED.md" \
    -s -o "${REPO_DIR}/paper.tex" \
    "${PANDOC_OPTS[@]}"

# Compile paper.pdf from paper.tex (two passes for cross-refs / TOC).
# tests/ is on TEXINPUTS so figures referenced without a path (e.g.
# entangled_pair_two_stage.png) resolve. Clean stale aux files first so a
# previous partial compile cannot poison this run.
echo "Compiling paper.pdf via xelatex (two-pass)..."
( cd "${REPO_DIR}" \
    && rm -f paper.aux paper.toc paper.out paper.log \
    && TEXINPUTS=".:tests:" xelatex -interaction=nonstopmode paper.tex > /dev/null \
    && TEXINPUTS=".:tests:" xelatex -interaction=nonstopmode paper.tex > /dev/null )

# Report
echo
echo "Done:"
ls -lh "${REPO_DIR}/ManyClocks.pdf" "${REPO_DIR}/AB_visibility.pdf" \
       "${REPO_DIR}/CosmicExpansion.pdf" "${REPO_DIR}/CosmicExpansion.tex" \
       "${REPO_DIR}/DiscretizationAsSync.pdf" \
       "${REPO_DIR}/equations.pdf" "${REPO_DIR}/equations.tex" \
       "${REPO_DIR}/paper.tex" "${REPO_DIR}/paper.pdf" \
    | awk '{print "  " $9 ": " $5}'
