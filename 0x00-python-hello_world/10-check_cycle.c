#include "lists.h"

/**
 * check_cycle-a function that checks if a singly linked list has a cycle in it
 * @list: the linked list to be checked
 *
 * Return: 1 when has cycle else 0
 */

int check_cycle(listint_t *list)
{
	listint_t *slow_ptr = root;
	listint_t *fast_ptr = root;

	while (slow_ptr != NULL && fast_ptr != NULL && fast_ptr->next != NULL)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;

		if (slow_ptr == fast_ptr)
		{
			return (1);
		}
		return (0);
	}
}
