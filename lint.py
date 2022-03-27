"""Module contain pylint checker."""

import argparse
import logging
import sys
from pylint.lint import Run

logging.getLogger().setLevel(logging.INFO)


def check_pylint():
    """Do checks that the project passes all pylint checks."""
    parser = argparse.ArgumentParser(prog="LINT")

    parser.add_argument(
        "-p",
        "--path",
        help="path to directory you want to run pylint | "
        "Default: %(default)s | "
        "Type: %(type)s ",
        default="./src",
        type=str,
    )

    parser.add_argument(
        "-t",
        "--threshold",
        help="score threshold to fail pylint runner | "
        "Default: %(default)s | "
        "Type: %(type)s ",
        default=10,
        type=float,
    )

    args = parser.parse_args()
    path = str(args.path)
    threshold = float(args.threshold)

    logging.info("PyLint Starting | Path: %s | Threshold: %s", path, threshold)

    results = Run([path], do_exit=False)

    final_score = results.linter.stats.global_note

    if final_score < threshold:
        message = "PyLint Failed | Score: %s | Threshold: %s"
        logging.error(message, final_score, threshold)
        raise Exception(message)

    logging.info(
        "PyLint Passed | Score: %s | Threshold: %s", final_score, threshold
    )
    sys.exit(0)


if __name__ == "__main__":
    check_pylint()
