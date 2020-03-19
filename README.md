# Software Engineering 2020

## Clone project
`git clone https://github.com/Elite-Build-Team/software-engineering-2020.git`

## Make PDFs/ZIP for phase-n (only for Linux)

Prerequisites:
1. pandoc
2. pdfunite
3. zip
4. xelatex
5. Linux Biolinum font

E.g. for phase 1:
```bash
cd software-engineering-2020/
mkdir build #Files will be generated inside build/
make phase-1 #Generate PDFs inside build/
make phase-1-zip #Generate ZIP inside build/
```