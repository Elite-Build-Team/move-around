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


PHASE_2_FILES = \
	Domain-model-v0.1.pdf \
	Use-cases-v0.1.pdf

PHASE_2_FILES_REV_2 = \
	Project-description-v0.2.pdf \
	Team-risk-assessment-v0.2.pdf \
	Risk-assessment-v0.2.pdf 


PHASE_3_FILES = \
	Robustness-diagrams-v0.1.pdf

PHASE_3_FILES_REV_2 = \
	Project-plan-v0.2.pdf \
	Domain-model-v0.2.pdf \
	Use-cases-v0.2.pdf \
	Team-plan-v0.2.pdf \

PHASE_3_FILES_REV_3 = \
	Risk-assessment-v0.3.pdf 


PHASE_4_FILES = \
	Sequence-diagrams-v0.1.pdf \
	Project-code-v0.1.pdf

PHASE_4_FILES_REV_2 = \
	Robustness-diagrams-v0.2.pdf

PHASE_4_FILES_REV_3 = \
	Domain-model-v0.3.pdf \
	Use-cases-v0.3.pdf

PHASE_4_FILES = \
	Test-cases-v0.1.pdf \
	Class-diagram-v0.1.pdf

PHASE_5_FILES_REV_2 = \
	Sequence-diagram-v0.2.pdf \
	Project-code-v0.2.pdf

PHASE_5_FILES_REV_3 = \
	Robustness-diagrams-v0.3.pdf
	Use-cases-v0.4.pdf \
	Team-plan-v0.3.pdf

PHASE_5_FILES_REV_4 = \
	Risk-assessment-v0.4.pdf \
	Use-cases-v0.4.pdf

EXECUTABLES = pandoc
K := $(foreach exec,$(EXECUTABLES),\
        $(if $(shell which $(exec)),some string,$(error "No $(exec) in PATH")))

