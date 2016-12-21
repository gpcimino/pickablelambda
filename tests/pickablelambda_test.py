import unittest
import pickle
import types
from functools import partial 

from pickablelambda import pickable

def dummy_func(x):
    return x+1

def dummy_func2(x, y):
    return x+y    

class TestLambdaProxy(unittest.TestCase):

    def test_pickle_lambda_raises_ex(self):
        lmb = lambda x: x+1
        with self.assertRaises(Exception):
            pickle_bin = pickle.dumps(lmb)

    def test_pickle_with_lamdba_proxy(self):
        lmb = lambda x: x+1
        pickle_bin = pickle.dumps(pickable(lmb))
        lmb2 = pickle.loads(pickle_bin)
        self.assertEqual(lmb(10), lmb2(10))
        self.assertTrue(isinstance(lmb2, types.FunctionType))

    def test_use_lambda_proxy(self):
        lmb = lambda x: x+1
        proxy = pickable(lmb)
        self.assertEqual(lmb(100), proxy(100))

    def test_use_lambda_proxy_2_args(self):
        lmb = lambda x, y: x+y
        proxy = pickable(lmb)
        self.assertEqual(lmb(100, 200), proxy(100, 200))

    def test_use_lambda_second_order_equation(self):
        lmb = lambda x: 5*x**2 + 3*x + 4
        proxy = pickable(lmb)
        self.assertEqual(lmb(2), proxy(2))

    def test_make_func_pickable_not_raise_err(self):
        proxy = pickable(dummy_func)
        self.assertEqual(3, proxy(2))

    def dummy_method(self, x):
        return x+1         

    def test_make_class_method_pickable_not_raise_err(self):
        proxy = pickable(self.dummy_method)
        self.assertEqual(3, proxy(2)) 

    def test_make_partial_func_pickable_not_raise_err(self):
        partial_func = partial(dummy_func, x=2)
        proxy = pickable(partial_func)
        self.assertEqual(3, proxy())

    def test_make_partial_func_2args_pickable_not_raise_err(self):
        partial_func = partial(dummy_func2, y=2)
        proxy = pickable(partial_func)
        self.assertEqual(3, proxy(1))        
        

if __name__ == "__main__":
    unittest.main()