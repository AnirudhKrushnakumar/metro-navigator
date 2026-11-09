
"""Unit tests for Queue and board_passengers()."""

import random
import time
import unittest

from linked_list import LinkedList
from linked_queue import Queue, board_passengers


class TestQueue(unittest.TestCase):

    def test_QU_01(self):
        queue = Queue()
        self.assertEqual(len(queue), 0)
        self.assertTrue(queue.is_empty())
        self.assertEqual(queue.to_list(), [])

        with self.assertRaises(IndexError):
            queue.dequeue()

        with self.assertRaises(IndexError):
            queue.peek()

    def test_QU_02(self):
        queue = Queue()
        for x in [1, 2, 3]:
            queue.enqueue(x)

        self.assertEqual(queue.peek(), 1)
        self.assertEqual(len(queue), 3)
        self.assertEqual(queue.to_list(), [1, 2, 3])

    def test_QU_03(self):
        queue = Queue()
        for x in [1, 2, 3]:
            queue.enqueue(x)

        self.assertEqual(
            [queue.dequeue(), queue.dequeue(), queue.dequeue()],
            [1, 2, 3]
        )

        self.assertTrue(queue.is_empty())

        with self.assertRaises(IndexError):
            queue.dequeue()

    def test_QU_04(self):
        queue = Queue()
        for x in [1, 2, 3]:
            queue.enqueue(x)

        for _ in range(3):
            self.assertEqual(queue.peek(), 1)

        self.assertEqual(len(queue), 3)

    def test_QU_05(self):
        queue = Queue()
        queue.enqueue("a")
        queue.enqueue("b")

        self.assertEqual(queue.dequeue(), "a")

        queue.enqueue("c")

        self.assertEqual(queue.dequeue(), "b")
        self.assertEqual(queue.dequeue(), "c")
        self.assertTrue(queue.is_empty())

    def test_QU_06(self):
        queue = Queue()

        for cycle in range(5):
            queue.enqueue(cycle)
            self.assertEqual(queue.dequeue(), cycle)

            queue.enqueue(cycle + 10)
            queue.enqueue(cycle + 20)

            self.assertEqual(
                queue.to_list(),
                [cycle + 10, cycle + 20]
            )

            self.assertEqual(queue.peek(), cycle + 10)
            self.assertEqual(queue.dequeue(), cycle + 10)
            self.assertEqual(queue.dequeue(), cycle + 20)
            self.assertTrue(queue.is_empty())

    def test_QU_07(self):
        queue = Queue()
        values = [None, 0, [], ("x",)]

        for value in values:
            queue.enqueue(value)

        self.assertEqual(
            [queue.dequeue() for _ in values],
            values
        )

    def test_QU_08(self):
        queue = Queue()

        self.assertIsInstance(queue._list, LinkedList)

        start = time.perf_counter()

        for i in range(20_000):
            queue.enqueue(i)

        for i in range(20_000):
            self.assertEqual(queue.dequeue(), i)

        elapsed = time.perf_counter() - start

        self.assertLess(elapsed, 1.0)

    def test_QU_09(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.clear()

        self.assertTrue(queue.is_empty())

        queue.enqueue(3)

        other = Queue()
        other.enqueue(9)

        self.assertEqual(queue.to_list(), [3])
        self.assertEqual(other.to_list(), [9])

    def test_QU_10(self):
        names = ["A", "B", "C", "D", "E"]

        self.assertEqual(
            board_passengers(names, 3),
            (["A", "B", "C"], ["D", "E"])
        )

    def test_QU_11(self):
        self.assertEqual(
            board_passengers(["A", "B", "C", "D", "E"], 1),
            (["A"], ["B", "C", "D", "E"])
        )

        self.assertEqual(
            board_passengers(["A", "B", "C"], 10),
            (["A", "B", "C"], [])
        )

        self.assertEqual(
            board_passengers(["Z"], 1),
            (["Z"], [])
        )

    def test_QU_12(self):
        self.assertEqual(
            board_passengers(["A", "B", "C"], 0),
            ([], ["A", "B", "C"])
        )

    def test_QU_13(self):
        self.assertEqual(
            board_passengers([], 3),
            ([], [])
        )

    def test_QU_14(self):
        with self.assertRaises(ValueError):
            board_passengers(["A", "B"], -1)

        with self.assertRaises(TypeError):
            board_passengers(["A", "B"], 2.5)

        with self.assertRaises(TypeError):
            board_passengers(["A", "B"], "2")

    def test_QU_15(self):
        names = ["Ada", "Grace", "Katherine"]
        original = names[:]

        board_passengers(names, 2)

        self.assertEqual(names, original)

    def test_QU_16(self):
        names = ["Ana", "Ben", "Cy"]
        boarded, waiting = board_passengers(names, 1)

        self.assertEqual(boarded, ["Ana"])
        self.assertEqual(waiting, ["Ben", "Cy"])

    def test_QU_17(self):
        rng = random.Random(1201)
        queue = Queue()
        model = []

        for _ in range(1_000):
            if not model or rng.random() < 0.6:
                value = rng.randint(-100, 100)
                queue.enqueue(value)
                model.append(value)
            else:
                self.assertEqual(queue.dequeue(), model.pop(0))

            self.assertEqual(queue.to_list(), model)
            self.assertEqual(len(queue), len(model))


if __name__ == "__main__":
    unittest.main()
