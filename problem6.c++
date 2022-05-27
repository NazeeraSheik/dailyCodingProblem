// This problem was asked by Google.

// An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

// If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
#include <stdio.h> 
#include <stdlib.h> 
#include <inttypes.h> 
  
// Node structure of a memory  
// efficient doubly linked list 
struct Node 
{ 
    int data; 
    struct Node* npx; /* XOR of next and previous node */
}; 
  
/* returns XORed value of the node addresses */
struct Node* XOR (struct Node *a, struct Node *b) 
{ 
    return (struct Node*) ((uintptr_t) (a) ^ (uintptr_t) (b)); 
} 

void insert(struct Node **head_ref, int data) 
{ 
    // Allocate memory for new node 
    struct Node *new_node = (struct Node *) malloc (sizeof (struct Node) ); 
    new_node->data = data; 
  
    new_node->npx = XOR(*head_ref, NULL); 
  
   
    if (*head_ref != NULL) 
    { 
     
        struct Node* next = XOR((*head_ref)->npx, NULL); 
        (*head_ref)->npx = XOR(new_node, next); 
    } 
  
    // Change head 
    *head_ref = new_node; 
} 
  
// prints contents of doubly linked 
// list in forward direction 
void printList (struct Node *head) 
{ 
    struct Node *curr = head; 
    struct Node *prev = NULL; 
    struct Node *next; 
  
    printf ("Following are the nodes of Linked List: \n"); 
  
    while (curr != NULL) 
    { 
        // print current node 
        printf ("%d ", curr->data); 
  
        next = XOR (prev, curr->npx); 
  
        // update prev and curr for next iteration 
        prev = curr; 
        curr = next; 
    } 
} 
  
// Driver program to test above functions 
int main () 
{ 
    /* Create following Doubly Linked List 
    head-->40<-->30<-->20<-->10 */
    struct Node *head = NULL; 
    insert(&head, 10); 
    insert(&head, 20); 
    insert(&head, 30); 
    insert(&head, 40); 
  
    // print the created list 
    printList (head); 
  
    return (0); 
}