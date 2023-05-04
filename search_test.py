import sys
import os
import unittest
import subprocess
sys.path.insert(0,r'./') #Add root directory here


class GoogleTest(unittest.TestCase):
    def test_search_wiki(self):
        # Change the current working directory
        cwd = os.getcwd()
        result = subprocess.run([".\google.exe", "Facebook", "--debug"], capture_output=True, cwd=os.path.join(cwd,'dist'), shell=True)
        with open('./test_example/Facebook_wiki.txt', 'r') as f:
            facebook_wiki_ref = f.read()
        self.assertIn(facebook_wiki_ref.lower(), str(result.stdout).lower())


def main():
    unittest.main()


if __name__ == "__main__":
    main()
