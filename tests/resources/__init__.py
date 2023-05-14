from pathlib import Path


def path(relative: str) -> str:
    """
    Returns the absolute path of a file relative to this file.
    """
    return str(
        Path(__file__).parent.joinpath(relative).absolute()
    )


def url(relative_path: str) -> str:
    """
    Returns the absolute path of a file relative to this file.
    """
    return f'file://{path(relative_path)}'
