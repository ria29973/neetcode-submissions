class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        mapping = defaultdict(list)
        for word in wordList:
            for i, c in enumerate(word):
                pattern = word[:i] + "*" + word[i+1:]
                mapping[pattern].append(word)
        q = deque()
        q.append(beginWord)
        visited = set()
        visited.add(beginWord)
        count = 0
        while q:
            count+=1
            length = len(q)
            for i in range(length):
                word = q.popleft()
                if word == endWord:
                    return count
                for i, c in enumerate(word):
                    pattern =  word[:i] + "*" + word[i+1:]
                    for words in mapping[pattern]:
                        if words not in visited:
                            q.append(words)
                            visited.add(words)
            
        return 0



        


        
        