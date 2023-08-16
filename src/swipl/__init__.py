import os
import subprocess
import sys

HOME = os.path.dirname(__file__)
BIN  = os.path.join(HOME, "bin")

def _program(name, args):
    return subprocess.call([os.path.join(BIN, name)] + args, close_fds=False)

def swipl():
    raise SystemExit(_program('swipl', sys.argv[1:]))

def swipl_ld():
    raise SystemExit(_program('swipl-ld', sys.argv[1:]))
