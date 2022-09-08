import click
import sys

from staking_deposit.cli.existing_mnemonic import existing_mnemonic
from staking_deposit.cli.new_mnemonic import new_mnemonic
from staking_deposit.utils.click import (
    captive_prompt_callback,
    choice_prompt_func,
    jit_option,
)
from staking_deposit.utils import config
from staking_deposit.utils.constants import INTL_LANG_OPTIONS
from staking_deposit.utils.intl import (
    get_first_options,
    fuzzy_reverse_dict_lookup,
    load_text,
)


def check_python_version() -> None:
    '''
    Checks that the python version running is sufficient and exits if not.
    '''
    if sys.version_info < (3, 7):
        click.pause(load_text(['err_python_version']))
        sys.exit()


@click.group()
@click.pass_context
@click.option(
    '--non_interactive',
    default=False,
    is_flag=True,
    help='Disables interactive prompts.',
    hidden=True,
)
def cli(ctx: click.Context, non_interactive: bool) -> None:
    config.language = "en"
    config.non_interactive = non_interactive  # Remove interactive commands


cli.add_command(existing_mnemonic)
cli.add_command(new_mnemonic)


if __name__ == '__main__':
    check_python_version()
    cli()
