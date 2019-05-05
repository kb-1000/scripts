from piptools.scripts import compile as compile_, sync

import os

try:
    compile_.cli.main(("--verbose", "--allow-unsafe", "--generate-hashes", "-U", "--annotate", os.path.expanduser("requirements-py3.in")))
except SystemExit as e:
    print(e.args)
sync.cli.main(("requirements-py3.txt",))
