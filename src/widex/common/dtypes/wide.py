from __future__ import annotations

import attrs

from . import base


@attrs.frozen(kw_only=True)
class Wide(base.AbstractDType):
    size: int
