#include "lists.h"

/**
 * palin - function to know if it's palindrome
 * @head: the head of the list
 * @end: end of the list
 * Return: always 1 since it's recursive
 */

int palin(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (palin(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (1);
}

/**
 * is_palindrome - function to check if it's recursive function
 * or not
 * @head: the head of the list
 * Return: - if it's not palindrome, 1 if it is
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (palin(head, *head));
}
