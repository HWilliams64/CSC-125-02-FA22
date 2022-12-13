import typing # Go and get the python module named typing

def function(x: typing.Iterable[int], y: int) -> float:
    return sum(x) * y


print(function(range(10), 4))
