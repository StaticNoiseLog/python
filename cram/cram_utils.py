def convert_filename_to_url(filename):
    """ Converts local relative filename of lowres Cram image to URL for the same
    image in highres on Cram.
    Example of expected input:
    SNL%20Calculus%20Foreign%20Language%20Flashcards%20-%20Cram.com_files/32008932_m.jpg
    """
    img_number = filename.split('_', 1)[0]
    # https://images.cram.com/images/upload-flashcard
    return 'https://dp11i9uvzjqmt.cloudfront.net/2/images/upload-flashcards' \
        + '/' + img_number[-6:-4] + '/' + img_number[-4:-2] + \
        '/' + img_number[-2:] + '/' + filename

def convert_filename_to_url_flex(filename, url):
    """ Converts local relative filename of lowres Cram image to URL for the same
    image in highres on Cram.
    Example of expected input:
    SNL%20Calculus%20Foreign%20Language%20Flashcards%20-%20Cram.com_files/32008932_m.jpg
    """
    img_number = filename.split('_', 1)[0]
    return url \
        + '/' + img_number[-6:-4] + '/' + img_number[-4:-2] + \
        '/' + img_number[-2:] + '/' + filename
