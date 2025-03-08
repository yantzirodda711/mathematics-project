import math
def calculate_pi(n):
    """
    Compute the value of pi using the Bailey-Borwein-Plouffe algorithm.
    """
    def bits(x):
        """Return the binary representation of x as a list of 1s and 0s."""
        return [int(bit) for bit in bin(x)[2:]]
    def pi_bits(n):
        """Generate the first n bits of the binary representation of pi."""
        i = 1
        while True:
            yield i if math.cos(i * math.pi / (1 << 30)) >= 0 else -i
            i += 1
    def estimate_pi(n):
        """Estimate the value of pi based on the first n bits."""
        return sum(b * (1 if b % 2 == 0 else -2) for b in pi_bits(n)) / (1 << (n - 1))
    return estimate_pi(n)