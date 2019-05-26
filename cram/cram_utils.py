def convert_filename_to_url(filename):
    """ Converts local relative filename of lowres Cram image to URL for the same
    image in highres on Cram.
    Example of expected input:
    SNL%20Calculus%20Foreign%20Language%20Flashcards%20-%20Cram.com_files/32008932_m.jpg
    """
    img_number = filename.split('_', 1)[0]
    return 'https://images.cram.com/images/upload-flashcard' \
        + '/' + img_number[-6:-4] + '/' + img_number[-4:-2] + \
        '/' + img_number[-2:] + '/' + filename
