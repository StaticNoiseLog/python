from tkinter import filedialog
from tkinter import Tk
import platform
import re
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from cram_utils import *

# navigate to CSV file with dialog unless it is Mac OS
if platform.system() != 'Darwin':
    root = Tk()
    root.filename = filedialog.askopenfilename(
        initialdir="", title="Select file", filetypes=(("HTML files", "*.html"), ("all files", "*.*")))
    input_filename = root.filename
    root.destroy()
else:
    input_filename = 'cram.html'  # workaround for Mac OS

output_directory = input_filename.rsplit('/', 1)[0]

with open(input_filename, 'r',
          encoding='utf-8',
          errors='strict',  # insist on correct encoding
          newline=None) as content_file:
    content = content_file.read()

content = re.sub('<head>(.*?|\n)*?</head>',
                 '<head><meta charset="utf-8"/></head>', content)

content = re.sub('<body>(.*?|\n)*?<table class="flashCardsListingTable',
                 '<body><table class="flashCardsListingTable', content)

content = re.sub('<\/table(.*?|\n)*?</html>',
                 '</table></body></html>', content)

content = re.sub(
    '</head>', '</head><meta name="changed" content="00:00:00"><style type="text/css">@page { size: 8.27in 11.69in; margin: 0.2in }</style>', content)

# remove first (empty) column of table
content = re.sub('<td class="audio">(.*?|\n)*?<\/td>', '', content)

# fix images and download higher resolution version from Cram
soup = BeautifulSoup(content, "html.parser")
images = soup.find_all('img')
for img in images:
    img['width'] = "auto"
    img['height'] = "auto"
    img['src'] = img['src'].replace('_m', '_b')  # _b is higher resolution
    img_subdirectory_and_filename = img['src'].rsplit('/', 1)
    img_subdirectory = urllib.parse.unquote(img_subdirectory_and_filename[0])
    img_filename = img_subdirectory_and_filename[1]
    img_full_filename = output_directory + '/' + \
        img_subdirectory + '/' + img_filename
    try:
        img_url = convert_filename_to_url_flex(img_filename, 'https://images.cram.com/images/upload-flashcard')
        print('Downloading ', img_url, ' to ', img_full_filename)
        urllib.request.urlretrieve(img_url, img_full_filename)
    except (urllib.error.HTTPError) as http_error:
        print(http_error)
        img_url = convert_filename_to_url_flex(img_filename, 'https://dp11i9uvzjqmt.cloudfront.net/2/images/upload-flashcards')
        print('Downloading ', img_url, ' to ', img_full_filename)
        urllib.request.urlretrieve(img_url, img_full_filename)

content = str(soup)  # from HTML back to string

output_filename = input_filename.rsplit('.', 1)[0] + "_FIXED.html"

with open(output_filename, "w", encoding='utf-8') as outfile:
    print(content, file=outfile)

print("DONE!")
