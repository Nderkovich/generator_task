import unittest
import sys
import io
from unittest import mock

import generators


class GeneratorTest(unittest.TestCase):

    def test_with_skip(self):
        fake_file = io.StringIO('line 1\nline 2\nline 3')
        user_input = [r'\n',r's']
        result = "line 1\nline 2\nMoving to the next file\n"
        saved_stdout = sys.stdout
        try:
            out = io.StringIO()
            sys.stdout = out
            with mock.patch('builtins.open', return_value=fake_file, create=True):
                with mock.patch('builtins.input', side_effect=user_input):
                    generators.display_files('1.txt')
            output = out.getvalue()
            self.assertEqual(output, result)
        finally:
            sys.stdout = saved_stdout


if __name__=='__main__':
    unittest.main()