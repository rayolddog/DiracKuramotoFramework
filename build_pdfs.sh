#!/usr/bin/env bash
# build_pdfs.sh — render PAPER_UNIFIED.md, PAPER_REVISED.md, COVER_LETTER.md,
# AB_VISIBILITY_PAPER.md, COSMIC_EXPANSION_PAPER.md, DISCRETIZATION_AS_SYNC_PAPER.md,
# and EQUATIONS.md to PDF
#
# Produces:
#   current_revision_DK_paper.pdf — pandoc render of current_revision_DK_paper.md
#                            (the canonical working manuscript), TOC depth 3
#   ManyClocks.pdf         — pandoc render of PAPER_UNIFIED.md, TOC depth 3
#   Two_Regimes_of_Chiral_Mass_Coupling.pdf       — pandoc render of PAPER_REVISED.md, TOC depth 3
#   4D-3DandSpacetime.pdf  — pandoc render of 4D-3DandSpacetime.md, TOC depth 3
#                            (NOTE: that document uses \( \) / \[ \] math delimiters rather than
#                            $ ... $, so it needs -f markdown+tex_math_single_backslash)
#   COVER_LETTER.pdf       — pandoc render of COVER_LETTER.md (cover letter, no TOC)
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

# Build the current working revision of the main DK paper (canonical manuscript;
# PAPER_REVISED.md below is the frozen FoP-submission snapshot and stays as-is)
echo "Building current_revision_DK_paper.pdf from current_revision_DK_paper.md..."
pandoc "${REPO_DIR}/current_revision_DK_paper.md" \
    -o "${REPO_DIR}/current_revision_DK_paper.pdf" \
    --toc --toc-depth=3 \
    "${PANDOC_OPTS[@]}"

# Build the 4D-to-3+1 spacetime document (speculative extension; untracked working doc).
# It uses \( \) and \[ \] rather than $ ... $, which pandoc does not read as math by
# default, hence the explicit input format.
if [[ -f "${REPO_DIR}/4D-3DandSpacetime.md" ]]; then
    echo "Building 4D-3DandSpacetime.pdf from 4D-3DandSpacetime.md..."
    pandoc "${REPO_DIR}/4D-3DandSpacetime.md" \
        -f markdown+tex_math_single_backslash \
        -o "${REPO_DIR}/4D-3DandSpacetime.pdf" \
        --toc --toc-depth=3 \
        "${PANDOC_OPTS[@]}"
else
    echo "Skipping 4D-3DandSpacetime.pdf (source not present)."
fi

# Build the revised single-paper manuscript (frozen FoP-submission snapshot) and its
# standalone LaTeX source for arXiv.
#
# NOTE (2026-08-24): PAPER_REVISED.md is currently ABSENT from the working tree — the
# canonical manuscript now lives in current_revision_DK_paper.md, built above. Because
# this script runs under `set -e`, an unguarded pandoc call on a missing source aborted
# the whole build here, silently skipping everything below (cover letter, AB visibility,
# cosmic expansion, discretization, equations, paper.tex/pdf). The guard below keeps the
# rest of the build alive. If the frozen snapshot is restored, this block runs unchanged.
if [[ -f "${REPO_DIR}/PAPER_REVISED.md" ]]; then
    echo "Building Two_Regimes_of_Chiral_Mass_Coupling.pdf from PAPER_REVISED.md..."
    pandoc "${REPO_DIR}/PAPER_REVISED.md" \
        -o "${REPO_DIR}/Two_Regimes_of_Chiral_Mass_Coupling.pdf" \
        --toc --toc-depth=3 \
        "${PANDOC_OPTS[@]}"

    echo "Regenerating Two_Regimes_of_Chiral_Mass_Coupling.tex from PAPER_REVISED.md..."
    pandoc "${REPO_DIR}/PAPER_REVISED.md" \
        -s -o "${REPO_DIR}/Two_Regimes_of_Chiral_Mass_Coupling.tex" \
        --toc --toc-depth=3 \
        "${PANDOC_OPTS[@]}"
else
    echo "Skipping Two_Regimes_of_Chiral_Mass_Coupling.{pdf,tex} (PAPER_REVISED.md not present)."
fi

# Build the submission cover letter (no TOC)
echo "Building COVER_LETTER.pdf from COVER_LETTER.md..."
pandoc "${REPO_DIR}/COVER_LETTER.md" \
    -o "${REPO_DIR}/COVER_LETTER.pdf" \
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

# Build the Born-selection paper (Paper 1 draft)
echo "Building Born_Selection.pdf from drafts/PAPER1_DRAFT_born_selection.md..."
pandoc "${REPO_DIR}/drafts/PAPER1_DRAFT_born_selection.md" \
    -o "${REPO_DIR}/Born_Selection.pdf" \
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
# List only what was actually produced, so a guarded/skipped target does not emit an
# ls error into the summary.
for f in current_revision_DK_paper.pdf \
         4D-3DandSpacetime.pdf \
         ManyClocks.pdf \
         Two_Regimes_of_Chiral_Mass_Coupling.pdf Two_Regimes_of_Chiral_Mass_Coupling.tex \
         COVER_LETTER.pdf AB_visibility.pdf \
         CosmicExpansion.pdf CosmicExpansion.tex \
         DiscretizationAsSync.pdf \
         equations.pdf equations.tex \
         paper.tex paper.pdf; do
    if [[ -f "${REPO_DIR}/${f}" ]]; then
        ls -lh "${REPO_DIR}/${f}" | awk '{print "  " $9 ": " $5}'
    else
        echo "  ${f}: (not built)"
    fi
done
