from __future__ import annotations

from typing import TypeVar

T = TypeVar('T')


class Nodo[T]:
    def __init__(self, value: T):
        self.data = value
        self.next: None | Nodo[T] = None
        
        
    def __repr__(self):
        return f"Node({self.data},{self.next})"        
        

