"""
Un America prayana niruvanathin, Thai niruvanam:
Question:

Implement a variation of a key value store, or cache

1. get is the same get(key)
2. put has two types - base put, which is the same as any dictionary put(key, value)
3. compute put - put(key, dependencies[dependent-key1, ....., dependent-keyN], function: [dependent-key1, ....., dependent-keyN] -> value)

dependent keys can be base keys or dependent keys themselves. If the a base key is changed, all the dependent functions should become stale and recalculated.

Example:

cache.put("amount", 100);
cache.compute("doubled", List.of("amount"), args -> (int)args[0] * 2);
cache.compute("quadrupled", List.of("doubled"), args -> (int)args[0] * 2);

cache.get("quadrupled"); // → 400

cache.put("amount", 10);
cache.get("quadrupled"); // → 40

SOLUTION:

How the solution will play out with my approach:

1. cache.put("base", 100);

You have one entry of type =>  key="base", base, value = 100, downstream = [], is_fresh = True

2. cache.compute("doubled", List.of("base"), args -> (int)args[0] * 2);

create new entry of type => compute, key="doubled", dependency =  ["base"], function = args -> (int)args[0] * 2);, downstream[], computed_value = 200
update the old entry => base, "base", value = 100, downstream = ["doubled"], is_fresh = True

3. cache.compute("quadrupled", List.of("doubled"), args -> (int)args[0] * 2);

type = compute, key="quadrupled", dependency =  ["quadrupled"], function = args -> (int)args[0] * 2);, downstream[], computed_value = 400, is_fresh = True
type = compute, key="doubled", dependency =  ["base"], function = args -> (int)args[0] * 2);, downstream["quadrupled"], computed_value = 200, is_fresh = True
base, "base", value = 100, downstream = ["doubled"], is_fresh = True

4. cache.put("base", 10);

type = compute, key="quadrupled", dependency =  ["quadrupled"], function = args -> (int)args[0] * 2);, downstream[], computed_value = 400, is_fresh = False
type = compute, key="doubled", dependency =  ["base"], function = args -> (int)args[0] * 2);, downstream["quadrupled"], computed_value = 200, is_fresh = False
base, "base", value = 10, downstream = ["doubled"], is_fresh = True

recursive operation to set all downstream to false

5. cache.get("Quadrupled")

if freshness is false, keep going up the dependency list until you see all true -
"""


class StateEntry:
    def __init__(self, e_type, key, value, dependencies=None, compute_function=None, downstream=None):
        self.key = key
        self.e_type = e_type
        self.value = value
        self.is_fresh = True  # Always True upon construction

        if self.e_type == 'base':
            # Base entries don't have up-stream dependencies or logic
            self.dependencies = []
            self.compute_function = None
            self.downstream = []
        else:
            # For all other types, use the provided arguments or defaults
            self.dependencies = dependencies if dependencies is not None else []
            self.compute_function = compute_function
            self.downstream = downstream if downstream is not None else []

    def __repr__(self):
        return f"StateEntry(type='{self.e_type}', value={self.value})"


class ComputeCache:

    """
    key - base or operation = type, null or [dependent names, function], value or derived value,
    downstream - through which you recursively go down and update,
    is-fresh
    """

    cache_state = {

    }

    def put(self, key: str, value: int):
        """

        if the key doesn't exist in the cache state, create a  base type entry  and add to the cache state
        if the key exists, 1 - we update the value; get the downstream entries and mark all of them as stale, do this recursively

        :param name:
        :param value:
        :return:
        """


    def compute(self, name: str, dep_list, func):
        """
         create an compute type entry, with provided name, computation function and upstream dependencies
         find all upstream dependencies and update their downstream lists, doesn't have to be recursive
         if the key already existed, mark all downtream as stale and do this recursively.
        :param name:
        :param dep_list:
        :param func:
        :return:
        """
        pass

    def get(self, name):
        pass
