import environ

from .common import *  # noqa

environ.Env.read_env('.env')
