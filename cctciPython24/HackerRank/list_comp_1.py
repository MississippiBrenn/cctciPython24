

#You are given three integers ( x ), ( y ), and ( z ) representing the dimensions of a cuboid, along with an integer ( n ). Print a list of all possible coordinates given by ( (i, j, k) ) on a 3D grid where the sum of ( i + j + k ) is not equal to ( n )
def threeD_filter_pair(): 
    x = 1
    y = 2 
    z = 3
    n = 5
    pairs = [(x,y,z) for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]
    print(pairs)
    return pairs

# Problem Statement: Create a list of all (x, y) pairs where ( x ) ranges from 0 to 2 and ( y ) ranges from 0 to 2.
def generate_pairs():
    pairs = [(x,y) for x in range(3) for y in range(3)]
    return pairs

def test_pairs():
    expected_pairs = [
        (0, 0), (0, 1), (0, 2),
        (1, 0), (1, 1), (1, 2),
        (2, 0), (2, 1), (2, 2)
    ]
    actual_pairs = generate_pairs()
    
    if actual_pairs == expected_pairs:
        print("Test Passed.")
    else:
        print("Test Failed.")
        print(f"Expected: {expected_pairs}")
        print(f"Actual: {actual_pairs}")

# Modify the above list comprehension to create a list of all (x, y) pairs where ( x ) ranges from 0 to 2 and ( y ) ranges from 0 to 2, but only include pairs where ( x + y ) is not equal to 3.
def pair_filter(): 
    pairs = [(x,y) for x in range(3) for y in range(3) if x+y==3]
    return pairs

def test_pairs_filter():
    expected_pairs = [
        (1, 2), (2, 1)
    ]
    actual_pairs = pair_filter()
    
    if actual_pairs == expected_pairs:
        print("Test pair_filter Passed.")
    else:
        print("Test pair_filter Failed.")
        print(f"Expected: {expected_pairs}")
        print(f"Actual: {actual_pairs}")


if __name__ == "__main__":
    test_pairs()
    test_pairs_filter()
    threeD_filter_pair()