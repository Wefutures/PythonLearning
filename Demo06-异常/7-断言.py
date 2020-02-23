# -*- coding: utf-8 -*-


# 断言
def _test_ssert(x):
    assert isinstance(x, int), '类型错误，请输入整形'
    assert x < 1, '数值错误，请输入一个小于1的数'


_test_ssert(1)
