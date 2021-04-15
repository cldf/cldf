import sys
import contextlib

from clldutils.clilib import register_subcommands, get_parser_and_subparsers, ParserError
from clldutils.loglib import Logging

import cldfspec.commands


def main(args=None):
    parser, subparsers = get_parser_and_subparsers('cldfspec')
    register_subcommands(subparsers, cldfspec.commands)
    args = parser.parse_args(args=args)

    if not hasattr(args, "main"):
        parser.print_help()
        return 1

    with contextlib.ExitStack() as stack:
        stack.enter_context(Logging(args.log, level=args.log_level))
        try:
            return args.main(args) or 0
        except KeyboardInterrupt:  # pragma: no cover
            return 0
        except ParserError as e:
            print(e)
            return main([args._command, '-h'])
        except Exception as e:  # pragma: no cover
            raise


if __name__ == '__main__':  # pragma: no cover
    sys.exit(main() or 0)
