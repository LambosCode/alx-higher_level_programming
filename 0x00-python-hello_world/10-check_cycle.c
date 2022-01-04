#include "lists.h"

/**
 * check_cycle - checking for a loop within nodes
 * @list: list of nodes
 *
 * Return: if loop occurs (1) else (0)
 */

int check_cycle(listint_t *list)
{
	listint_t *fst;
	listint_t *bck;

	if (!list || !list->next)
		return (0);
	fst = list;
	bck = list;

	fst = fst->next->next;
	bck = bck->next;

	while (fst && fst->next)
	{
		if (bck == fst)
			return (1);
		bck = bck->next;
		fst = fst->next->next;
	}

	if (bck != fst)
		return (0);
}
