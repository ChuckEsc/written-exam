spam = [
    {
        "id": "1",
        "name": "中国",
        "code": "110",
        "parent": ""
    },
    {
        "id": "2",
        "name": "北京市",
        "code": "110000",
        "parent": "110"
    },
    {
        "id": "3",
        "name": "河北省",
        "code": "130000",
        "parent": "110"
    },
    {
        "id": "4",
        "name": "四川省",
        "code": "510000",
        "parent": "110"
    },
    {
        "id": "5",
        "name": "石家庄市",
        "code": "130001",
        "parent": "130000"
    },
    {
        "id": "6",
        "name": "唐山市",
        "code": "130002",
        "parent": "130000"
    },
    {
        "id": "7",
        "name": "邢台市",
        "code": "130003",
        "parent": "130000"
    },
    {
        "id": "8",
        "name": "成都市",
        "code": "510001",
        "parent": "510000"
    },
    {
        "id": "9",
        "name": "简阳市",
        "code": "510002",
        "parent": "510000"
    },
    {
        "id": "10",
        "name": "武侯区",
        "code": "51000101",
        "parent": "510001"
    },
    {
        "id": "11",
        "name": "金牛区",
        "code": "51000102",
        "parent": "510001"
    }
]


class Solution:

    def recursion(self, data, parent_id):
        """
        把下面给出的扁平化json数据用递归的方式改写成组织树的形式
        此处默认 将json转换为 spam 列表
        :param data:
        :param parent_id:
        :return:
        """
        result = []
        for i in range(len(data) - 1):
            if data[i]['parent'] == parent_id:
                one = dict(
                    id=data[i]['id'],
                    name=data[i]['name'],
                    code=data[i]['code']
                )
                temp = self.recursion(data, data[i]['code'])
                if len(temp) > 0:
                    one.update({'children': temp})
                result.append(one)

        return result


if __name__ == '__main__':
    solution = Solution()
    answer = solution.recursion(spam, '')
    import pprint
    pprint.pprint(answer)
    print(answer)
