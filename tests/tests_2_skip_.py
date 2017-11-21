# -*- coding: utf-8 -*-
import sys
import unittest

import django

print django.__version__, sys.platform


class SkipTestCase(unittest.TestCase):
    # 无条件跳过
    @unittest.skip("always skip")
    def test_nothing(self):
        self.fail("should't happen")

    # 条件为真跳过
    @unittest.skipIf(django.__version__ > '1.8', 'skip test for django > 1.8')
    def test_skip_if(self):
        print sys._getframe().f_code.co_name

    # 条件为假时跳过
    # Skip a test unless the condition is true.
    @unittest.skipUnless(sys.platform.startswith('win'), 'skip windows test')
    def test_skip_unless(self):
        print 'only test for linux'
        print sys._getframe().f_code.co_name

    # Mark the test as an expected failure. If the test fails when run, the test is not counted as a failure.
    @unittest.expectedFailure
    def test_expect_fail(self):
        """"可预见的失败，测试结果不会在不通过中"""
        print sys._getframe().f_code.co_name
        self.assertEqual(1, 0, 'broken')

    def test_fail(self):
        print sys._getframe().f_code.co_name
        self.fail("fail directly")

if __name__ == '__main__':
    unittest.main()

# $ python tests_2_skip_.py
# 1.8.11 win32
# test_expect_fail
# xtest_fail
# Fssonly test for linux
# test_skip_unless
# .
# ======================================================================
# FAIL: test_fail (__main__.SkipTestCase)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "tests_2_skip_.py", line 36, in test_fail
#     self.fail("fail directly")
# AssertionError: fail directly
#
# ----------------------------------------------------------------------
# Ran 5 tests in 0.001s
#
# FAILED (failures=1, skipped=2, expected failures=1)

# unittest是Python自带的单元测试框架，我们可以用其来作为我们自动化测试框架的用例组织执行框架。

# unittest的流程：写好TestCase，然后由TestLoader加载TestCase到TestSuite，然后由TextTestRunner来运行TestSuite，
# 运行的结果保存在TextTestResult中，我们通过命令行或者unittest.main()执行时，main会调用TextTestRunner中的run来执行，
# 或者我们可以直接通过TextTestRunner来执行用例。

# 一个class继承unittest.TestCase即是一个TestCase，其中以 test 开头的方法在load时被加载为一个真正的TestCase。

# verbosity参数可以控制执行结果的输出，0 是简单报告、1 是一般报告、2 是详细报告。

# 可以通过addTest和addTests向suite中添加case或suite，可以用TestLoader的loadTestsFrom__()方法。

# 用 setUp()、tearDown()、setUpClass()以及 tearDownClass()可以在用例执行前布置环境，以及在用例执行后清理环境

# 我们可以通过skip，skipIf，skipUnless装饰器跳过某个case，或者用TestCase.skipTest方法。

# 参数中加stream，可以将报告输出到文件：可以用TextTestRunner输出txt报告，以及可以用HTMLTestRunner输出html报告。

