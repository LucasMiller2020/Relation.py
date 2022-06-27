#!/usr/bin/env python3

# ----------------------------------------------------------------------
# Relation.py
# Lucas Miller
# 2/23/22
# ----------------------------------------------------------------------

from __future__ import annotations
import collections.abc

class Relation:

    # ------------------------------------------------------------------

    # i need to go back over this lab 
    def __init__(self, *args, **kwargs):
        domainKey = "domain"
        if domainKey not in kwargs:
            raise ValueError("must provide domain keyword parameter")

        if not isinstance(kwargs[domainKey], collections.abc.Sequence):
            raise ValueError("domain parameter is not a Sequence")
        self.domain = set(kwargs[domainKey])
        self.items = set(args)

    def __iter__(self):
        """
        iterator that yields all the pairs in the Relation
        """
        # can just the set iterator to iterate over items in the set
        return iter(self.items)

    def __contains__(self, pair) -> bool:
        # in operator
        """
        :param pair: a tuple of (x, y)
        :return: True if (x, y) in the Relation, False otherwise
        """
        return pair in self.items

    def __str__(self) -> str:
        """
        string with each ordered pair as (x, y) separated by a comma and space between {}
        the ordered pairs must be sorted as they would if sorting the tuples
        example: {(1, 1), (1, 2), (2, 2), (2, 3)}
        :return: string representation of Relation as described above
        """

        # turn set into a list of tuples and sort
        sList = list(self.items)
        sList.sort()

        # build string list beginning with {
        strings = ["{"]
        for item in sList:
            # last item does not receive comma or space, all others do
            if item == sList[-1]:
                strings.append(f"{item}")
            else:
                strings.append(f"{item}, ")
        # end string list with }
        strings.append("}")
        return "".join(strings)

    # why are these two methods necessary ? can't I just use == and != since those work for sets already?
    def __eq__(self, other: Relation) -> bool:
        """
        :param other: the other Relation
        :return: True if the two Relations contain the same ordered pairs, and False otherwise
        """

        # true when all tuples in the set are the same between each set
        return self.items == other.items and self.domain == other.domain

    def __ne__(self, other: Relation) -> bool:
        """
        :param other: the other Relation
        :return: True if the two Relations do not contain the same ordered pairs, and False otherwise
        """

        # true when all tuples in each set are not the same
        return self.items != other.items or self.domain != other.domain

    # ------------------------------------------------------------------

    def insert(self, x, y) -> None:
        """
        add (x, y) to the Relation
        :param x: first element of ordered pair
        :param y: second element of ordered pair
        :return: None
        """
        # (x, y) pair to the set
        self.items.add((x, y))
        # add x and y to the domain if they aren't in there already
        if x not in self.domain:
            self.domain.add(x)
        if y not in self.domain:
            self.domain.add(y)

    def remove(self, x, y) -> None:
        """
        remove (x, y) from the Relation if it is in there
        :param x: first element of ordered pair
        :param y: second element of ordered pair
        :return: None
        """
        # remove tuple if it exists in the set already
        if (x, y) in self.items:
            self.items.remove((x, y))
            # remove x and y from the domain if they are in there
            if x in self.domain:
                self.domain.remove(x)
            if y in self.domain:
                self.domain.remove(y)

    def isReflexive(self) -> bool:
        """
        :return: True if the Relation is reflexive, False otherwise
        """
        for x in self.domain:
            # the pair (x, x) is not in the relation, it is not reflexive
            if (x, x) not in self.items:
                return False
        return True

    def isSymmetric(self) -> bool:
        """
        :return: True if the Relation is symmetric, False otherwise
        """
        # for every (x, y), (y, x) is in the relation.  if x = y, then symmetry is implied for that pair
        for item in self.items:
            # get x and y and check if (y, x) is in the relation
            x, y = item[0], item[1]
            if (y, x) not in self.items:
                return False
        return True

    def isAntiSymmetric(self) -> bool:
        """
        :return: True if the Relation is antisymmetric, False otherwise
        """
        # when x != y, there is no (y, x) for (x, y)
        for item in self.items:
            # get x and y
            x, y = item[0], item[1]
            # antisymmetric if (y, x) not in the relation and x != y
            if (y, x) not in self.items and x != y:
                return True
        return False

    def isTransitive(self) -> bool:
        """
        :return: True if the Relation is transitive, False otherwise
        """
        # for every (x, y), (y, z) and (x, z) must be in the relation

        """ i need to work on my consistency with python but i'm at a BMW dealership right now so that's sorta
        hard to do right now, i'll try to update my gf that i need to work on some stuff soon, but for now this will do 
        """

        # list of z elements
        zList = []
        for item in self.items:
            # obtain x and y
            x, y = item[0], item[1]
            for pair in self.items:
                # append z element when y
                if pair[0] == y:
                    zList.append(pair[1])
            # check if (x, z) is in the list
            for z in zList:
                if (x, z) not in self.items:
                    return False
            # reset zList to empty
            zList = []
        return True

    def relatedTo(self, x) -> set:
        """
        :param x: element to find related items to
        :return: set of all the elements related to x in the Relation
        """
        # empty
        related = set()
        for item in self.items:
            # add second item of the tuple when first item in the tuple is x
            if item[0] == x and len(self.items) > 1:
                related.add(item[1])
        return related

    # ------------------------------------------------------------------


# ----------------------------------------------------------------------

def main():
    r = Relation((1, 2), (2, 1), domain=(1, 2, 3))
    print(r)

# ----------------------------------------------------------------------


if __name__ == '__main__':
    main()
