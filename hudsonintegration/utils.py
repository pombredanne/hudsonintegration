import os
import subprocess
import sys

# For zc.buildout's system() method:
MUST_CLOSE_FDS = not sys.platform.startswith('win')


def system(command, input=None):
    """commands.getoutput() replacement that also works on windows

    Code copied from zc.buildout.

    """
    print '[%s] %s' % (os.getcwd(), command)
    p = subprocess.Popen(command,
                         shell=True,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         close_fds=MUST_CLOSE_FDS)
    stdoutdata, stderrdata = p.communicate(input=input)
    result = stdoutdata + stderrdata
    if p.returncode:
        print "Something went wrong when executing:"
        print "    %s" % command
        print "while in directory:"
        print "    %s" % os.getcwd()
        print "Returncode:"
        print "    %s" % p.returncode
        print "Output:"
        print result
        sys.exit(1)

    print result
