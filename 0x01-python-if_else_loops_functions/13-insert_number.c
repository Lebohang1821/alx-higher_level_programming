#include "lists.h"

/**
 * insert_node - It inserts a number into a sorted singly-linked list.
 * @head: Pointer the head of the linked list.
 * @number: Number to insert.
 *
 * Return: If function fails - NULL.
 * Otherwise - Pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *now;

	now = malloc(sizeof(listint_t));
	if (now == NULL)
		return (NULL);
	now->n = number;

	if (node == NULL || node->n >= number)
	{
		now->next = node;
		*head = now;
		return (now);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	now->next = node->next;
	node->next = now;

	return (now);
}
