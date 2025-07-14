import argparse
from enum import Enum, StrEnum
import os.path
import sys
from typing import List, Sequence, Tuple
import zipfile


EXT = StrEnum("EXT", [("NO_EXT", "no ext")])

class magic_bytes(Enum):
    # From University of Houston-Clear Lake. FILE SIGNATURES TABLE
    DOC = b"\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1"
    DOC_513to516 = b"\xEC\xA5\xC1\x00"

    # From Wikipedia. Executable and Linkable Format
    ELF = b"\x7F\x45\x4C\x46"

    # From CompuServe Incorporated. (1990, July 31). Graphics Interchange Format Version 89a Specification
    GIF_ver87a = b"\x47\x49\x46\x38\x37\x61"
    GIF_ver89a = b"\x47\x49\x46\x38\x39\x61"

    # From File Recovery. JPG Signature Format: Documentation and Recovery Example
    JPG_SOI = b"\xFF\xD8" # Start of Image marker - is in all JPEGs
    JPG_EXIF_3to4 = b"\xFF\xE0" # Bytes 3-4 after JPG_SOI for JPEG/EXIF
    JPG_EXIF_IDENTIFIER_7to10 = b"\x4A\x46\x49\x46\x00" # Bytes 7-10 for JPEG/EXIF
    JPG_JFIF_3to4 = b"\xFF\xE1" # Bytes 3-4 after JPG_SOI for JPEG/JFIF
    JPG_JFIF_IDENTIFIER_7to10 = b"\x45\x78\x69\x66\x00" # Bytes 7-10 for JPEG/JFIF

    # From University of Houston-Clear Lake. FILE SIGNATURES TABLE
    # MS_OOXML can be .docx, .pptx, and .xlsx files
    # there is no subheader magic bytes to distinguish between them,
    # need to examine their contents
    MS_OOXML = b"\x50\x4B\x03\x04" # \x14\x00\x06\x00 excluded

    # From Wikipedia. MP3 File structure
    MP3_untagged = b"\xFF\xFB" # could also be tagged with ID3v1
    MP3_ID3v1 = b"\x54\x41\x47" # start of the last 128 bytes
    MP3_ID3v2 = b"\x49\x44\x33"

    OPENSSH_PRIVATE = b"\x2D\x2D\x2D\x2D\x2D\x42\x45\x47\x49\x4E\x20\x4F\x50\x45\x4E\x53\x53\x48\x20\x50\x52\x49\x56\x41\x54\x45\x20\x4B\x45\x59\x2D\x2D\x2D\x2D\x2D"

    PDF = b"\x25\x50\x44\x46\x2D"

    PNG = b"\x89\x50\x4E\x47"

    # From File Format Docs. Waveform Audio File Format
    WAV_1to4 = b"\x52\x49\x46\x46" # RIFF Four-CC
    WAV_9to12 = b"\x57\x41\x56\x45"

    # Google for Developers. WebP Container Specification
    WEBP_1to4 = b"\x52\x49\x46\x46" # RIFF Four-CC
    WEBP_9to12 = b"\x57\x45\x42\x50"

class FileType():
    def __init__(self, name: str, ext: List[str], magic: List["magic_bytes"]):
        self.name = name
        self.ext = ext
        self.magic = magic

    def get_name() -> str:
        return self.name

    def get_ext() -> List[str]:
        return self.ext


def identify_file_type(header: bytes) -> Tuple[FileType] | None:
    #
    # Note: an IndexError will not occur from slicing outside of bounds
    # so no check is performed here
    #
    if header[0:8] == magic_bytes.DOC.value and header[512:516] == magic_bytes.DOC_513to516.value:
        return (FileType("Microsoft Word 97-2003", [".doc"], [magic_bytes.DOC, magic_bytes.DOC_513to516]),)

    if header[0:4] == magic_bytes.ELF.value:
        return (FileType("Executable and Linkable Format", ["no ext", ".axf", ".bin", ".elf", ".o", ".out", ".prx", ".puff", ".ko", ".mod", ".so"], [magic_bytes.ELF]),)

    if header[0:6] == magic_bytes.GIF_ver87a.value:
        return (FileType("GIF ver87a", [".gif"], [magic_bytes.GIF_ver87a]),)

    if header[0:6] == magic_bytes.GIF_ver89a.value:
        return (FileType("GIF ver89a", [".gif"], [magic_bytes.GIF_ver89a]),)

    if header[0:2] == magic_bytes.JPG_SOI.value and header[2:4] == magic_bytes.JPG_EXIF_3to4.value and header[6:10] == magic_bytes.JPG_EXIF_IDENTIFIER_7to10.value:
        return (FileType("JPEG/EXIF", [".jpg"], [magic_bytes.JPG_SOI, magic_bytes.JPG_EXIF_3to4, magic_bytes.JPG_EXIF_IDENTIFIER_7to10]),)

    if header[0:2] == magic_bytes.JPG_SOI.value and header[2:4] == magic_bytes.JPG_JFIF_3to4.value and header[6:10] == magic_bytes.JPG_JFIF_IDENTIFIER_7to10.value:
        return (FileType("JPEG/JFIF", [".jpg"], [magic_bytes.JPG_SOI, magic_bytes.JPG_JFIF_3to4, magic_bytes.JPG_JFIF_IDENTIFIER_7to10]),)

    if header[0:2] == magic_bytes.MP3_untagged.value:
        return (FileType("MP3 without ID3v2 tag", [".mp3"], [magic_bytes.MP3_untagged]),)

    if header[0:3] == magic_bytes.MP3_ID3v2.value:
        return (FileType("MP3 with ID3v2 tag", [".mp3"], [magic_bytes.MP3_ID3v2]),)

    if header[0:4] == magic_bytes.MS_OOXML.value:
        return (FileType("Microsoft Open Office XML Format", [".docx", ".pptx", ".xlsx"], [magic_bytes.MS_OOXML]),)

    if header[0:35] == magic_bytes.OPENSSH_PRIVATE.value:
        return (FileType("OpenSSH Private Key", ["no ext"], [magic_bytes.OPENSSH_PRIVATE]),)

    if header[0:5] == magic_bytes.PDF.value:
        return (FileType("Portable Document Format", [".pdf"], [magic_bytes.PDF]),)

    if header[0:4] == magic_bytes.PNG.value:
        return (FileType("Portable Network Graphics Format", [".png"], [magic_bytes.PNG]),)
    
    if header[0:4] == magic_bytes.WAV_1to4.value and header[8:12] == magic_bytes.WAV_9to12.value:
        return (FileType("Waveform Audio Format", [".wav"], [magic_bytes.WAV_1to4, magic_bytes.WAV_9to12]),)
    
    if header[0:4] == magic_bytes.WEBP_1to4.value and header[8:12] == magic_bytes.WEBP_9to12.value:
        return (FileType("WebP", [".webp"], [magic_bytes.WEBP_1to4, magic_bytes.WEBP_9to12]),)
    return None

