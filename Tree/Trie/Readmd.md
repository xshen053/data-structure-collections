# Why we need Trie

- efficient prefix searching

比如我们想找到所有的 words，start with "pre", a trie allows you to do this in O(m)

如果用了 trie，time 就是 O(m + k)

不用 trie 的话，time 是 O(m \* n)
