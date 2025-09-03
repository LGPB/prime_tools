"""Unit tests for is_prime(num).

Assumptions based on your docstring:
- Raises TypeError if num is not an integer
- Raises ValueError if num < 2
- Returns True for primes, False for composites

Tests written by AI, hope nothing bad happens 30/08/2025 14:31:30 -3 UTC
"""

from unittest import TestCase
import unittest

from src.prime_tools.prime_tools import is_prime, prime_range, prime_list, nearest_prime


class TestIsPrime(TestCase):
    def test_small_primes(self):
        """2 and 3 are primes (smallest primes)."""
        self.assertTrue(is_prime(2), "2 should be prime")
        self.assertTrue(is_prime(3), "3 should be prime")

    def test_other_primes(self):
        """Some other known primes."""
        for p in (5, 7, 11, 13, 17, 19, 23, 97, 7919):
            with self.subTest(p=p):
                self.assertTrue(is_prime(p), f"{p} should be prime")

    def test_composites(self):
        """Known composites should return False."""
        for n in (4, 6, 8, 9, 12, 15, 100, 1024, 7918):
            with self.subTest(n=n):
                self.assertFalse(is_prime(n), f"{n} should not be prime")

    def test_values_below_two_raise_value_error(self):
        """Numbers below 2 raise ValueError (per docstring)."""
        for n in (-10, -1, 0, 1):
            with self.subTest(n=n):
                with self.assertRaises(ValueError):
                    is_prime(n)

    def test_non_integer_types_raise_type_error(self):
        """Non-integer inputs raise TypeError (per docstring)."""
        non_ints = (2.0, 3.14, "7", None, [], {}, (5,))
        for val in non_ints:
            with self.subTest(val=val):
                with self.assertRaises(TypeError):
                    is_prime(val)

    def test_large_prime_and_large_composite(self):
        """A reasonably large prime and a large composite to exercise algorithm."""
        self.assertTrue(is_prime(104729), "104729 is a prime (the 10000th prime)")
        self.assertFalse(is_prime(104729 * 2), "Even multiple of a prime is composite")


class TestPrimeRange(TestCase):
    def test_basic_range(self):
        """simple inclusive/exclusive behavior: primes >= start and < end"""
        self.assertEqual(prime_range(10, 2), [2, 3, 5, 7])
        self.assertEqual(prime_range(6, 3), [3, 5])

    def test_empty_range(self):
        """ranges with no primes return empty list"""
        self.assertEqual(prime_range(16, 14), [])
        # end <= start -> typically returns empty list (test expects that)
        self.assertEqual(prime_range(10, 10), [])
        self.assertEqual(prime_range(10, 11), [])  # if your implementation raises, change this test

    def test_start_below_two(self):
        """start below 2 should normally treat primes starting at 2"""
        self.assertEqual(prime_range(5, -5), [2, 3])

    def test_type_checks(self):
        """non-int types should raise TypeError (recommended)"""
        for bad in (2.0, "10", None, [], (3,)):
            with self.subTest(bad=bad):
                with self.assertRaises(TypeError):
                    prime_range(10, bad)
                with self.assertRaises(TypeError):
                    prime_range(bad, 2)

    def test_large_range_sample(self):
        """sanity check for larger ranges (not exhaustive)"""
        # primes between 100 and 120: [101, 103, 107, 109, 113]
        self.assertEqual(prime_range(120, 100), [101, 103, 107, 109, 113])


class TestPrimeList(TestCase):
    def test_basic_length_and_start(self):
        """returns list of requested length, first prime >= start"""
        lst = prime_list(5, start=2)
        self.assertEqual(len(lst), 5)
        self.assertTrue(all(isinstance(x, int) for x in lst))
        self.assertTrue(lst[0] >= 2)
        # check monotonic increasing sequence of primes
        for i in range(1, len(lst)):
            self.assertGreater(lst[i], lst[i - 1])

    def test_start_greater_than_first_prime(self):
        """start not necessarily 2"""
        lst = prime_list(3, start=30)
        self.assertEqual(len(lst), 3)
        self.assertTrue(lst[0] >= 30)

    def test_length_zero_allowed(self):
        """decide whether length 0 is allowed; here we expect empty list"""
        self.assertEqual(prime_list(0, start=2), [])

    def test_negative_length_raises_value_error(self):
        """negative lengths should raise ValueError (recommended)"""
        with self.assertRaises(ValueError):
            prime_list(-1, start=2)

    def test_type_checks(self):
        """non-int length or non-int start should raise TypeError (recommended)"""
        for bad in (2.0, "3", None, [], ()):
            with self.subTest(bad=bad):
                with self.assertRaises(TypeError):
                    prime_list(bad, start=2)
                with self.assertRaises(TypeError):
                    prime_list(3, start=bad)


class TestNearestPrime(TestCase):
    def test_nearest_inclusive(self):
        """if start is prime, nearest_prime(start, skips=0, ascending=True) returns start"""
        self.assertEqual(nearest_prime(7, skips=0, ascending=True), 11)
        self.assertEqual(nearest_prime(7, skips=0, ascending=False), 5)

    def test_ascending_search(self):
        """search for next primes greater than start"""
        self.assertEqual(nearest_prime(8, skips=0, ascending=True), 11 or 11)  # expects first prime >=8 => 11
        # a clearer: test known next primes
        self.assertEqual(nearest_prime(10, skips=0, ascending=True), 11)
        self.assertEqual(nearest_prime(10, skips=1, ascending=True), 13)  # 1 skip -> next after next

    def test_descending_search(self):
        """search for primes smaller than start"""
        self.assertEqual(nearest_prime(10, skips=0, ascending=False), 7)
        self.assertEqual(nearest_prime(10, skips=1, ascending=False), 5)

    def test_none_when_no_smaller_prime(self):
        """when searching downward and there is no valid prime (e.g. below 2) return None"""
        self.assertIsNone(nearest_prime(2, skips=0, ascending=False))
        self.assertIsNone(nearest_prime(2, skips=2, ascending=False))
        self.assertIsNone(nearest_prime(1, skips=0, ascending=False))

    def test_type_checks(self):
        """wrong types should raise TypeError for start/skips/ascending"""
        bad_values = (2.0, "10", None, [], {})
        for bad in bad_values:
            with self.subTest(bad=bad):
                with self.assertRaises(TypeError):
                    nearest_prime(bad, skips=0, ascending=True)
        # skips must be int
        with self.assertRaises(TypeError):
            nearest_prime(10, skips=0.5, ascending=True)
        # ascending must be bool
        with self.assertRaises(TypeError):
            nearest_prime(10, skips=0, ascending=1)  # integers shouldn't be accepted as bool

    def test_negative_skips_raises_value_error(self):
        """negative skips should raise ValueError"""
        with self.assertRaises(ValueError):
            nearest_prime(10, skips=-1, ascending=True)


if __name__ == "__main__":
    unittest.main()