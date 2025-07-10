import argparse
import subprocess

def test_identify_matching_png(args: argparse.Namespace):
    expected = ""
    result: subprocess.CompletedProcess = subprocess.run(["python3", "filetypecheck.py", "--non-matching", "test/resources/png_example.png"], capture_output=True, encoding="utf-8")

    if args.show_stderr:
        print(f"stderr:\n{result.stderr}")
    assert result.stdout == expected, f"Expected: {repr(expected)}\nActual: {repr(result.stdout)}"

def test_identify_non_matching_png(args: argparse.Namespace):
    expected = "test/resources/non_matching_png_example.jpg: Portable Network Graphics Format (.png)\n"
    result: subprocess.CompletedProcess = subprocess.run(["python3", "filetypecheck.py", "--non-matching", "test/resources/non_matching_png_example.jpg"], capture_output=True, encoding="utf-8")

    if args.show_stderr:
        print(f"stderr:\n{result.stderr}")
    assert result.stdout == expected, f"Expected: {repr(expected)}\nActual: {repr(result.stdout)}"

def test_identify_multiple_with_non_matching(args: argparse.Namespace):
    expected = "test/resources/non_matching_png_example.jpg: Portable Network Graphics Format (.png)\n"
    result: subprocess.CompletedProcess = subprocess.run(["python3", "filetypecheck.py", "--non-matching", "test/resources/png_example.png", "test/resources/pdf_example.pdf", "test/resources/non_matching_png_example.jpg", "test/resources/webp_example.webp"], capture_output=True, encoding="utf-8")

    if args.show_stderr:
        print(f"stderr:\n{result.stderr}")
    assert result.stdout == expected, f"Expected: {repr(expected)}\nActual: {repr(result.stdout)}"

def test_identify_no_format_no_ext(args: argparse.Namespace):
    expected = "Could not identify file type for: test/resources/empty_file\n"
    result: subprocess.CompletedProcess = subprocess.run(["python3", "filetypecheck.py", "--non-matching", "test/resources/empty_file"], capture_output=True, encoding="utf-8")

    if args.show_stderr:
        print(f"stderr:\n{result.stderr}")
    assert result.stdout == expected, f"Expected: {repr(expected)}\nActual: {repr(result.stdout)}"

def test_identify_has_format_no_ext(args: argparse.Namespace):
    expected = "test/resources/no_ext_png_example: Portable Network Graphics Format (.png)\n"
    result: subprocess.CompletedProcess = subprocess.run(["python3", "filetypecheck.py", "--non-matching", "test/resources/no_ext_png_example"], capture_output=True, encoding="utf-8")

    if args.show_stderr:
        print(f"stderr:\n{result.stderr}")
    assert result.stdout == expected, f"Expected: {repr(expected)}\nActual: {repr(result.stdout)}"

def test_identify_format_has_no_ext(args: argparse.Namespace):
    """Tests whether the program shows output for a file that has
    no extension and is of a format that has no extension. For example,
    the ELF format has a variety of file extensions as well as no extension.
    """
    expected = ""
    result: subprocess.CompletedProcess = subprocess.run(["python3", "filetypecheck.py", "--non-matching", "test/resources/elf_example"], capture_output=True, encoding="utf-8")

    if args.show_stderr:
        print(f"stderr:\n{result.stderr}")
    assert result.stdout == expected, f"Expected: {repr(expected)}\nActual: {repr(result.stdout)}"

def test_identify_non_matching_format_has_multiple_ext(args: argparse.Namespace):
    """Tests whether the program shows output for a file that has
    a non matching extension and is of a format that has multiple extensions. For example,
    the ELF format has a variety of file extensions.
    """
    expected = "test/resources/elf_example.png: Executable and Linkable Format (no ext, .axf, .bin, .elf, .o, .out, .prx, .puff, .ko, .mod, .so)\n"
    result: subprocess.CompletedProcess = subprocess.run(["python3", "filetypecheck.py", "--non-matching", "test/resources/elf_example.png"], capture_output=True, encoding="utf-8")

    if args.show_stderr:
        print(f"stderr:\n{result.stderr}")
    assert result.stdout == expected, f"Expected: {repr(expected)}\nActual: {repr(result.stdout)}"

def test_identify_docx(args: argparse.Namespace):
    expected = "test/resources/docx_example.docx: Microsoft Word 2007+ (.docx)\n"
    result: subprocess.CompletedProcess = subprocess.run(["python3", "filetypecheck.py", "--msooxml", "test/resources/docx_example.docx"], capture_output=True, encoding="utf-8")

    if args.show_stderr:
        print(f"stderr:\n{result.stderr}")
    assert result.stdout == expected, f"Expected: {repr(expected)}\nActual: {repr(result.stdout)}"

def test_identify_pptx(args: argparse.Namespace):
    expected = "test/resources/pptx_example.pptx: Microsoft PowerPoint 2007+ (.pptx)\n"
    result: subprocess.CompletedProcess = subprocess.run(["python3", "filetypecheck.py", "--msooxml", "test/resources/pptx_example.pptx"], capture_output=True, encoding="utf-8")

    if args.show_stderr:
        print(f"stderr:\n{result.stderr}")
    assert result.stdout == expected, f"Expected: {repr(expected)}\nActual: {repr(result.stdout)}"

def test_identify_pptx_with_excel_embed(args: argparse.Namespace):
    expected = "test/resources/pptx_embed_excel_example.pptx: Microsoft PowerPoint 2007+ (.pptx)\n"
    result: subprocess.CompletedProcess = subprocess.run(["python3", "filetypecheck.py", "--msooxml", "test/resources/pptx_embed_excel_example.pptx"], capture_output=True, encoding="utf-8")

    if args.show_stderr:
        print(f"stderr:\n{result.stderr}")
    assert result.stdout == expected, f"Expected: {repr(expected)}\nActual: {repr(result.stdout)}"

def test_identify_xlsx(args: argparse.Namespace):
    expected = "test/resources/xlsx_example.xlsx: Microsoft Excel 2007+ (.xlsx)\n"
    result: subprocess.CompletedProcess = subprocess.run(["python3", "filetypecheck.py", "--msooxml", "test/resources/xlsx_example.xlsx"], capture_output=True, encoding="utf-8")

    if args.show_stderr:
        print(f"stderr:\n{result.stderr}")
    assert result.stdout == expected, f"Expected: {repr(expected)}\nActual: {repr(result.stdout)}"

