from io import StringIO
import sys

from src.cli import main


def run_cli(args):
    # capture stdout
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        code = main(args)
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    return code, output


def test_list_formatting_and_done_error():
    # empty args prints usage and returns 1
    code, output = run_cli([])
    assert code == 1
    assert "Usage:" in output

    # add two tasks then list
    run_cli(["add", "Buy milk"])  # code ignored; repository is in-process
    run_cli(["add", "Walk dog"])  # adds second
    code, output = run_cli(["list"])  # lists current in-memory state
    assert code == 0
    lines = output.strip().splitlines()
    assert lines[0].startswith("1. [ ] Buy milk")
    assert lines[1].startswith("2. [ ] Walk dog")

    # done with non-integer
    code, output = run_cli(["done", "abc"])
    assert code == 1
    assert "must be an integer" in output
