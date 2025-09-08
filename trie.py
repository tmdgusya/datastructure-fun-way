from dataclasses import dataclass
from locale import currency
from typing import Dict, Optional


@dataclass
class TrieNode:
    def __init__(self, is_entry: bool = False) -> None:
        self.is_entry: bool = is_entry
        self.children: Dict[str, 'TrieNode'] = {}


@dataclass
class Trie:
    def __init__(self, root: Optional[TrieNode] = None) -> None:
        if not root:
            root = TrieNode(is_entry=False)
        self.root: TrieNode = root
    
    def insert(self, word: str) -> None:
        """Insert a word into the trie."""
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_entry = True
        
def trieSearch(trie: Optional[Trie], target: str):
  if not trie or not trie.root:
    return False
  
  current = trie.root
  
  for char in target:
    if char not in current.children:
      return False
    current = current.children[char]
  
  return current.is_entry