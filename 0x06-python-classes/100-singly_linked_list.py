#!/usr/bin/python3
"""It define classes for singly-linked list."""


class Node:
    def __init__(self, data, next_node=None):
        """
        Initialize new Node.

        Args:
            data (int): data of new Node.
            next_node (Node): ext node of new Node.
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        
        self.__data = data
        self.__next_node = next_node


class SinglyLinkedList:
    def __init__(self):
        """
        Initialize new SinglyLinkedList.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert new Node into correct sorted position in the list (increasing order).

        Args:
            value (int): Value to insert as a new Node.
        """
        new_node = Node(value)
        if self.__head is None or self.__head._Node__data > value:
            new_node._Node__next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current._Node__next_node is not None and current._Node__next_node._Node__data < value:
                current = current._Node__next_node
            new_node._Node__next_node = current._Node__next_node
            current._Node__next_node = new_node

    def __str__(self):
        """
        Define string representation of a SinglyLinkedList.

        Returns:
            str: String containing one node number per line.
        """
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current._Node__data))
            current = current._Node__next_node
        return '\n'.join(values)
