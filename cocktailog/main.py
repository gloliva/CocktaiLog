"""
Author: Gregg Oliva
"""
# stdlib imports
import sys

# project imports
from app import Cocktailog

# mypy imports
from typing import Optional


def main() -> Optional[int]:
    app = Cocktailog()
    app.setup()
    app.run()
    return app.return_code


# Program entrypoint
if __name__ == "__main__":
    sys.exit(main() or 0)
