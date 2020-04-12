# Software Engineering 2020

## Clone project
`git clone https://github.com/Elite-Build-Team/software-engineering-2020.git`

## Install prerequisites
1. Install Linux Biolinum font from [here](https://www.fontsquirrel.com/fonts/linux-biolinum).
2. ```bash
    apt-get install texlive pandoc zip
    ```

## Make PDFs/ZIP for phase-n (only for Linux)

E.g. for phase 1:
```bash
cd software-engineering-2020/
mkdir build #Files will be generated inside build/
make phase-1 #Generate PDFs inside build/
make phase-1-zip #Generate ZIP inside build/
```