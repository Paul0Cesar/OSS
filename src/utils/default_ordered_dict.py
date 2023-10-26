from collections import OrderedDict


class DefaultOrderedDict(OrderedDict):
    
    def __init__(self, default_factory=None, *args, **kwargs):
        self.default_factory = default_factory
        super().__init__(*args, **kwargs)

    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        else:
            self[key] = value = self.default_factory()
            return value