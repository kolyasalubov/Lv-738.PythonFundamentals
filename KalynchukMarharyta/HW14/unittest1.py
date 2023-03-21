import unittest

def sq_rect(a, b):
    return a*b 


 
class TestSq(unittest.TestCase):
    
    def test_sq(self):
        expected = 2
        actual = (sq_rect(1, 2))
        self.assertEqual(actual, expected)
        
    
if __name__ == '__main__':
    unittest.main()