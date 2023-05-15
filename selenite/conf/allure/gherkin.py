from typing import Optional

from selenite.conf.allure import report


def _step(description: Optional[str] = None):
    """
    Decorator for steps in BDD scenarios.
    """
    def decorated(fn):
        if description:
            fn.__name__ = description.replace(' ', '_')
        return report.step(fn, display_context=False)()

    return decorated


def given(precondition: Optional[str] = None):
    """
    Given step is used to describe the initial context of the system - the scene of the scenario.
    """
    return _step(precondition)


def when(act: Optional[str] = None):
    """
    When step is used to describe an event - an action that occurs in the scene.
    """
    return _step(act)


def then(assertion: Optional[str] = None):
    """
    Then step is used to describe an expected outcome, or result, of the event.
    """
    return _step(assertion)
