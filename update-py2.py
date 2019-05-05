from piptools.scripts import compile as compile_, sync

import os

try:
    compile_.cli.main(("--verbose", "--allow-unsafe", "--generate-hashes", "-U", "--annotate", os.path.expanduser("requirements-py2.in")))
except SystemExit as e:
    print(e.args)
sync.cli.main(("requirements-py2.txt",))
