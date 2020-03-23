""" Django app configuration module

    Classes:
        StatsConfig
"""

from django.apps import AppConfig


class StatsConfig(AppConfig):
    """ Django child class which identifies the name of the app """
    name = 'stats'
