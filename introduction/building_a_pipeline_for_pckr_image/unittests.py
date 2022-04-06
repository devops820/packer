
class Test(unittest.TestCase):

    def setUp(self):
        self.host = testinfra.get_host("localhost")

    def test_jenkins_is_installed():
        jenkins = self.host.package("jenkins")
        self.assertTrue(jenkins.is_running)
        self.assertTrue(jenkins.is_installed)
        self.assertTrue(jenkins.version.startswith("2.1"))

    def test_jenkins_running_and_enabled():
        jenkins = self.host.service("jenkins")
        self.assertTrue(jenkins.is_running)
        self.assertTrue(jenkins.is_enabled)

    def test_ansible_is_installed():
        ansible = self.host.package("ansible")
        self.assertTrue(ansible.is_installed)
        self.assertTrue(ansible.version.startswith("2.6"))

    def test_packer_in_path():
        packer = self.host.exists("packer")
        self.assertTrue(packer)


if __name__ == "__main__":
    unittest.main()