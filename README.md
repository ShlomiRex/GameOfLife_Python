# Game of Life - Written in Python

Game of Life:

https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

![](README/demo.gif)
 
# How to use

| Key                | Description |
| ------------------ | ----------- |
| W or Up arrow      | Move up     |
| S or Down arrow    | Move down   |
| A or Left arrow    | Move left   |
| D or Right arrow   | Move right  |
| Plus (equals)      | Zoom in     |
| Minus (underscore) | Zoom out    |

# Greedy Implimentation

Instead of using giant zero and ones board, like so:
```
[
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    [0, 1, 0, 0, 0, 0, 0, 1, 1, 1]
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 0]
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0]
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
```
I use tuple (pair) to describe alive cell, like so:
```
[(1, 0), (1, 1), (1, 2), (3, 2), (4, 2), (3, 3), (4, 3), (7, 1), (8, 1), (9, 1)]
```

# Greedy Performance

Because the board is mostly empty anyways, and we don't need to deal with 'expanding' the board to fit negative, out of bounds indexes.

This allows much smaller memory footprint, though at the cost of CPU time. 

(Finding neighbours of (x,y) is `O(N)` - one pass, instead of constant time `O(9)`)

Altough we pay in finding neighbours, because of the `Complementary surplus principle`, we actually use less CPU time, because we don't pass all of the cells, the exact neighbours of the alive cells. We gain advantage by NOT iterating through the matrix. 

Furthermore, because we want to expand the board anyway, this is a good solution. In addition, most of the cells are dead.
