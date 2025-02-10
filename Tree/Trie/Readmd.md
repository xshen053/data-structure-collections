# 一文说明白 Trie

Trie 像树一样，但是又有区别。区别在于，我们用一个 hashtable，key value pair 的结构来表示 tree

# Why we need Trie

- efficient prefix searching

比如我们想找到所有的 words，start with "pre", a trie allows you to do this in O(m)

如果用了 trie，time 就是 O(m + k)

不用 trie 的话，time 是 O(m \* n)

# Complexity

n : Number of keys (words) in the trie.

m : length of the longest word

Insertion: O(m)

- Inserting a word of length m takes O(m) , as each character requires a single operation to add to the trie.

Search: O(m)

- Searching for a word of length m also takes O(m) , as we follow each character down the trie.

Deletion: O(m)

- Deleting a word takes O(m) , assuming we need to remove each character in the word if it’s no longer shared with other words.

Space: O(m \* n)
