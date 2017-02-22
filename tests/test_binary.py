from .context import binary

def test_first():
    binry = binary.Binary(6);
    assert int(binry) == 6