.PHONY: clean
clean:
	-rm -rf $(BUILDDIR)/*

$(PHASE_1_FILES): %-v0.1.pdf : %.md
	pandoc $< --metadata-file=misc/metadata.yaml -V mainfont='$(MAINFONT)' -V fontsize=12pt --pdf-engine=$(PDFENGINE) -o $(BUILDDIR)/$@

$(PHASE_2_FILES): %-v0.1.pdf : %.md
	pandoc $< --metadata-file=misc/metadata.yaml -V mainfont='$(MAINFONT)' -V fontsize=12pt --pdf-engine=$(PDFENGINE) -o $(BUILDDIR)/$@

$(PHASE_2_FILES_REV): %-v0.2.pdf : %.md
	pandoc $< --metadata-file=misc/metadata.yaml -V mainfont='$(MAINFONT)' -V fontsize=12pt --pdf-engine=$(PDFENGINE) -o $(BUILDDIR)/$@

$(PHASE_3_FILES): %-v0.1.pdf : %.md
	pandoc $< --metadata-file=misc/metadata.yaml -V mainfont='$(MAINFONT)' -V fontsize=12pt --pdf-engine=$(PDFENGINE) -o $(BUILDDIR)/$@

$(PHASE_3_FILES_REV_2): %-v0.2.pdf : %.md
	pandoc $< --metadata-file=misc/metadata.yaml -V mainfont='$(MAINFONT)' -V fontsize=12pt --pdf-engine=$(PDFENGINE) -o $(BUILDDIR)/$@

$(PHASE_3_FILES_REV_3): %-v0.3.pdf : %.md
	pandoc $< --metadata-file=misc/metadata.yaml -V mainfont='$(MAINFONT)' -V fontsize=12pt --pdf-engine=$(PDFENGINE) -o $(BUILDDIR)/$@

$(PHASE_4_FILES): %-v0.1.pdf : %.md
	pandoc $< --metadata-file=misc/metadata.yaml -V mainfont='$(MAINFONT)' -V fontsize=12pt --pdf-engine=$(PDFENGINE) -o $(BUILDDIR)/$@

$(PHASE_4_FILES_REV_2): %-v0.2.pdf : %.md
	pandoc $< --metadata-file=misc/metadata.yaml -V mainfont='$(MAINFONT)' -V fontsize=12pt --pdf-engine=$(PDFENGINE) -o $(BUILDDIR)/$@

$(PHASE_4_FILES_REV_3): %-v0.3.pdf : %.md
	pandoc $< --metadata-file=misc/metadata.yaml -V mainfont='$(MAINFONT)' -V fontsize=12pt --pdf-engine=$(PDFENGINE) -o $(BUILDDIR)/$@

$(PHASE_5_FILES): %-v0.1.pdf : %.md
	pandoc $< --metadata-file=misc/metadata.yaml -V mainfont='$(MAINFONT)' -V fontsize=12pt --pdf-engine=$(PDFENGINE) -o $(BUILDDIR)/$@

$(PHASE_5_FILES_REV_2): %-v0.2.pdf : %.md
	pandoc $< --metadata-file=misc/metadata.yaml -V mainfont='$(MAINFONT)' -V fontsize=12pt --pdf-engine=$(PDFENGINE) -o $(BUILDDIR)/$@

$(PHASE_5_FILES_REV_3): %-v0.3.pdf : %.md
	pandoc $< --metadata-file=misc/metadata.yaml -V mainfont='$(MAINFONT)' -V fontsize=12pt --pdf-engine=$(PDFENGINE) -o $(BUILDDIR)/$@

$(PHASE_5_FILES_REV_4): %-v0.3.pdf : %.md
	pandoc $< --metadata-file=misc/metadata.yaml -V mainfont='$(MAINFONT)' -V fontsize=12pt --pdf-engine=$(PDFENGINE) -o $(BUILDDIR)/$@

.PHONY: phase-1
phase-1: $(PHASE_1_FILES)
	@echo
	@echo "Build finished!"

.PHONY: phase-1-zip
phase-1-zip: $(PHASE_1_FILES)
	cd build
	zip -r software-engineering-2020.zip $(PHASE_1_FILES) $
	cd ..
	@echo
	@echo "Build finished!"


.PHONY: phase-2
phase-2: $(PHASE_2_FILES) $(PHASE_2_FILES_REV)
	@echo
	@echo "Build finished!"

.PHONY: phase-2-zip
phase-2-zip: $(PHASE_2_FILES) $(PHASE_2_FILES_REV_2)
	cd build
	zip -r software-engineering-2020.zip $(PHASE_2_FILES) $(PHASE_2_FILES_REV_2)
	cd ..
	@echo
	@echo "Build finished!"


.PHONY: phase-3
phase-3: $(PHASE_3_FILES) $(PHASE_3_FILES_REV_2) $(PHASE_3_FILES_REV_3)
	@echo
	@echo "Build finished!"

.PHONY: phase-3-zip
phase-3-zip: $(PHASE_3_FILES) $(PHASE_3_FILES_REV_2) $(PHASE_3_FILES_REV_3)
	cd build
	zip -r software-engineering-2020.zip $(PHASE_3_FILES) $(PHASE_3_FILES_REV_2) $(PHASE_3_FILES_REV_3)
	cd ..
	@echo
	@echo "Build finished!"


.PHONY: phase-4
phase-4: $(PHASE_4_FILES) $(PHASE_4_FILES_REV_2) $(PHASE_4_FILES_REV_3)
	@echo
	@echo "Build finished!"

.PHONY: phase-4-zip
.ONESHELL:
phase-4-zip: $(PHASE_4_FILES) $(PHASE_4_FILES_REV_2) $(PHASE_4_FILES_REV_3)
	cd build
	zip -r software-engineering-2020.zip $(PHASE_4_FILES) $(PHASE_4_FILES_REV_2) $(PHASE_4_FILES_REV_3)
	cd ..
	@echo
	@echo "Build finished!"

.PHONY: phase-5
phase-5: $(PHASE_4_FILES) $(PHASE_4_FILES_REV_2) $(PHASE_4_FILES_REV_3)
	@echo
	@echo "Build finished!"

.PHONY: phase-5-zip
.ONESHELL:
phase-5-zip: $(PHASE_5_FILES) $(PHASE_5_FILES_REV_2) $(PHASE_5_FILES_REV_3) $(PHASE_5_FILES_REV_4)
	cd build
	zip -r software-engineering-2020.zip $(PHASE_4_FILES) $(PHASE_4_FILES_REV_2) $(PHASE_4_FILES_REV_3) $(PHASE_5_FILES_REV_4)
	cd ..
	@echo
	@echo "Build finished!"