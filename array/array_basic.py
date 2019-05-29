# -*-coding:utf-8-*-
"""
author：Li Xiang
date: 2019-05-29
configuration: VScode, Python 3.6.5
"""

class Array:
    """
    实现数组的一些基本操作：
    ● 实现一个支持动态扩容的数组
    ● 实现一个大小固定的有序数组，支持动态增删改操作
    """
    def __init__(self, capacity=10):
        """
        初始化数组
        capacity: 数组的最大容量，默认为10
        """
        self._capacity = capacity                # 数组最大容量
        self._size = 0                           # 数组已使用的容量
        self._data = [None] * self._capacity     # 初始化数组元素

    def _resize(self, new_capacity):
        """
        数组扩容
        """
        if new_capacity < self._capacity:
            self._data = self._data[:new_capacity]                   # 缩容
        else:
            self._data += [None] * (new_capacity - self._capacity)   # 扩容
        self._capacity = new_capacity

    def add(self, index, elem):
        """
        向数组中添加新的元素
        index: 添加元素所在的索引
        elem: 添加元素的数值
        """
        if(index < 0 or index > self._size):              # 索引无效
            print("Add failed, index不合法!")
            return False
        if self._size == self._capacity:                  # 数组的容量用完了
            self._resize(self._capacity * 2)
        for i in range(self._size - 1, index - 1, -1):    # index后面的元素后移一位
            self._data[i + 1] = self._data[i]
        self._data[index] = elem                          # 添加元素
        self._size += 1                                   # 更新size
        return True

    def delete(self, index):
        """
        删除数组的元素
        index: 删除元素的索引
        """
        if(index < 0 or index >= self._size):                   # 索引无效
            print("Delete failed, index不合法！")
            return False
        for i in range(index + 1, self._size):                  # index后面的元素前移一位
            self._data[i - 1] = self._data[i]
        self._data[self._size] = None                           # 更新变量
        self._size -= 1
        if(self._size and self._capacity // self._size == 4):   # 有效元素数量为容量的1/4，减小容量
            self._resize(self._capacity // 2)
        return True

    def set(self, index, elem):
        """
        修改数组的元素
        index: 修改元素的索引
        elem： 修改元素的数值
        """
        if(index < 0 or index >= self._size):       # 索引无效
            print("Set failed, index不合法")
            return False
        self._data[index] = elem                    # 修改元素
        return True

    def print(self):
        """
        打印数组
        """
        for i in range(self._size):
            print(self._data[i], end='  ')
        print("\n")


def test_array():
    """
    测试
    """
    array = Array(10)
    for i in range(10):
        array.add(i, i + 1)
    array.print()
    array.add(3, 100)
    array.print()
    array.add(15, 3)
    print(array.delete(3))
    print(array.delete(15))
    array.print()
    for i in range(5):
        array.delete(0)
    array.print()
    array.set(0, 666)
    array.print()



if __name__ == "__main__":
    test_array()
