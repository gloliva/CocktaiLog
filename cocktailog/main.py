"""
Author: Gregg Oliva
"""
# stdlib imports
import sys

# project imports
from app import app_manager

def main():
    app_manager.init_app()
    app_manager.run_app()
    return 0


# Program entrypoint
if __name__ == "__main__":
    sys.exit(main())
