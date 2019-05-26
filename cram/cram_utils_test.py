from unittest import TestCase, main
from cram_utils import convert_filename_to_url


class UtilsTestCase(TestCase):
    def test_convert_filename_to_url_ok(self):
        self.assertEqual('https://images.cram.com/images/upload-flashcard/98/92/62/31989262_b.jpg',
                         convert_filename_to_url('31989262_b.jpg'))


if __name__ == '__main__':
    main()
