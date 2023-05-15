from functools import reduce
from typing import Protocol, Dict, Any, ContextManager, Iterable, Tuple


class _ContextManagerFactory(Protocol):
    def __call__(
            self, *, title: str, params: Dict[str, Any], **kwargs
    ) -> ContextManager:
        ...


def log_with(
        *,
        context: _ContextManagerFactory,
        translations: Iterable[Tuple[str, str]] = (),
):
    def decorator_factory(wait):
        def decorator(for_):
            def decorated(fn):
                title = f'{wait.entity}: {fn}'

                def translate(initial: str, item: Tuple[str, str]):
                    old, new = item
                    return initial.replace(old, new)

                translated_title = reduce(
                    translate,
                    translations,
                    title,
                )

                with context(title=translated_title, params={}):
                    return for_(fn)

            return decorated

        return decorator

    return decorator_factory
