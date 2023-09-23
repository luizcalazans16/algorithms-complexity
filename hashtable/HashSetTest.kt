fun testHashSet() {
    val set1 = HashSet<Int>()
    val set2 = HashSet<Int>()

    set1.add(1)
    set1.add(2)
    set1.add(3)

    set2.add(3)
    set2.add(4)
    set2.add(5)

    println("set1.contains(2): ${set1.contains(2)}")
    println("set1.contains(4): ${set1.contains(4)}")

    val unionSet = set1.union(set2)
    val intersectionSet = set1.intersection(set2)
    val differenceSet = set1.difference(set2)

    println("Union: ${unionSet.items()}")
    println("Intersection: ${intersectionSet.items()}")
    println("Difference: ${differenceSet.items()}")

    set1.remove(2)
    set2.remove(3)

    println("set1.contains(2): ${set1.contains(2)}")
    println("set2.contains(3): ${set2.contains(3)}")
}

fun main() {
    testHashSet()
}
