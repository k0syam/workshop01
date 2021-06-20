from unittest import TestCase, main
from algo_sample import plus


class TestAlgo(TestCase):

    def test_plus(self):
        """
        テスト用の入力・出力を配置し，事前にACかどうかを確認する
        配列の組として与えることで複数のテストを実行できる
        """
        value1_list = [2, 4, 5]
        value2_list = [6, 3, 2]
        expected = [8, 7, 7]
        for a, b, c in zip(value1_list, value2_list, expected):
            with self.subTest(a=a, b=b):
                self.assertEqual(plus(a=a, b=b), c)


if __name__ == "__main__":
    main()