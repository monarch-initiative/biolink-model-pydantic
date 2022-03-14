import re

import pytest

from pydanticgen.pydanticgen import PydanticGen

curie_regexp = re.compile(PydanticGen.curie_regexp)


@pytest.mark.parametrize(
    "curie",
    [
        "foo:bar",
        "foo:123",
        "foo:",
        "123:456",
        "1-2:3-4",
        ":",
        "D:1.1/a.bcd.1900.1.1",
        "DOI:10.10/06-11(22)33-1",
        "DOI:10.1002/(SICI)1097-0061(19980430)14:6<551::AID-YEA260>3.0.CO;2-Q",
        "A.B:12345",
    ],
)
def test_valid_curie(curie):
    assert re.match(curie_regexp, curie)


@pytest.mark.parametrize(
    "curie",
    ["http://123", "://", "NotACurie"],
)
def test_invalid_curie(curie):
    assert not re.match(curie_regexp, curie)
