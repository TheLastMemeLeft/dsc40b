"""Learning a threshold classifier. DSC 40B - Super Homework."""


def learn_theta(data, colors):
    """All blue points are < all red points. Return theta with
    blue <= theta < red. Theta(n) time (optimal: must look at every point)."""
    return max(x for x, c in zip(data, colors) if c == 'blue')


def compute_ell(data, colors, theta):
    """Loss at theta: (# red points <= theta) + (# blue points > theta).
    Theta(n) time (optimal)."""
    loss = 0
    for x, c in zip(data, colors):
        if c == 'red' and x <= theta:
            loss += 1
        elif c == 'blue' and x > theta:
            loss += 1
    return float(loss)


def minimize_ell(data, colors):
    """Return a theta minimizing L. Quadratic time.

    L only changes at data points, so some data point is a minimizer
    (the smallest point is blue, so we never need theta left of all data).
    """
    best_theta = None
    best_loss = float('inf')
    for theta in data:                       # n candidates
        loss = compute_ell(data, colors, theta)  # O(n) each
        if loss < best_loss:
            best_loss = loss
            best_theta = theta
    return float(best_theta)


def minimize_ell_sorted(data, colors):
    """data is sorted; n/2 red, n/2 blue. Return a minimizer of L in linear time.

    Loop invariant: after the alpha-th iteration, blue_gt_theta is the
    number of blue points which are greater than data[alpha - 1].
    """
    n = len(data)
    red_le_theta = 0
    blue_gt_theta = n // 2
    best_theta = None
    best_loss = float('inf')

    for alpha in range(1, n + 1):
        if colors[alpha - 1] == 'red':
            red_le_theta += 1
        else:
            blue_gt_theta -= 1
        # invariant holds: blue_gt_theta == # blue points > data[alpha - 1]
        loss = red_le_theta + blue_gt_theta
        if loss < best_loss:
            best_loss = loss
            best_theta = data[alpha - 1]

    return float(best_theta)
