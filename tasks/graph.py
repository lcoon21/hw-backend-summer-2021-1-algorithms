from typing import Any
from collections import deque

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:
        output = []
        stack = [self._root]
        while len(stack):
            temp = stack.pop()
            if temp not in output:
                output.append(temp)
                for t in temp.outbound[::-1]:
                    stack.append(t)
        return output


    def bfs(self) -> list[Node]:
        result = []
        q = deque()
        q.append(self._root)
        while len(q):
            temp = q.popleft()
            if temp not in result:
                result.append(temp)
                for t in temp.outbound:
                    q.append(t)

        return result
