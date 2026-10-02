def power_set(s):
    n = len(s)
    result = []

    # Iterate through all subsets (represented by 0 to 2^n - 1)
    for i in range(1 << n):   
        subset = ""
        for j in range(n):
            # Check if the j-th bit is set in i
            if i & (1 << j):
                subset += s[j]
                
            # Add the subset to the result
        result.append(subset)   

    return result

T = {1, 2}
# Probability space
omega = {(HH), (HT), (TH), (TT)}
F = power_set(omega)
P = {1/4, 1/4, 1/4, 1/4}

# Measure space
E = (0, 1, 2)
G = power_set(E)

# Random variable after one coin flip
X_1 = {HH: 1, HT: 1, TH: 0, TT: 0}
# Random variable after two coin flips
X_2 = {HH: 2, HT: 1, TH: 1, TT: 0}