import pytest
import re

from incolume.py.model20220325 import __version__


__author__ = '@britodfbr'  # pragma: no cover


class TestCase:
    @pytest.mark.parametrize(
        'entrance expected'.split(),
        (
            (__version__, True),
            ('1.0.0-alpha.0', True),
        )
    )
    def test_version(self, entrance, expected):
        """Validação de versionamento semântico."""
        assert bool(re.fullmatch(r"\d+(\.\d+){2}(-?\w+\.?\d+)?", entrance, re.I)) == expected
