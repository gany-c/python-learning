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
    def __init__(self, e_type, value=None, dependencies=None, compute_function=None):
        self.e_type = e_type
        self.is_fresh = True

        if e_type == 'base':
            self.value = value
            self.dependencies = []
            self.compute_function = None
        else:
            self.value = None
            self.dependencies = dependencies or []
            self.compute_function = compute_function

        self.downstream = []

    def __repr__(self):
        return f"StateEntry(type={self.e_type},value={self.value}"


class ComputeCache:

    def __init__(self):
        self.cache_state = {}

    def _mark_stale(self, key):
        entry = self.cache_state[key]

        for child_key in entry.downstream:
            child_entry = self.cache_state[child_key]
            if child_entry.is_fresh:
                child_entry.is_fresh = False
                self._mark_stale(child_key)

    def put(self, key: str, value: int):

        if key not in self.cache_state:
            self.cache_state[key] = StateEntry('base', value)
            return

        entry = self.cache_state[key]
        entry.value = value
        entry.is_fresh = True  # This particular update value is fresh

        self._mark_stale(key)  # But the downstreams have to be recomputed.

    def _recompute(self, key):
        # internal recompute
        entry = self.cache_state[key]

        if entry.e_type == 'base':
            return entry.value

        # refresh the downstream, and collect the arg values. You only have the keys
        args = []
        for dep_key in entry.dependencies:
            dep_entry = self.cache_state[dep_key]

            if not dep_entry.is_fresh:
                self._recompute(dep_key)

            args.append(dep_entry.value)

        entry.value = entry.compute_function(args)
        entry.is_fresh = True

        return entry.value

    def compute(self, key: str, dep_list, func):

        # if you are replacing an existing compute, remove it from all upstreams first
        if key in self.cache_state:
            old_entry = self.cache_state[key]
            for upstream in old_entry.dependies:
                self.cache_state[upstream].downstream.remove[key]

                self._mark_stale(key)

        # Ensure that supplied dependency keys are valid
        for dep in dep_list:
            if dep not in self.cache_state:
                raise KeyError(f"Dependency {dep} not found")

        # Create compute entry
        entry = StateEntry(
            e_type='compute',
            value=None,
            dependencies=dep_list,
            compute_function=func
        )

        # insert the key and value
        self.cache_state[key] = entry

        # mark the new key as downstream in all dependencies
        for dep in dep_list:
            self.cache_state[dep].downstream.append(key)

        # compute the initial derived value
        self._recompute(key)

    def get(self, key: str):

        entry = self.cache_state[key]
        if entry.e_type == 'base':
            return entry.value

        if not entry.is_fresh:
            return self._recompute(key)
        else:
            return entry.value


if __name__ == '__main__':
    cache = ComputeCache()
    cache.put("amount", 100)
    print(cache.get('amount'))

    cache.compute("doubled", ["amount"], lambda args: args[0] * 2)
    print(cache.get('doubled'))

    cache.compute("quadrupled", ["doubled"], lambda args: args[0] * 2)
    print(cache.get('quadrupled'))

    cache.put("amount", 5)
    print(cache.get('quadrupled'))
