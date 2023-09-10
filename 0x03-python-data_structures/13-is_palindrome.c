#include "lists.h"

/**
* reverse_listint - Reverses singly-linked listint_t list.
* @head: Pointer to the starting node of the list to reverse.
*
* Return: Pointer to the head of the reversed list.
*/
listint_t *reverse_listint(listint_t **head)
{
listint_t *node = *head, *next, *prev = NULL;

while (node)
{
next = node->next;
node->next = prev;
prev = node;
node = next;
}

*head = prev;
return (*head);
}

/**
* is_palindrome - It checks if singly linked list is palindrome.
* @head: Pointer to the head of the linked list.
*
* Return: If linked list is not a palindrome - 0.
*         If linked list is a palindrome - 1.
*/
int is_palindrome(listint_t **head)
{
if (*head == NULL || (*head)->next == NULL)
return (1);

listint_t *slow = *head, *fast = *head;

while (fast && fast->next)
{
slow = slow->next;
fast = fast->next->next;
}

listint_t *second_half = reverse_listint(&slow);

listint_t *first_half = *head;
while (second_half)
{
if (first_half->n != second_half->n)
{
reverse_listint(&slow);
return (0);
}
first_half = first_half->next;
second_half = second_half->next;
}

reverse_listint(&slow);

return (1);
}
