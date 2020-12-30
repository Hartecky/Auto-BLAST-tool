# Remote sequence downloader

## Description:

CLI program which job is to find and download all avalaible DNA sequences using NCBI nucleotide BLAST (blastn) in an automatic way. 
User is providing arguments like:
```
- -q , --query      Nucleotide sequence query
- -o , --organism   Name of the organism input
- -e , --exclude    Exclude provided organism (False by default)
- -n , --num_seq    Select sequence search target to download (100 by default)
- -a , --align      Download aligned or complete sequences (aligned by
                    default)
- -out , --output   Output file name (output.txt by default)
```
After that, the script is opening web browser, goes to the main nucleotide BLAST website, and fills it with provided information from the arguments. Next the 'BLAST' button is clicked and script is submitting query. After a while when searching is done, script is clicking download button and found sequences are downloaded to an output file.

### Compatibility:
- Microsot Edge WebDriver
- Windows OS (for now)


### Technologies:
- Python 3.7+
- Selenium module
- Microsoft Edge WebDriver compatible with your Microsoft Edge web browser


### Requirements
- Selenium module
```
pip install selenium
```

__Microsoft Edge WebDriver__
Microsoft Edge Webdriver should be localised in the C:\path and it is also required to first check your browser version.

[Link to official Microsoft Developer Website](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
