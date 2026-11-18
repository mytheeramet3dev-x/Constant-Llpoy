import unittest
from pathlib import Path

class PinnedGitHubCliInstallerTests(unittest.TestCase):
    def test_installer_pins_exact_release_and_asset_digest(self):
        script = (Path(__file__).with_name("install_pinned_gh_cli.sh")).read_text()
        self.assertIn('version="2.103.3"', script)
        self.assertIn('gh_\${version}_linux_amd64.tar.gz', script)
        self.assertIn('https://github.com/cli/cli/releases/download/v\${version}/', script)
        self.assertIn('4c806978ffce1cec70853302a56d70ac6da4f19bae7adca4e1a8ab00633dd91d', script)
        self.assertIn('sha256sum --check --status', script)
        self.assertIn('GITHUB_PATH', script)
        self.assertNotIn('/releases/latest/', script)

if __name__ == "__main__":
    unittest.main(verbosity=2)
