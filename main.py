# -*- coding: utf-8 -*-

import os
import argparse
import logging

current_directory = os.path.dirname(os.path.abspath(__file__))
log_settings = os.path.join(current_directory, 'settings', 'logging.yaml')

from src.utils import configure_logging, retrieve_configuration

configure_logging(log_settings)
log = logging.getLogger(__name__)


def build_cli_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--conf',
        help='Configuration file path',
        required=True
    )

    parser.add_argument(
        '--debug',
        help='Enable debug mode',
        action='store_true'
    )
    return parser


def parse_cli_args():
    parser = build_cli_parser()
    cli_args = parser.parse_args()
    return cli_args


def main():
    cli_args = parse_cli_args()

    if cli_args.debug:
        log.setLevel(logging.DEBUG)
        log.debug('Running in debug mode')

    conf = retrieve_configuration(cli_args.conf)
    log.debug('Configuration loaded: {}'.format(conf))


if __name__ == '__main__':
    main()
