"""A sub-package: a package inside a package. Nesting can go as deep as you like.

Most real __init__.py files are this small, or empty.
"""

from .badges import badge_for

__all__ = ["badge_for"]
