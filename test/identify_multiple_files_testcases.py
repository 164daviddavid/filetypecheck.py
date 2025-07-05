import argparse
import subprocess

def test_identify_two(args: argparse.Namespace):
    expected = "test/resources/gif87_example.gif: GIF ver87a (.gif)\n" + \
               "test/resources/gif89_example.gif: GIF ver89a (.gif)\n"
    result: subprocess.CompletedProcess = subprocess.run(["python3", "filetypecheck.py", "test/resources/gif87_example.gif", "test/resources/gif89_example.gif"], capture_output=True, encoding="utf-8")

    if args.show_stderr:
        print(f"stderr:\n{result.stderr}")
    assert result.stdout == expected, f"Expected: {repr(expected)}\nActual: {repr(result.stdout)}"