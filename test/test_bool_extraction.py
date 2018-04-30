
from magwitch import _boolean_args, _boolean_args_and_options


def test_positionals():
    def f(a, b:bool=True, c:bool=False):
        pass
    assert frozenset(_boolean_args(f)) == {'b', 'c'}

def test_kwonly():
    def f(a:bool, b, c:bool=False, *, d, e:bool, f:bool=True):
        pass
    assert frozenset(_boolean_args(f)) == {'a', 'c', 'e', 'f'}


def test_options_positionals():
    def f(a, b:bool=True, c:bool=False):
        pass
    assert dict(_boolean_args_and_options(f)) == {
        'b': True,
        'c': False,
    }

def test_options_kwonly():
    def f(a:bool, b, c:bool=False, *, d, e:bool, f:bool=True):
        pass
    assert dict(_boolean_args_and_options(f)) == {
        'a': True,
        'c': False,
        'e': True,
        'f': True,
    }

def test_options_default_value():
    def f(a:bool, b, c:bool=False, *, d, e:bool, f:bool=True):
        pass
    assert dict(_boolean_args_and_options(f, default_bool_value=42)) == {
        'a': 42,
        'c': False,
        'e': 42,
        'f': True,
    }
