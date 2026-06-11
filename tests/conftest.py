import pytest


@pytest.fixture(scope="session")
def browser_launch_args():
    return {"headless": False}
