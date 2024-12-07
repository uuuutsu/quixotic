import typing


def impl[I: type[typing.Any]](prot: I) -> typing.Callable[[I], I]:
    return lambda cls: cls
