import attrs
from attrs import validators

from . import base


@attrs.frozen(kw_only=True)
class Array(base.AbstractDType):
    size: int = attrs.field(
        validator=validators.gt(0),
    )
    granularity: int = attrs.field(
        validator=validators.gt(0),
        default=1,
    )
