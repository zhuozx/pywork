import allure
import pytest

from test_pytest.core.calc import Calc


class TestCalc:
    def setup_class(self):
        self.calc = Calc()

    # 正常除法用例
    @allure.feature("除法用例")
    @allure.story("正常除法用例")
    @pytest.mark.parametrize("a,b,c", [
        [0, 1, 0],
        [2, 2, 1],
        [1, 2, 0.5],
        [1.8, 0.3, 6],
        [1000, 0.1, 10000],
        [1, 3, 0.3333333333333333],
        [1, 100000000, 0.00000001],
        [0.000000001, 0.000000002, 0.5]
    ])
    def test_div_normal(self, a, b, c):
        assert self.calc.div(a, b) == c

    # 精度丢失除法用例
    @allure.feature("除法用例")
    @allure.story("精度丢失除法用例")
    @pytest.mark.parametrize("a,b,c", [
        [5.6, 0.8, 7],
        [1.2, 3, 0.4],
    ])
    def test_div_lost(self, a, b, c):
        assert self.calc.div(a, b) == c

    # 异常除法用例
    @allure.feature("除法用例")
    @allure.story("异常除法用例")
    @pytest.mark.parametrize("a,b", [
        [1, 0],
        ["a", 2],
        [2, "a"],
        [2, " "],
        ["中文", "中文"]
    ])
    def test_div_ex(self, a, b):
        with pytest.raises(Exception):
            assert self.calc.div(a, b)

    # 正常乘法用例
    @allure.feature("乘法用例")
    @allure.story("正常乘法用例")
    @pytest.mark.parametrize("a,b,c", [
        [1, 2, 2],
        [0, 10, 0],
        [-1, 2, -2],
        [0.26, 0.25, 0.065],
        [9, 0.7, 6.3],
        [-10, -0.1, 1],
        [0.1, 2, 0.2]
    ])
    def test_mul_normal(self, a, b, c):
        assert self.calc.mul(a, b) == c

    # 精度丢失乘法用例
    @allure.feature("乘法用例")
    @allure.story("精度丢失乘法用例")
    @pytest.mark.parametrize("a,b,c", [
        [7, 0.8, 5.6],
        [6, 0.3, 1.8],
        [3, -0.4, -1.2],
    ])
    def test_mul_lost(self, a, b, c):
        assert self.calc.mul(a, b) == c

    # 异常乘法用例
    @allure.feature("乘法用例")
    @allure.story("异常乘法用例")
    @pytest.mark.parametrize("a,b", [
        ["a", "a"],
        ["中文", "中文"],
        [" ", " "]
    ])
    def test_mul_ex(self, a, b):
        with pytest.raises(Exception):
            assert self.calc.mul(a, b)
