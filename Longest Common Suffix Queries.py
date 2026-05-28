class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        # Trie node: children dict + best index stored at this node
        # best = index of wordsContainer string with shortest len (tie: earliest index)

        trie = {}  # nested dicts; each node also has '__best__' key

        def is_better(new_idx, cur_idx):
            """Return True if new_idx is a better candidate than cur_idx."""
            if cur_idx == -1:
                return True
            new_len = len(wordsContainer[new_idx])
            cur_len = len(wordsContainer[cur_idx])
            return new_len < cur_len or (new_len == cur_len and new_idx < cur_idx)

        # Insert reversed words into trie, updating best at every node
        for i, word in enumerate(wordsContainer):
            node = trie
            # Update root best
            if is_better(i, node.get('__best__', -1)):
                node['__best__'] = i

            for ch in reversed(word):
                if ch not in node:
                    node[ch] = {'__best__': -1}
                node = node[ch]
                if is_better(i, node['__best__']):
                    node['__best__'] = i

        # Answer each query
        ans = []
        for query in wordsQuery:
            node = trie
            for ch in reversed(query):
                if ch not in node:
                    break
                node = node[ch]
            ans.append(node['__best__'])

        return ans