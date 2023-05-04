import sys
import os
import unittest
import subprocess
sys.path.insert(0,r'./') #Add root directory here


class GoogleTest(unittest.TestCase):

    # Change the current working directory
    cwd = os.getcwd()

    def test_build_success(self):
        result = subprocess.run([".\google.exe", "--help"], capture_output=True, cwd=os.path.join(cwd,'dist'), shell=True)
        with open('./test_example/help.txt', 'r') as f:
            help_ref = f.read()
        self.assertEqual(help_ref.lower(), str(result.stdout).lower())

    def test_search_wiki(self):
        result = subprocess.run([".\google.exe", "Facebook", "--debug"], capture_output=True, cwd=os.path.join(cwd,'dist'), shell=True)
        with open('./test_example/Facebook_wiki.txt', 'r') as f:
            facebook_wiki_ref = f.read()
        self.assertIn(facebook_wiki_ref.lower(), str(result.stdout).lower())


def main():
    unittest.main()


if __name__ == "__main__":
    main()
