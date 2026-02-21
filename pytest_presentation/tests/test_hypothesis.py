from hypothesis import given, strategies as st
from src.my_pkg.util import add


@given(st.integers(), st.integers())
def test_add_commutative(a, b):
    assert add(a, b) == add(b, a)
