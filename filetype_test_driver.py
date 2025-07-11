import argparse
from enum import StrEnum

import test.identify_single_file_testcases as sf_testcases
import test.identify_multiple_files_testcases as mf_testcases
import test.identify_with_options_testcases as o_testcases


TEXT_COLOURS = StrEnum("Text_Colour", [("GREEN", "\033[92m"), ("RED", "\033[91m"), ("RESET", "\033[0m")])

TEST_CASES = [
        sf_testcases.test_identify_doc,
        sf_testcases.test_identify_elf_ext_bin,
        sf_testcases.test_identify_elf_ext_elf,
        sf_testcases.test_identify_elf_ext_o,
        sf_testcases.test_identify_elf_ext_out,
        sf_testcases.test_identify_elf_no_ext,
        sf_testcases.test_identify_gif87,
        sf_testcases.test_identify_gif89,
        sf_testcases.test_identify_mp3,
        sf_testcases.test_identify_mp3_untagged,
        sf_testcases.test_identify_ms_ooxml,
        sf_testcases.test_identify_openssh_private_key,
        sf_testcases.test_identify_pdf,
        sf_testcases.test_identify_png,
        sf_testcases.test_identify_wav,
        sf_testcases.test_identify_webp,
        sf_testcases.test_empty_file,
        mf_testcases.test_identify_two,
        o_testcases.test_identify_matching_png,
        o_testcases.test_identify_multiple_with_non_matching,
        o_testcases.test_identify_non_matching_png,
        o_testcases.test_identify_no_format_no_ext,
        o_testcases.test_identify_has_format_no_ext,
        o_testcases.test_identify_docx,
        o_testcases.test_identify_pptx,
        o_testcases.test_identify_pptx_with_excel_embed,
        o_testcases.test_identify_xlsx,
        o_testcases.test_identify_format_has_no_ext,
        o_testcases.test_identify_non_matching_format_has_multiple_ext]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", "--quiet", action="store_true", help="do not print anything to stdout")
    parser.add_argument("-c", "--continue", action="store_true", dest="continue_", help="continue running sf_testcases even if a testcase fails")
    parser.add_argument("-s", "--show-stderr", action="store_true", help="show standard error output of program")
    parser.add_argument("-t", "--testcase", nargs="+", help="only run testcases with given names")

    args: argparse.Namespace = parser.parse_args()

    run_all = True
    if args.testcase != None:
        run_all = False

    for testcase in TEST_CASES:
        try:
            if (not run_all) and (testcase.__name__ not in args.testcase):
                continue

            testcase(args)

            if not args.quiet:
                print(f"{testcase.__name__}: {TEXT_COLOURS.GREEN}OK{TEXT_COLOURS.RESET}")

        except AssertionError as e:
            print(f"{testcase.__name__}: {TEXT_COLOURS.RED}FAILED{TEXT_COLOURS.RESET}")
            print(e)

            if not args.continue_:
                break


if __name__ == "__main__":
    main()
