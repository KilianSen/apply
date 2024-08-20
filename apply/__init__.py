from typing import Callable


def Apply(on_subclass: Callable[[type, dict], None] = None,
          on_instance: Callable[[object], None] = None,
          on_del: Callable[[object], None] = None):
    class Apply:
        def __init_subclass__(cls, **kwargs):
            if on_subclass is not None:
                on_subclass(cls, **kwargs)
            return super().__init_subclass__(**kwargs)

        def __init__(self):
            if on_instance is not None:
                on_instance(self)
            super().__init__()

        def __del__(self):
            if on_del is not None:
                on_del(self)
            if hasattr(super(), '__del__'):
                super().__del__()


    return Apply