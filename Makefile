SHELL = /bin/sh
BUILDDIR = build
PDFENGINE = xelatex
MAINFONT = Linux Biolinum

PHASE_1_FILES = \
	Project-plan-v0.1.pdf \
	Project-description-v0.1.pdf \
	Team-plan-v0.1.pdf \
	Risk-assessment-v0.1.pdf \
	Team-risk-assessment-v0.1.pdf \
	Feasibility-study-v0.1.pdf

EXECUTABLES = pandoc
K := $(foreach exec,$(EXECUTABLES),\
        $(if $(shell which $(exec)),some string,$(error "No $(exec) in PATH")))

.PHONY: clean
clean:
	-rm -rf $(BUILDDIR)/*

$(PHASE_1_FILES): %-v0.1.pdf : %.md
	pandoc $< --metadata-file=misc/metadata.yaml -V mainfont='$(MAINFONT)' -V fontsize=12pt --pdf-engine=$(PDFENGINE) -o $(BUILDDIR)/$@

.PHONY: phase-1
phase-1: $(PHASE_1_FILES)
	@echo
	@echo "Build finished!"

.PHONY: phase-1-zip
phase-1-zip: $(PHASE_1_FILES)
	zip -r $(BUILDDIR)/phase-1.zip $(addprefix $(BUILDDIR)/, $(PHASE_1_FILES))
	@echo
	@echo "Build finished!"