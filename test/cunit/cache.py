import sys
from pathlib import Path
from test.cunit import SRC
from test.cunit import CModule


CFLAGS = ["-g", "-fprofile-arcs", "-ftest-coverage"]

sys.modules[__name__] = CModule.compile(SRC / Path(__file__).stem, cflags=CFLAGS)
