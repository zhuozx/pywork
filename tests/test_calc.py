import pytest

from test_pytest.core.calc import Calc


class TestCalc:
    def setup_class(self):
        self.calc = Calc()

    #正常
    @pytest.mark.parametrize("a,b,c", [
        [0, 1, 0],
        [2, 2, 4],
        [1, 2, 0.5],
        [1,100000000,0.00000001],
        [0.000000001,0.000000001,1]
    ])
    def test_div(self, a, b, c):
        assert self.calc.div(a,b) == c

    #异常值
    @pytest.mark.parametrize("a,b", [
        [1, 0],
        ["a", 2],
    ])
    def test_div(self, a, b):
        with pytest.raises(Exception):
            assert self.calc.div(a,b)

    #正常值
    @pytest.mark.parametrize("a,b,c", [
        [1, 2, 2],
        [0, 10, 0],
        [-1,2,-2],
        [0.5,0.5,0.25],
        [999999,9999999,9999989000001]
    ])
    def test_mul(self, a, b, c):
        assert self.calc.mul(a, b) == c

    #异常值
    @pytest.mark.parametrize("a,b", [
        ["1","2"],
        ["a",1]
    ])
    def test_mul(self, a, b):
        with pytest.raises(Exception):
            assert self.calc.mul(a, b)