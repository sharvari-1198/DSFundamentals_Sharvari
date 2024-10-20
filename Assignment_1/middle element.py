# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:50:33 2024

@author: Sharvari
"""
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# Function to add a new node


def pushNode(head_ref, data_val):
    # Allocate node
    new_node = Node(data_val)
    # Link the old list of the new node
    new_node.next = head_ref[0]
    # Move the head to point to the new node
    head_ref[0] = new_node

# Function to find the middle of the linked list


def getMiddle(head):
    mid = head
    counter = 1
    # Traverse over the entire linked list
    while head:
        # If counter is even, move the mid pointer to the next node
        if counter % 2 == 0:
            mid = mid.next
        head = head.next
        # Increment the counter for each node
        counter += 1
    return mid.data



# Driver Code
head = [None]
for i in range(8, 0, -1):
    pushNode(head, i)
print("Middle Value Of Linked List is:", getMiddle(head[0]))