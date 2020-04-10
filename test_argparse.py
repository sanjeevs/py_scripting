# Test out the argparse module for cmd line processing.
# Note that -h is used by the module and so should not be used by test.

import unittest
import argparse

class TestArgParse(unittest.TestCase):

    def test_position(self):
        """Positional arguments are required args. They must be in order.
        """
        sys_argv = ["hello", "100"]
        parser = argparse.ArgumentParser(description="Test out position")
        parser.add_argument("pos1", help="Provide first positional arg")
        parser.add_argument("num", type=int, help="Provide second positional arg")
        argv = parser.parse_args(sys_argv)
        self.assertEqual(argv.pos1, "hello")
        self.assertEqual(argv.num, 100)

    def test_options(self):
        """Optional args are identified by single or double dash.
        """
        sys_argv = ["-n", "hello", "--age", "20"]
        parser = argparse.ArgumentParser(description="Test out option")
        parser.add_argument("-n", "--name", help="Provide name arg")
        parser.add_argument("-a", "--age", type=int, help="Provide age")
        parser.add_argument("-", "--sex", default="male", help="Default value of sex is male")
        argv = parser.parse_args(sys_argv)
        self.assertEqual(argv.name, "hello")
        self.assertEqual(argv.age, 20)
        self.assertEqual(argv.sex, "male")
     
    def test_default_flag(self):
        """Check the default value of flags.
        """
        sys_argv = []
        parser = argparse.ArgumentParser(description="Test out option")
        parser.add_argument("-q", "--quiet", action="store_true")
        argv = parser.parse_args(sys_argv)
        self.assertFalse(argv.quiet)
        
    def test_flag(self):
        """Pass flags to command line.
        """
        sys_argv = ["-q"]
        parser = argparse.ArgumentParser(description="Test out option")
        parser.add_argument("-q", "--quiet", action="store_true")
        argv = parser.parse_args(sys_argv)
        self.assertTrue(argv.quiet)
       
    def test_exclusive_args(self):
        """Specify either verbose or quiet option.
        """
        sys_argv = ["-q", '-v']
        parser = argparse.ArgumentParser(description="Test out option")
        group = parser.add_mutually_exclusive_group()
        group.add_argument("-q", "--quiet", action="store_true")
        group.add_argument("-v", "--verbose", action="store_true", help="print quiet")
        self.assertRaises(SystemExit, parser.parse_args, sys_argv)
        
if __name__ == "__main__":
    unittest.main()
