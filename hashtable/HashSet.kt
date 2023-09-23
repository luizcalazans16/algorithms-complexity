class HashSet<T> {
    private val hashMap = mutableMapOf<T, Boolean>()

    fun add(element: T) {
        hashMap[element] = true
    }

    fun remove(element: T) {
        hashMap.remove(element)
    }

    fun contains(element: T): Boolean {
        return hashMap.containsKey(element)
    }

    fun union(otherSet: HashSet<T>): HashSet<T> {
        val resultSet = HashSet<T>()
        resultSet.hashMap.putAll(this.hashMap)
        resultSet.hashMap.putAll(otherSet.hashMap)
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

    fun items() =
        hashMap.keys.toSet()
}
