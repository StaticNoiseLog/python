with open('files.py',  # try with resources (closes object)
          encoding='utf-8', errors='strict',  # insist on correct encoding
          newline=None) as dafile:
    print(dafile.read(5))  # first 5 characters
