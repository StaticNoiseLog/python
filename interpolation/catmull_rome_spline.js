let spline = (t, a, b, c, d) => {
    return 0.5 * (
        (2 * b) +
        (-a + c) * t +
        (2 * a - 5 * b + 4 * c - d) * t * t +
        (-a + 3 * b - 3 * c + d) * t * t * t
    );
}

