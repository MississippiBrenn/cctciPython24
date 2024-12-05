#remove dups from an unsorted linked list 
# create a list 
# add nodes to list 
# check list 
# remove if found 
from singly_linked_list import SinglyLinkedList


def remove_dups(linked_list):
    dup_checker = []
    while linked_list.head.next: 
        dup_checker.append(head.data)
        
