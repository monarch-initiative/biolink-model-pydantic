import re

import pytest

curie_regexp = re.compile(r'^[a-zA-Z_]?[a-zA-Z_0-9-]*:([A-Za-z0-9_][A-Za-z0-9_.-]*[A-Za-z0-9_]*)?$')


@pytest.mark.parametrize(
    "curie",
    ["foo:bar", "foo:123", "foo:", "123:456", "1-2:3-4", ":"],
)
def test_valid_curie(curie):
    assert re.match(curie_regexp, curie)


@pytest.mark.parametrize(
    "curie",
    ["http://123", "://", "NotACurie"],
)
def test_invalid_curie(curie):
    assert not re.match(curie_regexp, curie)
