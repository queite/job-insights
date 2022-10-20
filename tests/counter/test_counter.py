import json
from unittest.mock import mock_open, patch

from src.counter import count_ocurrences


def test_counter():
    phrase = [{"info": "So many books, so little time."}]
    with patch("builtins.open", mock_open(read_data=json.dumps(phrase))):
        assert count_ocurrences("path", "so") == 2
