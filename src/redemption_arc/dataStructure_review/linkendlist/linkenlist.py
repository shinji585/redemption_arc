from collections.abc import Generator
from typing import Any, TypeVar

from redemption_arc.dataStructure_review.linkendlist.node import Nodo

T = TypeVar("T")


class SinglyLinkedlist[T]:
    def __init__(self) -> None:
        self._head: None | Nodo[T] = None
        self._tail: None | Nodo[T] = None
        self._size: int = 0

    def append(self, value: T) -> None:
        new_node: Nodo[T] = Nodo(value=value)

        if self._tail is not None:
            self._tail.next = new_node
            self._tail = new_node
        else:
            self._head = new_node
            self._tail = new_node
        self._size += 1

    def preappend(self, value: T) -> None:
        new_node: Nodo[T] = Nodo(value=value)

        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head = new_node
        self._size += 1

    @property
    def __len__(self) -> int:
        return self._size

    def prepop(self) -> T:
        if self._head is None:
            raise IndexError("Pop from empty list")

        value: T = self._head.data
        if self._head is self._tail:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next
        self._size -= 1
        return value

    def pop(self) -> T:
        if self._tail is None:
            raise IndexError("Pop from empty list")

        value: T = self._tail.data
        if self._head is self._tail:
            self._head = None
            self._tail = None
        else:
            assert self._head is not None
            prev: Nodo[T] = self._head
            current: Nodo[T] = self._head
            while current.next is not None:
                prev = current
                current = current.next
            self._tail = prev
            self._tail.next = None
        self._size -= 1
        return value

    def get(self, index: int) -> None | Nodo[T]:
        if index < 0 or index >= self._size:
            return None

        current: None | Nodo[T] = self._head
        for _ in range(index):
            assert current is not None
            current = current.next
        return current 
    
    def update(self, index: int, value: T) -> bool: 
        current: None | Nodo[T] = self.get(index=index)
        if current: 
            current.data = value
            return True
        return False
    
    def insert(self, index: int, value: T) -> None: 
        if index < 0 or index > self._size: 
            return 
        
        if index == 0: 
            self.preappend(value=value)
        elif index == self._size: 
            self.append(value=value)
        else:     
            current = self.get(index=index - 1)
            assert current is not None 
            new_nodo = Nodo(value=value)
            new_nodo.next = current.next
            current.next = new_nodo
            self._size += 1 
            
            
    def remove(self, index: int)  -> None | T: 
        if index < 0 or index > self._size: 
            return None 
        
        if index == 0: 
            return self.prepop()
        elif index == self._size: 
            return self.pop()
        else: 
            prev: None | Nodo[T] = self.get(index=index - 1)
            assert prev is not None 
            current: None | Nodo[T] = prev.next
            assert current is not None 
            prev.next = current.next
            current.next = None 
            self._size -= 1
            return current.data
            
    
        
    def __iter__(self) -> Generator[T, Any]:
        current: None | Nodo[T] = self._head

        while current is not None:
            yield current.data
            current = current.next


if __name__ == "__main__":
    xls: SinglyLinkedlist[str] = SinglyLinkedlist()
    
    for x in ["a", "b", "c"]:
        xls.append(x)
        
    print(f"List: {[x for x in xls]}")
    xls.insert(0, "X")
    xls.insert(2, "Y")
    print(f"List: {[x for x in xls]}")