import sys
sys.setrecursionlimit(10**5)

def solution(words, queries):
    words = set(words)
    
    forwardTrie = {}
    reverseTrie = {}
    
    def insertWord(trie, word):
        if len(word) == 0:
            return
        if not trie.get(word[0]):
            trie[word[0]] = { 'total': 1 }
        trie[word[0]]['total'] += 1
        insertWord(trie[word[0]], word[1:])
    
    for word in words:
        if not forwardTrie.get(len(word)):
            forwardTrie[len(word)] = { 'total': 1 }
        if not reverseTrie.get(len(word)):
            reverseTrie[len(word)] = { 'total': 1 }
        forwardTrie[len(word)]['total'] += 1
        reverseTrie[len(word)]['total'] += 1
        insertWord(forwardTrie[len(word)], word)
        insertWord(reverseTrie[len(word)], word[::-1])
    
    def getCount(trie, word):
        count = 0
        if len(word) == 0:
            return 1
        if word[0] == '?':
            count += trie['total']
        elif not trie.get(word[0]):
            return 0
        else:
            count = getCount(trie[word[0]], word[1:])
        return count
    
    answer = []
    for query in queries:
        if query[-1] == '?':
            if not forwardTrie.get(len(query)):
                answer.append(0)
            else:
                answer.append(getCount(forwardTrie[len(query)], query))
        else:
            if not reverseTrie.get(len(query)):
                answer.append(0)
            else:
                answer.append(getCount(reverseTrie[len(query)], query[::-1]))
        
    return answer

print(solution(	["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
print(solution(	["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "?????", "fr???", "fro???", "pro?"]))