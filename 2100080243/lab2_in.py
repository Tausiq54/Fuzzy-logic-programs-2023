import numpy as np
def max_min_composition(P, Q):
    n = len(P)
    m = len(Q[0])
    R = np.zeros((n, m))
    for i in range(n):
        for k in range(m):
            R[i, k] = np.max(np.minimum(P[i, :], Q[:, k]))
    return R
  def max_dot_composition(P, Q):
    n = len(P)
    m = len(Q[0])
    R = np.zeros((n, m))
    for i in range(n):
        for k in range(m):
            R[i, k] = np.max(P[i, :] * Q[:, k])
    return R
    P = np.array([[0.6, 0.6, 0.8, 0.9],
              [0.1, 0.2, 0.9, 0.8],
              [0.9, 0.3, 0.4, 0.8],
              [0.9, 0.8, 0.1, 0.2]])

Q = np.array([[0.1, 0.2, 0.7, 0.9],
              [1.1, 0.4, 0.6, 0.0],
              [0.0, 0.5, 0.9, 0.0],
              [0.9, 1.0, 0.8, 0.2]])
# Max-min composition
R_max_dot = max_dot_composition(P, Q)
print("Max-dot Composition (R_max_dot):")
print(R_max_dot)
R_max_dot = max_dot_composition(P, Q)
print("Max-dot Composition (R_max_dot):")
print(R_max_dot)
