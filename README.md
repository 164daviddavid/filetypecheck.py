## Usage
Tries to identify the format of a file by checking for the magic bytes of known file formats. Note that a file is not guaranteed to be of a particular format just because it contains the magic bytes of that format.

**Identify a single file**
```
python3 filetypecheck.py <filepath>
```

**Identify multiple files**
```
python3 filetypecheck.py <filepath1> <filepath2> <filepath3> ...
```

**Only show files whose file extensions don't match their magic bytes**
```
python3 filetypecheck.py --non-matching <filepath1> ...
```

## Test Files
| **File Name** | **Source** | **Notes** |
| ------------- | ------ | ----- |
| doc\_example.doc | Created in Word | |
| docx\_example.docx | file-examples.com | |
| empty\_file | Created with touch | |
| gif89\example.gif | file-examples.com | |
| jpg\_example.jpg | file-examples.com | |
| mp3\_example.mp3 | file-examples.com | |
| mp3\_untagged\_example.mp3 | file-examples.com | Same as 'mp3\_example.mp3' but with the ID3 tags removed |
| no\_ext\_png\_example | file-examples.com | Same file as 'png\_example.png' but with the extension removed |
| non\_matching\_png\_example.jpg | file-examples.com | Same file as 'png\_example.png' but renamed to have .jpg extension |
| pdf\_example.pdf | file-examples.com | |
| png\_example.png | file-examples.com | |
| ppt\_example.ppt | file-examples.com | |
| ppt\_example\_2.ppt | Created in PowerPoint | |
| pptx\_embed\_excel\_example.pptx | Created in PowerPoint | .pptx file containing an embedded excel table from file 'resource\_pptx\_embed\_excel\_example.xlsx' |
| pptx\_example.pptx | Created in PowerPoint | |
| resource\_pptx\_embed\_excel\_example.xlsx | Created in Excel | Used as an embed in 'pptx\_embed\_excel\_example.pptx' |
| wav\_example.wav | file-examples.com | |
| webp\_example.webp | file-examples.com | |
| xls\_example.xls | Created in Excel | |
| xlsx\_example.xlsx | file-examples.com | |
