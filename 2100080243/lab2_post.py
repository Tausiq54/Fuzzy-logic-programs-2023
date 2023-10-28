class FuzzySet:
    def __init__(self, elements):
        self.elements = dict(elements)

    def union(self, other):
        union_elements = dict(self.elements)
        for key, value in other.elements.items():
            if key in union_elements:
                union_elements[key] = max(union_elements[key], value)
            else:
                union_elements[key] = value
        return FuzzySet(union_elements.items())

    def intersection(self, other):
        intersection_elements = {}
        for key, value in self.elements.items():
            if key in other.elements:
                intersection_elements[key] = min(value, other.elements[key])
        return FuzzySet(intersection_elements.items())

    def __str__(self):
        return str(self.elements)


# Create the fuzzy sets
a = FuzzySet({('x1', 0.5), ('x2', 0.7), ('x3', 0.0)})
b = FuzzySet({('x1', 0.8), ('x2', 0.2), ('x3', 1.0)})

# Perform set operations
union_result = a.union(b)
intersection_result = a.intersection(b)

# Print the results
print("Union:", union_result)
print("Intersection:", intersection_result)
