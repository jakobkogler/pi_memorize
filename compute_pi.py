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

    @staticmethod
    def arctan_euler(x, one=1000000):
        """Calculate arctan(1/x) using euler's accelerated formula.

        Based on http://www.craig-wood.com/nick/articles/pi-machin/"""
        x_squared = x * x
        x_squared_plus_1 = x_squared + 1
        term = (x * one) // x_squared_plus_1
        total = term
        two_n = 2
        while 1:
            divisor = (two_n+1) * x_squared_plus_1
            term *= two_n
            term += divisor // 2    # round the division
            term = term // divisor
            if term == 0:
                break
            total += term
            two_n += 2
        return total

    @staticmethod
    def machin_euler(one):
        """Compute pi using Machin's formula.

        Based on http://www.craig-wood.com/nick/articles/pi-machin/"""
        one *= 10**20
        pi = 4*(4*ComputePi.arctan_euler(5, one) - ComputePi.arctan_euler(239, one))
        pi //= 10**20
        return '3.{}'.format(str(pi)[1:])



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculates pi.')
    parser.add_argument('--precision', type=int, default=100,
                        help='The desired precision of pi (default: 100 digits)')

    args = parser.parse_args()
    pi_computer = ComputePi()

    print(pi_computer.machin_euler(10**args.precision))
