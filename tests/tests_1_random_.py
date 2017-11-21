# -*- coding: utf-8 -*-

import random
import unittest

import sys

step_no = 0


class TestRandomFunctions(unittest.TestCase):
    failureException = AssertionError
    longMessage = False
    print 'TestRandomFunctions: %s' % step_no

    def setUp(self):
        """设置测试夹具（测试准备工作）"""
        print sys._getframe().f_code.co_name
        self.seq = range(10)

    def tearDown(self):
        """销毁测试夹具（测试清理工作）"""
        print sys._getframe().f_code.co_name
        del self.seq

    @classmethod
    def setUpClass(cls):
        print sys._getframe().f_code.co_name

    @classmethod
    def tearDownClass(cls):
        print sys._getframe().f_code.co_name

    def test_shuffle(self):
        print sys._getframe().f_code.co_name
        random.shuffle(self.seq)
        print self.seq
        self.seq.sort()
        self.assertEqual(self.seq, range(10))

    def test_choice(self):
        print sys._getframe().f_code.co_name
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        print sys._getframe().f_code.co_name
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)

        with self.assertRaises(ValueError) as error:
            # 必须抛出ValueError
            # raise KeyError
            random.sample(self.seq, 20)

        # exception keeped in error
        self.assertIsInstance(error.exception, ValueError)
        # self.assertIs(error.exception, ValueError)

        # self.assertListEqual(self.seq, random.sample(self.seq, 5))
        for element in random.sample(self.seq, 5):
            self.assertIn(element, self.seq)
            # self.assertTrue(element in self.seq)


# 启动方式一：python xxx.py
if __name__ == '__main__':
    # unittest.main()
    unittest.main(verbosity=2)

# 启动方式二：python -m unittest xxx

# $ python -m unittest tests_1_random_
# $ python -m unittest -v tests_1_random_
# TestRandomFunctions: 0
# setUp
# test_choice
# tearDown
# .setUp
# test_sample
# tearDown
# .setUp
# test_shuffle
# [1, 4, 9, 3, 7, 6, 0, 5, 8, 2]
# tearDown
# .
# ----------------------------------------------------------------------
# Ran 3 tests in 0.004s
#
# OK

# 1. 在每个测试样例中都会调用一次测试夹具，准备测试条件和清理测试现场
# setUp -> test_xxx -> tearDown

# 2. 测试样例执行的顺序和函数定义的顺序无关
# 3. 成功/失败/错误/跳过 -> ./F/E/S

# 部分测试 模块/类/函数
# python -m unittest test_module1 test_module2
# python -m unittest test_module.TestClass
# python -m unittest test_module.TestClass.test_method
