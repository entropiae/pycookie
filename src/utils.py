# -*- coding: utf-8 -*-

import yaml

from logging import config


def configure_logging(log_settings):
    with open(log_settings) as f:
        log_conf = yaml.load(f)
    config.dictConfig(log_conf)


def retrieve_configuration(conf_filename):
    with open(conf_filename) as f:
        conf = yaml.load(f)
    return conf
