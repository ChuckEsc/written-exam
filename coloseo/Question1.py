spam = 'abcd'


class Solution:

    def reverse(self, s: str):
        """
        递归版本的 reverse(s) 函数(或方法),以将字符串s倒置
        :param s:
        :return:
        """
        if len(s) == 1:
            # self.result.append(s[0])
            return s[0]
        else:
            item = self.reverse(s[1:])
            return item + s[0]

        # return self.result


if __name__ == '__main__':
    solution = Solution()
    answer = solution.reverse(spam)
    print(answer)