def get_first_component(filepath: str) -> str:
    components = filepath.split("/")

    if len(components) == 0:
        return ""
    return components[0]

def identify_msooxml(filepath: str) -> FileType | None:
    ftype = None
    try:
        zf = zipfile.ZipFile(filepath)
    except zipfile.BadZipFile:
        return None

    for filename in zf.namelist():
        match get_first_component(filename):
            case "word":
                ftype = FileType("Microsoft Word 2007+", [".docx"], [magic_bytes.GIF_ver89a])
                break

            case "ppt":
                ftype = FileType("Microsoft PowerPoint 2007+", [".pptx"], [magic_bytes.GIF_ver89a])
                break

            case "xl":
                ftype = FileType("Microsoft Excel 2007+", [".xlsx"], [magic_bytes.GIF_ver89a])
                break

    zf.close()
    return ftype

def has_matching_extension(filepath: str, filetypes: Sequence["FileType"]) -> bool:
    ext: str = os.path.splitext(filepath)[1]

    if ext == "":
        ext = EXT.NO_EXT

    for filetype in filetypes:
        if ext in filetype.get_ext():
            return True
    return False

def generate_ext_output_str(extensions: Sequence[str]) -> str:
    """Generates a string containing all extensions inside
    <extensions> separated by a comma and space.

    E.g. [".bin", ".elf"] |-> ".bin, .elf"
    """
    output: str = ""

    i = 0
    while i < len(extensions):
        ext: str = extensions[i]

        output += ext

        if i != (len(extensions) - 1):
            output += ", "
        i += 1
    return output

def print_filetypes(filepath: str, filetypes: Sequence["FileType"]) -> None:
    print(f"{filepath}: ", end="")

    i = 0
    while i < len(filetypes):
        filetype: FileType = filetypes[i]

        extensions: str = generate_ext_output_str(filetype.get_ext())

        if len(filetypes) == 1:
            print(f"{filetype.get_name()} ({extensions})")
            break

        if i + 1 == len(filetypes):
            print(f" or {filetype.get_name()} ({extensions})")
        
        else:
            print(f"{filetype.get_name()} ({extensions}),", end="")

        i += 1

def contains_filetype(name: str, ftypes: Sequence["FileType"]) -> bool:
    for ftype in ftypes:
        if name == ftype.get_name():
            return True
    return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--non-matching", action="store_true", help="only show files whose file extension does not match their magic bytes; files with no file extensions will always be shown")
    parser.add_argument("--msooxml", action="store_true", help="try to identify the specific type of any files with msooxml magic bytes by unzipping them")
    parser.add_argument("filepaths", nargs="+")

    args: argparse.Namespace = parser.parse_args()

    for filepath in args.filepaths:
        try:
            with open(filepath, "rb") as file:

                line: bytes = file.readline()

                ftypes: Tuple[FileType] | None = identify_file_type(line)

                if ftypes == None:
                    print(f"Could not identify file type for: {filepath}")
                    continue
                
                if args.msooxml and contains_filetype("Microsoft Open Office XML Format", ftypes):
                    msooxml_type: FileType | None = identify_msooxml(filepath)
                    if msooxml_type != None:
                        ftypes = (msooxml_type,)

                if args.non_matching and has_matching_extension(filepath, ftypes):
                    continue

                print_filetypes(filepath, ftypes)


        except OSError as e:
            print(f"{filepath}: {e.strerror}", file=sys.stderr)
            sys.exit(1)




if __name__ == "__main__":
    main()
