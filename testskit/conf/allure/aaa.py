from testskit.conf.allure import gherkin


def arrange(description: str):
    """
    Arrange step is used to describe the initial context of the system - the scene of the scenario.
    """
    return gherkin.given(description)


def act(description: str):
    """
    Act step is used to describe an event - an action that occurs in the scene.
    """
    return gherkin.when(description)


def assert_(description: str):
    """
    Assert step is used to describe an expected outcome, or result, of the event.
    """
    return gherkin.then(description)
