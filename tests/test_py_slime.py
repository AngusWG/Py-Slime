#!/usr/bin/python3
# encoding: utf-8

"""
test_py_slime
----------------------------------

Tests for `py_slime` module.
"""
import pytest
import py_slime


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')



class TestPy_slime:

    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def test_something(self):
        assert py_slime.__version__
