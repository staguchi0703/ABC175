#
from resolve import resolve
####################################
####################################
# 以下にプラグインの内容をペーストする
#  
import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        print('------------')
        print(out)
        print('------------')
        self.assertEqual(out, output)

#     def test_入力例_1(self):
#         input = """5 2
# 2 4 5 1 3
# 3 4 -10 -8 8"""
#         output = """8"""
#         self.assertIO(input, output)

#     def test_入力例_2(self):
#         input = """2 3
# 2 1
# 10 -7"""
#         output = """13"""
#         self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 3
3 1 2
-1000 -2000 -3000"""
        output = """-1000"""
        self.assertIO(input, output)

#     def test_入力例_4(self):
#         input = """10 58
# 9 1 6 7 8 4 3 2 10 5
# 695279662 988782657 -119067776 382975538 -151885171 -177220596 -169777795 37619092 389386780 980092719"""
#         output = """29507023469"""
#         self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
