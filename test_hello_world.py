import unittest  # 2.导入unittest模块
import hello_world  # 2.导入被测试模块


# 3.创建一个继承unittest.TestCase的类
class Tests(unittest.TestCase):
    # 4.创建test_为前缀的方法，里面用self.assert方法调用被测试的对象
    def test_mod_three(self):
        self.assertEqual(hello_world.get_info('Snow'), 'hello, Project! -- Snow')

    # 4.创建test_为前缀的方法，里面用self.assert方法调用被测试的对象
    def test_isupper(self):
        self.assertFalse("HELlO".isupper())
        self.assertTrue("HELLO".isupper())


# 5.unittest.main()作为主函数入口
if __name__ == '__main__':
    unittest.main()
