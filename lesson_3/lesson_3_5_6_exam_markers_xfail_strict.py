# pytest -rX -v lesson_3_5_6_exam_markers_xfail.py - запустить тест

import pytest


@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False