# 位运算

主要的操作符号就那么几个

- AND(&)
- OR(|)
- XOR(^)
  - 主要是用来 toggle a bit，1 变 0，0 变 1
- NOT(~)
- Shift Left(<<)
  - 左移，补 0
- Shift Right(>>)
  - 这个根据原来的数是 sign 和 unsigned 会有差异

# 常见 pattern

## even or odd

```C
if (x & 1) {
    // even path
} else {
    // odd path
}
// 根据奇偶走不同的path
```

## set 1，翻转 bit，清除 bit 为 0

```C
// sets the n-th bit of x to 1, regardless of its current state.
x |= (1 << n);

// This operation clears (sets to 0) the n-th bit of x, regardless of its current state.
x &= ~(1 << n);

// Toggle a bit
x ^= (1 << n);
```

## 数 1

```C
// calculate how many 1 in x
int count = 0;
while (x) {
    count += x & 1;
    x >>= 1;
}
```

## 交换 2 个数

```C
// swap 2 numbers
x = x ^ y;
y = x ^ y;
x = x ^ y;

/**
 * dry run:
 * x = 1, y = 0
 * x = 1 ^ 0
 * y = (1 ^ 0) ^ 0 = 1
 * x = 1 ^ 0 ^ 1 = 0
 * x = 0, y = 1
 * /
```

## 检查是否 x 为 power of 2

```C
if (x > 0 && (x & (x - 1)) == 0) {
    // x is a power of two
    // 因为 x & (x - 1)会去除最低位的1，而power of 2只有1个1
}
```

## not equal

```C
/*
 * isNotEqual - return 0 if x == y, and 1 otherwise
 *   Examples: isNotEqual(5L, 5L) = 0L, isNotEqual(4L, 5L) = 1L
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 6
 *   Rating: 2
 */
long isNotEqual(long x, long y) {
    return !(!(x ^ y));
}
```
