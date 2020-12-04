# Auto-Blast-tool

---

## Description:

A project whose goal was to create a script / executable program responsible for searching and downloading DNA sequences, from NCBI nucleotide BLAST (blastn) database automatically.

Compatible with Microsoft Edge only

---
### Technologies:
- Python 3.7+
- Selenium module
- Microsoft Edge WebDriver compatible with your Microsoft Edge web browser

---
### Requirements
__Selenium module__

_pip install selenium_

__Microsoft Edge WebDriver__

[Link to official Microsoft Developer Website](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

---
### Usage:
For now:
- Download compressed folder with all needed files from here, unzip
- Open ___cmd___, then ___cd/___ into the directory, where Auto-Blast Tool is being stored
- Run ___python main.py___ or run the ___main.py___ scripts via your current using IDE (e.g. PyCharm / SublimeText3)
- Paste or type your sequence with an organism to the inputs
- Click ___Submit Auto-Blast___ and let the program do its work

Two cases are considered while running: 
1) Sequences will be found
2) Sequences will not be found

In the first case downloaded file with, all matched queries in a FASTA format (Aligned sequences!) will be downloaded to the folder, where the files are downloaded from a browser.
On the other hand after page redirection the program stops and opened tab closes automatically.
