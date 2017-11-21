# -*- coding: utf-8 -*-

import unittest
from tests_1_random_ import TestRandomFunctions
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    # 控制测试样例执行顺序

    suite = unittest.TestSuite()

    # 有序执行
    tests = [TestRandomFunctions("test_shuffle"), TestRandomFunctions("test_sample")]

    # 批量添加或者只添加一个case
    suite.addTests(tests)
    suite.addTest(TestRandomFunctions("test_choice"))

    # create runner for suite, print detail test info
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    # other loader
    # suite.addTests(unittest.TestLoader().loadTestsFromName('tests_1_random_.TestRandomFunctions'))
    # suite.addTests(unittest.TestLoader().loadTestsFromNames(['tests_1_random_.TestRandomFunctions']))

    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestRandomFunctions))

    # with open('test_report.txt', 'a') as f:
    with open('test_report.html', 'w') as f:
        # runner = unittest.TextTestRunner(stream=f, verbosity=2)
        # runner.run(suite)
        html_runner = HTMLTestRunner(
            stream=f,
            title="html reporter",
            description="use HTMLTestRunner to test",
            verbosity=2
        )
        html_runner.run(suite)
