## INFORMATION

- exiftool filename
- look at license it looks like base64 encoding
- exiftool cat.jpeg | grep License | sed -e "s/.*: //" | base64 -d
- sed grabs part after the ":" in "License" grep and "base64 -d" decodes.
