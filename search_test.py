import sys
import os
import unittest
import subprocess
sys.path.insert(0,r'./') #Add root directory here


class GoogleTest(unittest.TestCase):

    def test_build_success(self):
        # Change the current working directory
        cwd = os.getcwd()
        process = subprocess.Popen(["./google.exe", "--help"],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       cwd=os.path.join(cwd,'dist'), shell=True)

        result, err = process.communicate()

        with open('./test_example/help.txt', 'r') as f:
            help_ref = f.read()
        self.assertEqual(help_ref.lower(), str(result).lower())

    def test_search_wiki(self):
        # Change the current working directory
        cwd = os.getcwd()
        process = subprocess.Popen(["./google.exe", "Facebook", "--debug"],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       cwd=os.path.join(cwd,'dist'), shell=True)

        result, err = process.communicate()

        with open('./test_example/Facebook_wiki.txt', 'r') as f:
            facebook_wiki_ref = f.read()
        self.assertIn(facebook_wiki_ref.lower(), str(result).lower())
        print(err)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
