
Data structure mainly have 2 types

1. linear  
	- **Array**
	- **Linked List**
	- **Stack**
	- **Queue**
	- **Deque**
Array      → [10, 20, 30, 40]

Linked List → 10 → 20 → 30 → 40

Stack       → 40
              30
              20
              10

Queue       → 10 → 20 → 30 → 40
              ↑           ↑
            front        rear
            
1. Non-linear 
	- **Tree**
	- **Graph**
	- **Heap**
	- **Trie**

# Linked List

### 1. What is it?

A **Linked List** is a collection of objects called **nodes**, where each node

Types of Linked Lists

1. **Singly Linked List**: Each node points to the next node in the sequence.
2. **Doubly Linked List**: Each node has two references, one to the next node and one to the previous node.
3. **Circular Linked List**: The last node points back to the first node, forming a circle.
4. **Circular Doubly Linked List**: A combination of circular and doubly linked lists.
5. **Header Linked List**: Includes a special header node at the beginning.

### 2. Why do we need it?
Suppose you have:

```
10 → 20 → 30 → 40
```

If you want to insert `25` between `20` and `30`:

```
10 → 20 → 25 → 30 → 40
```

You mainly change the connections:

```
20.next = 25
25.next = 30
```

You don't need to shift `30` and `40`.

That's the main strength of a linked list:

> **Easy insertion/deletion when you already know where the change should happen.**


Node A
┌──────┬──────┐
│  10  │  ──────────┐
└──────┴──────┘     ↓
                 Node B
                ┌──────┬──────┐
                │  20  │  ──────────┐
                └──────┴──────┘     ↓
                                  Node C
                                 ┌──────┬──────┐
                                 │  30  │ NULL │
                                 └──────┴──────┘


## Linked List — Operations


1. Node
2. create linked_list
3. length of linked list
4. **Traversal** — visit all nodes
5. **Insertion**
    - At beginning (node head )
    - At end (node tail )
    - At position (mid)
6. **Deletion**
    - From beginning (head )
    - From end (tail)
    - From position (mid)
7. **Search** — find a value
8. **Update** — change node value
9. **Reverse** — reverse the list


### Types of Linked Lists:
There are three basic forms of linked lists:
- Singly linked lists
- Doubly linked lists
- Circular linked lists

