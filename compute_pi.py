"""Compute pi."""
from decimal import Decimal, getcontext
import argparse
import itertools


class ComputePi:
    """Compute pi to a specific precision using multiple algorithms."""

    @staticmethod
    def BBP(precision):
        """Compute pi using the Bailey-Borwein-Plouffe formula."""
        getcontext().prec = precision + 20

        pi = Decimal(0)
        for k in itertools.count():
            term = (Decimal(4)/(8*k+1) - Decimal(2)/(8*k+4) - Decimal(1)/(8*k+5) - Decimal(1)/(8*k+6))
            term /= Decimal(16)**k
            pi += term

            if term < Decimal(10)**(-precision-10):
                break

        pi = str(pi)[:-19]
        return pi


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculates pi.')
    parser.add_argument('--precision', type=int, default=100,
                        help='The desired precision of pi (default: 100 digits)')

    args = parser.parse_args()
    pi_computer = ComputePi()
    print(pi_computer.BBP(args.precision))
