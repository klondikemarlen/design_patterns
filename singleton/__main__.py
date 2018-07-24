from singleton.generic import Singleton


class A(Singleton):
    pass


class B(Singleton):
    pass

class C(Singleton):
    pass


a, a2 = A.get_instance(), A.get_instance()
b, b2 = B.get_instance(), B.get_instance()
c, c2 = C(), C()

assert a is a2
assert b is b2
assert c is c2
assert a is not b is not c

print('a:  {}\na2: {}'.format(a, a2))
print('b:  {}\nb2: {}'.format(b, b2))
print('c:  {}\nc2: {}'.format(c, c2))
