import java.util.Iterator;
import java.util.Set;

public class BSTMap<K extends Comparable<K>, V> implements Map61B<K, V> {
    private class BSTNode {
        public BSTNode(K k, V v) {
            key = k;
            value = v;
            left = null;
            right = null;
        }
        K key;
        V value;
        BSTNode left;
        BSTNode right;
    }

    public BSTMap() {
        root = null;
    }
    private BSTNode root;
    private int size;

    @Override
    public void put(K key, V value) {
        root = insert(root, key, value);
    }

    private BSTNode insert(BSTNode cur, K key, V value) {
        if (cur == null) {
            size += 1;
            return new BSTNode(key, value);
        } else if (cur.key.compareTo(key) < 0) {
            cur.right = insert(cur.right, key, value);
        } else if (cur.key.compareTo(key) > 0) {
            cur.left = insert(cur.left, key, value);
        } else {
            cur.value = value;
        }
        return cur;
    }

    @Override
    public V get(K key) {
        return find(root, key);
    }

    private V find(BSTNode cur, K key) {
        if (cur == null) {
            return null;
        } else if (cur.key.compareTo(key) < 0) {
            return find(cur.right, key);
        } else if (cur.key.compareTo(key) > 0) {
            return find(cur.left, key);
        } else {
            return cur.value;
        }
    }

    private boolean containsKeyHelper(BSTNode cur, K key) {
        if (cur == null) {
            return false;
        } else if (cur.key.compareTo(key) < 0) {
            return containsKeyHelper(cur.right, key);
        } else if (cur.key.compareTo(key) > 0) {
            return containsKeyHelper(cur.left, key);
        } else {
            return true;
        }
    }

    @Override
    public boolean containsKey(K key) {
        return containsKeyHelper(root, key);
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public void clear() {
        root = null;
        size = 0;
    }

    @Override
    public Set<K> keySet() {
        return null;
    }

    @Override
    public V remove(K key) {
        return null;
    }

    @Override
    public Iterator<K> iterator() {
        return null;
    }

    public void printInOrder() {
        inorderTraversal(root);
    }
    private void inorderTraversal(BSTNode cur) {
        if (cur == null) {
            return;
        }
        inorderTraversal(cur.left);
        System.out.println(cur.key);
        inorderTraversal(cur.right);

    }
}
