# Jedis
# Code Json like Redis easier
# t.me/Kobsser

__version__ = "1.0"
__author__ = "Kobsser"
__copyright__ = "Copyright (C) 2021 Kobsser"

from .jedis import jedis
from helpers import FileHelper

__all__ = [
    "jedis", 'FileHelper'
]
