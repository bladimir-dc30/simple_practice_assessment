import sys
from behave.__main__ import main as behave_main


def setup_behave():
    from behave.configuration import Configuration
    Configuration.defaults["show_timings"] = False


def run_behave_tests():
    sys.argv = ['behave']
    setup_behave()
    behave_main()


if __name__ == '__main__':
    run_behave_tests()
