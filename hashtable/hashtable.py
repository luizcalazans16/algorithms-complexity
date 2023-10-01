class HashSet:
    def __init__(self):
        self.table_size = 16
        self.hash_table = [None] * self.table_size

    def _hash(self, element):
        return hash(element) % self.table_size

    def add(self, element):
        index = self._hash(element)
        if self.hash_table[index] is None:
            self.hash_table[index] = []
        if element not in self.hash_table[index]:
            self.hash_table[index].append(element)

    def remove(self, element):
        index = self._hash(element)
        if self.hash_table[index] is not None and element in self.hash_table[index]:
            self.hash_table[index].remove(element)

    def contains(self, element):
        index = self._hash(element)
        return self.hash_table[index] is not None and element in self.hash_table[index]

    def union(self, other_set):
        result_set = HashSet()
        for item_list in self.hash_table:
            if item_list is not None:
                for element in item_list:
                    result_set.add(element)
        for item_list in other_set.hash_table:
            if item_list is not None:
                for element in item_list:
                    result_set.add(element)
        return result_set

    def intersection(self, other_set):
        result_set = HashSet()
        for item_list in self.hash_table:
            if item_list is not None:
                for element in item_list:
                    if other_set.contains(element):
                        result_set.add(element)
        return result_set

    def difference(self, other_set):
        result_set = HashSet()
        for item_list in self.hash_table:
            if item_list is not None:
                for element in item_list:
                    if not other_set.contains(element):
                        result_set.add(element)
        return result_set

    def items(self):
        item_set = set()
        for item_list in self.hash_table:
            if item_list is not None:
                item_set.update(item_list)
        return item_set


def main():
    set1 = HashSet()
    set2 = HashSet()

    set1.add(1)
    set1.add(2)
    set1.add(3)

    set2.add(2)
    set2.add(3)
    set2.add(4)

    print("Set 1:", set1.items())
    print("Set 2:", set2.items())

    print("\nTesting union:")
    union_set = set1.union(set2)
    print("Union of Set 1 and Set 2:", union_set.items())

    print("\nTesting intersection:")
    intersection_set = set1.intersection(set2)
    print("Intersection of Set 1 and Set 2:", intersection_set.items())

    print("\nTesting difference:")
    difference_set = set1.difference(set2)
    print("Difference between Set 1 and Set 2:", difference_set.items())

    set1.remove(1)
    print("\nAfter removing 1 from Set 1:", set1.items())

    print("\nChecking if 4 is in Set 2:", set2.contains(4))
    print("Checking if 1 is in Set 2:", set2.contains(1))

if __name__ == "__main__":
    main()
