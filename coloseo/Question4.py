spam = [{
    "name": "张三",
    "serial": "0001"
}, {
    "name": "李四",
    "serial": "0002"
}, {
    "name": "王五",
    "serial": "0003"
}, {
    "name": "王五2",
    "serial": "0003"
}, {
    "name": "赵四",
    "serial": "0004"
}, {
    "name": "小明",
    "serial": "005"
}, {
    "name": "小张",
    "serial": "006"
}, {
    "name": "小李",
    "serial": "006"
}, {
    "name": "小李2",
    "serial": "006"
}, {
    "name": "赵四2",
    "serial": "0004"
}]


class Solution:

    def solu(self):
        """
        对下面的 json 字符串 serial 相同的进行去重。
        这里默认对json字符进行转义后得到 spam 列表
        :return:
        """
        result = []  # 存放最后结果
        row = {}  # 键值映射去重
        for item in spam:
            # print(item, end='\n')
            if row.get(item['serial']) is None:
                row[item['serial']] = 0
                result.append(item)

        print(result)


if __name__ == '__main__':
    solution = Solution()
    solution.solu()
