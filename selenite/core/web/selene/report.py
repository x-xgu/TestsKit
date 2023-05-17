from functools import reduce
from typing import Protocol, Dict, Any, ContextManager, Iterable, Tuple, Callable


class _ContextManagerFactory(Protocol):
    def __call__(
            self, *, title: str, params: Dict[str, Any], **kwargs
    ) -> ContextManager:
        ...


def log_with(
        *,
        context: _ContextManagerFactory,
        translations: Iterable[Tuple[str, str]] = (),
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Decorator factory that logs function calls with a context manager.

    Args:
        context: A factory that returns a context manager.
        translations: A list of tuples of strings to replace in the log title.

    Returns:
        A decorator that logs function calls with the given context manager.

    Example:
        >>> @log_with(context=MyContextManager)
        ... def my_function():
        ...     pass
    """
    def decorator_factory(wait: Any) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        def decorator(for_: Any) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
            def decorated(fn: Callable[..., Any]) -> Callable[..., Any]:
                title = f'{wait.entity}: {fn}'

                def translate(initial: str, item: Tuple[str, str]) -> str:
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
