class HashSet<T> {
    private val hashMap = mutableMapOf<T, Boolean>()

    fun add(element: T) {
        hashMap[element] = true
    }

    fun remove(element: T) {
        hashMap.remove(element)
    }

    fun contains(element: T): Boolean {
        return hashMap[element] != null
    }

    fun union(otherSet: HashSet<T>): HashSet<T> {
        val resultSet = HashSet<T>()
        for (key in this.hashMap.keys) {
            resultSet.add(key)
        }
        for (key in otherSet.hashMap.keys) {
            resultSet.add(key)
        }
        return resultSet
    }

    fun intersection(otherSet: HashSet<T>): HashSet<T> {
        val resultSet = HashSet<T>()
        for (element in this.hashMap.keys) {
            if (otherSet.contains(element)) {
                resultSet.add(element)
            }
        }
        return resultSet
    }

    fun difference(otherSet: HashSet<T>): HashSet<T> {
        val resultSet = HashSet<T>()
        for (element in this.hashMap.keys) {
            if (!otherSet.contains(element)) {
                resultSet.add(element)
            }
        }
        return resultSet
    }

    fun items(): Set<T> {
        val itemSet = mutableSetOf<T>()
        for (key in hashMap.keys) {
            itemSet.add(key)
        }
        return itemSet
    }
}
