import os
import unittest

from click.testing import CliRunner
from cli import display_cv_data

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'cv_data.json')


class TestCLI(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()
        self.testfile = open(TESTDATA_FILENAME)
        self.testdata = self.testfile.read()

    def test_personal_info(self):
        result = self.runner.invoke(display_cv_data, ['personal'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Name:", result.output)
        self.assertIn("Email:", result.output)
        self.assertIn("Phone:", result.output)

    def test_experience_info(self):
        result = self.runner.invoke(display_cv_data, ['experience'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Position:", result.output)
        self.assertIn("Company:", result.output)
        self.assertIn("Year:", result.output)

    def test_education_info(self):
        result = self.runner.invoke(display_cv_data, ['education'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Degree:", result.output)
        self.assertIn("University:", result.output)
        self.assertIn("Year:", result.output)

    def test_invalid_section(self):
        result = self.runner.invoke(display_cv_data, ['invalid_section'])
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn("'invalid_section' is not one of 'personal', 'experience', 'education'", result.output)

    def tearDown(self):
        self.testfile.close()


if __name__ == '__main__':
    unittest.main()
