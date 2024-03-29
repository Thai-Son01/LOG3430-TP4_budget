import os

GOOD = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"
BAD = "HEAD"
COMMAND = "python3 manage.py test"

os.system(f"git bisect start {BAD} {GOOD}")
os.system(f"git bisect run {COMMAND}")