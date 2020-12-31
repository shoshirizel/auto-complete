""""
Auto - Complete Project
Receives a sentence from user
and gives up to 5 completions.
Allows one mistake, omits punctuations.
"""

import get_best_completions
from cli import Cli

QUIT_REQUEST = "-1"  # The input to quit from program.


def auto_complete():
    cli = Cli()
    complete = get_best_completions.Complete()
    input_ = cli.input()
    while input_ != QUIT_REQUEST:
        cli.output(complete.get_best_completions(input_))
        input_ = cli.input()


if __name__ == '__main__':
    auto_complete()
