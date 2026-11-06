from collections import defaultdict


def is_anagram(first_word: str, second_word: str) -> bool:
    return sorted(first_word.strip()) == sorted(second_word.strip())


def groups_anagrams(words: list) -> list:
    anagrams = defaultdict(list)
    for word in words: 
        key = tuple(sorted(word))
        anagrams[key].append(word)
        
    return list(anagrams.values())

print(is_anagram('listen', 'silent'))
print(f"Angrams: {groups_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])}")