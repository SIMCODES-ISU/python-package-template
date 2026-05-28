import argparse
import logging
import sys

from .. import __version__
from ..hello import hello_world

logger = logging.getLogger(__name__)


def parse_args(args: list[str]) -> argparse.Namespace:
    """Parses all command line arguments.

    :param args: Command line arguments to be parsed.
    :type args: list[str]
    :return: Parsed command line arguments
    :rtype: argparse.Namespace
    """
    parser = argparse.ArgumentParser(description="Example CLI program")

    # Positional arguments
    # parser.add_argument("file", nargs="?")

    # Optional flags
    parser.add_argument(
        "--version",
        action="store_true",
        help="Output version information and exit.",
    )

    return parser.parse_args()


def main(argv: list[str]) -> int:
    """Entry point of the program.

    :param argv: Command line argument values.
    :type argv: list[str]
    :return: Return code; should use values in range [0, 255]
    :rtype: int
    """
    args = parse_args(argv)

    # Print version and exit
    if args.version:
        print(__version__)
        return 0

    print(hello_world())

    return 0


def run() -> int:
    """Entry point of program that provides command line arguments.

    As opposed to ``main()``, this function is suitable for use in
    ``pyproject.toml:project.scripts`` entries since it has no parameters.

    :return: return code; should use values in range [0, 255]
    :rtype: int
    """
    return main(sys.argv[1:])


if __name__ == "__main__":
    sys.exit(run())
