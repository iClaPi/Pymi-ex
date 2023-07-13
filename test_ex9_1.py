import unittest
import subprocess

class TestGitHubRepos(unittest.TestCase):
    def test_list_user_repositories(self):
        output = subprocess.check_output(["python3", "githubrepos.py", "pymivn"]).decode().strip()
        self.assertEqual(output, "repo1\nrepo2\nrepo3")

if __name__ == "__main__":
    unittest.main()
