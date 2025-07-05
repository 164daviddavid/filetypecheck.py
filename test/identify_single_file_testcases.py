import argparse
import subprocess

def test_identify_doc(args: argparse.Namespace):
    expected = "test/resources/doc_example.doc: Microsoft Word 97-2003 (.doc)\n"
    result: subprocess.CompletedProcess = subprocess.run(["python3", "filetypecheck.py", "test/resources/doc_example.doc"], capture_output=True, encoding="utf-8")

    if args.show_stderr:
        print(f"stderr:\n{result.stderr}")
    assert result.stdout == expected, f"Expected: {repr(expected)}\nActual: {repr(result.stdout)}"

def test_identify_gif87(args: argparse.Namespace):
    expected = "test/resources/gif87_example.gif: GIF ver87a (.gif)\n"
    result: subprocess.CompletedProcess = subprocess.run(["python3", "filetypecheck.py", "test/resources/gif87_example.gif"], capture_output=True, encoding="utf-8")

    if args.show_stderr:
        print(f"stderr:\n{result.stderr}")
    assert result.stdout == expected, f"Expected: {repr(expected)}\nActual: {repr(result.stdout)}"

def test_identify_gif89(args: argparse.Namespace):
    expected = "test/resources/gif89_example.gif: GIF ver89a (.gif)\n"
    result: subprocess.CompletedProcess = subprocess.run(["python3", "filetypecheck.py", "test/resources/gif89_example.gif"], capture_output=True, encoding="utf-8")

    if args.show_stderr:
        print(f"stderr:\n{result.stderr}")
    assert result.stdout == expected, f"Expected: {repr(expected)}\nActual: {repr(result.stdout)}"

def test_identify_mp3(args: argparse.Namespace):
    expected = "test/resources/mp3_example.mp3: MP3 with ID3v2 tag (.mp3)\n"
    result: subprocess.CompletedProcess = subprocess.run(["python3", "filetypecheck.py", "test/resources/mp3_example.mp3"], capture_output=True, encoding="utf-8")

    if args.show_stderr:
        print(f"stderr:\n{result.stderr}")
    assert result.stdout == expected, f"Expected: {repr(expected)}\nActual: {repr(result.stdout)}"

def test_identify_mp3_untagged(args: argparse.Namespace):
    expected = "test/resources/mp3_untagged_example.mp3: MP3 without ID3v2 tag (.mp3)\n"
    result: subprocess.CompletedProcess = subprocess.run(["python3", "filetypecheck.py", "test/resources/mp3_untagged_example.mp3"], capture_output=True, encoding="utf-8")

    if args.show_stderr:
        print(f"stderr:\n{result.stderr}")
    assert result.stdout == expected, f"Expected: {repr(expected)}\nActual: {repr(result.stdout)}"

def test_identify_ms_ooxml(args: argparse.Namespace):
    expected = "test/resources/docx_example.docx: Microsoft Open Office XML Format (.docx, .pptx, .xlsx)\n"
    result: subprocess.CompletedProcess = subprocess.run(["python3", "filetypecheck.py", "test/resources/docx_example.docx"], capture_output=True, encoding="utf-8")

    if args.show_stderr:
        print(f"stderr:\n{result.stderr}")
    assert result.stdout == expected, f"Expected: {repr(expected)}\nActual: {repr(result.stdout)}"

def test_identify_pdf(args: argparse.Namespace):
    expected = "test/resources/pdf_example.pdf: Portable Document Format (.pdf)\n"
    result: subprocess.CompletedProcess = subprocess.run(["python3", "filetypecheck.py", "test/resources/pdf_example.pdf"], capture_output=True, encoding="utf-8")

    if args.show_stderr:
        print(f"stderr:\n{result.stderr}")
    assert result.stdout == expected, f"Expected: {repr(expected)}\nActual: {repr(result.stdout)}"

def test_identify_png(args: argparse.Namespace):
    expected = "test/resources/png_example.png: Portable Network Graphics Format (.png)\n"
    result: subprocess.CompletedProcess = subprocess.run(["python3", "filetypecheck.py", "test/resources/png_example.png"], capture_output=True, encoding="utf-8")

    if args.show_stderr:
        print(f"stderr:\n{result.stderr}")
    assert result.stdout == expected, f"Expected: {repr(expected)}\nActual: {repr(result.stdout)}"

def test_identify_wav(args: argparse.Namespace):
    expected = "test/resources/wav_example.wav: Waveform Audio Format (.wav)\n"
    result: subprocess.CompletedProcess = subprocess.run(["python3", "filetypecheck.py", "test/resources/wav_example.wav"], capture_output=True, encoding="utf-8")

    if args.show_stderr:
        print(f"stderr:\n{result.stderr}")
    assert result.stdout == expected, f"Expected: {repr(expected)}\nActual: {repr(result.stdout)}"

def test_identify_webp(args: argparse.Namespace):
    expected = "test/resources/webp_example.webp: WebP (.webp)\n"
    result: subprocess.CompletedProcess = subprocess.run(["python3", "filetypecheck.py", "test/resources/webp_example.webp"], capture_output=True, encoding="utf-8")

    if args.show_stderr:
        print(f"stderr:\n{result.stderr}")
    assert result.stdout == expected, f"Expected: {repr(expected)}\nActual: {repr(result.stdout)}"



def test_empty_file(args: argparse.Namespace):
    expected = "Could not identify file type for: test/resources/empty_file\n"
    result: subprocess.CompletedProcess = subprocess.run(["python3", "filetypecheck.py", "test/resources/empty_file"], capture_output=True, encoding="utf-8")

    if args.show_stderr:
        print(f"stderr:\n{result.stderr}")
    assert result.stdout == expected, f"Expected: {repr(expected)}\nActual: {repr(result.stdout)}"