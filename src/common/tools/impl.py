import typing


def impl[I: type[typing.Any]](_prot: I) -> typing.Callable[[I], I]:
    return lambda cls: cls
