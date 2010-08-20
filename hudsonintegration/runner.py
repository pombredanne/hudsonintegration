import os
import sys

from hudsonintegration.utils import system

# /var/lib/hudson/jobs/lizard-map/workspace/trunk


def bin_dir():
    """Return the directory of the hudsonintegration buildout."""
    our_script = sys.argv[0]
    pathname = os.path.dirname(our_script)
    return os.path.abspath(pathname)


def go_to_checkout():
    """Go to the directory with the actual checkout."""
    # We're in the workspace with one directory: the checkout.
    contents = os.listdir('.')
    assert len(contents) == 1
    os.chdir(contents[0])


def run_tests():
    go_to_checkout()
    system("python bootstrap.py -d")
    system("bin/buildout -v")
    coverage = os.path.join(bin_dir(), 'coverage')
    system("%s run bin/test" % coverage)
    sys.exit(0)


def create_reports():
    go_to_checkout()
    coverage = os.path.join(bin_dir(), 'coverage')
    pep8 = os.path.join(bin_dir(), 'pep8')
    pyflakes = os.path.join(bin_dir(), 'pyflakes')
    system(("%s lizard_sticky | " +
            "perl -ple 's/: ([WE]\\d+)/: [$1]/' > pep8.txt") % pep8)
    system(("%s lizard_sticky | " +
            "perl -ple 's/:\\ /: [E] /' >> pep8.txt") % pyflakes)
    system("%s xml" % coverage)
    sys.exit(0)
