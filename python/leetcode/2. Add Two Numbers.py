# -*- coding: utf-8 -*-
"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        _node = self
        res = ''
        while 1:
            res += str(_node.val)
            if _node.next:
                res += '->'
                _node = _node.next
            else:
                break
        return res


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # if l1 is not None and l2 is not None:
        #     _val = None
        #     val_1 = l1.val
        #     val_2 = l2.val
        #     flag = 0
        #
        #     _val = val_1 + val_2
        #
        #     if flag:
        #         _val += 1
        #         flag = 0
        #     if _val > 9:
        #         _val %= 10
        #         flag = 1
        #
        #     _node = ListNode(_val)
        #
        #     val_1 = l1.next.val if l1.next else None
        #     val_2 = l2.next.val if l2.next else None
        #
        # elif l1 is None and l2 is not None:
        #     return l2
        # elif l1 is not None and l2 is None:
        #     return l2
        # else:
        #     return None
        #


        def nodeListToList(node_list):
            tmp_list = []
            while 1:
                tmp_list.append(node_list.val)
                if node_list.next is None:
                    break
                else:
                    node_list = node_list.next
            return tmp_list

        def completeList(list_a, list_b):
            if len(list_a) == len(list_b):
                pass
            elif len(list_a) < len(list_b):
                list_a.extend([0] * (len(list_b) - len(list_a)))
            else:
                list_b.extend([0] * (len(list_a) - len(list_b)))

        def addTwoList(list1, list2):
            res_list = []
            flag = 0
            for i in range(len(list1)):
                sum_xy = list1[i] + list2[i]
                if flag:
                    sum_xy += 1
                    flag = 0
                if sum_xy > 9:
                    sum_xy %= 10
                    flag = 1
                res_list.append(sum_xy)
            if flag:
                res_list.append(1)
            return res_list

        def listToNodeList(l):
            node_list = [ListNode(val) for val in l]
            for i in range(0, len(node_list) - 1):
                node_list[i].next = node_list[i + 1]
            return node_list[0]

        list1 = nodeListToList(l1)
        list2 = nodeListToList(l2)
        completeList(list1, list2)
        res_list = addTwoList(list1, list2)
        return listToNodeList(res_list)


if __name__ == '__main__':
    a = ListNode(2)
    a.next = a1 = ListNode(4)
    a1.next = a2 = ListNode(5)
    b = ListNode(8)
    b.next = ListNode(6)
    b.next.next = ListNode(4)
    # b.next.next.next = ListNode(9)
    print Solution().addTwoNumbers(a, b)

    print a
    print b
