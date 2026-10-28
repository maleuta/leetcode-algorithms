
import unittest


class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.minStack[-1]




class TestMinStack(unittest.TestCase):

    def setUp(self):
        self.ms = MinStack()

    def test_push_single_and_getmin(self):
        self.ms.push(5)
        self.assertEqual(self.ms.getMin(), 5)
        self.assertEqual(self.ms.top(), 5)

    def test_push_increasing_min_stays(self):
        self.ms.push(1)
        self.ms.push(2)
        self.ms.push(3)
        self.assertEqual(self.ms.getMin(), 1)
        self.assertEqual(self.ms.top(), 3)

    def test_push_decreasing_min_updates(self):
        self.ms.push(3)
        self.ms.push(2)
        self.ms.push(1)
        self.assertEqual(self.ms.getMin(), 1)

    # --- pop restores previous min ---
    def test_pop_restores_previous_min(self):
        self.ms.push(5)
        self.ms.push(1)
        self.ms.push(3)
        self.assertEqual(self.ms.getMin(), 1)
        self.ms.pop()                       
        self.assertEqual(self.ms.getMin(), 1)
        self.ms.pop()                       
        self.assertEqual(self.ms.getMin(), 5)   

    def test_pop_to_single(self):
        self.ms.push(2)
        self.ms.push(1)
        self.ms.pop()
        self.assertEqual(self.ms.getMin(), 2)
        self.assertEqual(self.ms.top(), 2)




if __name__ == "__main__":
    unittest.main()