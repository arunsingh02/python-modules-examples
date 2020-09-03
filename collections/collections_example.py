from collections import namedtuple, OrderedDict, defaultdict, deque, Counter


def named_tuple_test():
    """Named tuple"""
    point = namedtuple('point', 'x y')
    p = point(11, 12)  # point(x=11, y=12)
    print(p)
    p1 = point._make('12')  # [1,2], (1,2) itrable point(x='1', y='2')
    print(p1)
    p2 = point(11, y=12)
    print(p2)
    p3 = p2._asdict()  # orderdict - OrderedDict([('x', 11), ('y', 12)])
    print(p3)
    print(p2._replace(x=23))
    print(point._fields)  # ('x', 'y')
    print(p2.__hash__())


def ordered_dict():
    """Ordered Dict"""
    od = OrderedDict()
    od["name"] = 'Arun'
    od["age"] = 27
    od["add"] = "Bangalore"
    od["post"] = "Mahadevapura"

    print(od)
    od["name"] = "Ravi"
    print(od)  # OrderedDict([("name", "arun"), ("age", 27), ...])
    od.popitem()  # bydefault - last=True (act like LIFO)
    print(od)
    od.popitem(last=False)  # act like FIFO
    print(od)
    od.pop("add")  # required key name as input
    print(od)


def default_dict():
    """Default dict"""
    dd = defaultdict(list)  # default factory  -> None
    # dd["num"].append(10)
    dd["num"].append(20)
    dd["nums"].append(30)
    print(dd)

    dd1 = defaultdict(int)
    dd1["a"] += 1
    dd1["a"] += 1
    print(dd1)  # defaultdict(<class 'list'>, {'num': [10, 20], 'nums': [30]})

    # nested default dict
    dd2 = defaultdict(lambda: defaultdict(int))
    dd2['name']['count'] += 10
    print(
        dd2)  # defaultdict(<function default_dict.<locals>.<lambda> at 0x0000029C2AB29400>, {'name': defaultdict(<class 'int'>, {'count': 10})})
    dd3 = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    dd3["age"]["sex"]["count"] += 20
    print(
        dd3)  # defaultdict(<function default_dict.<locals>.<lambda> at 0x0000029C2AB29488>, {'age': defaultdict(<function default_dict.<locals>.<lambda>.<locals>.<lambda> at 0x0000029C2AB29510>, {'sex': defaultdict(<class 'int'>, {'count': 20})})})

    dd4 = defaultdict()
    dd4["name"] = "ravi"
    print(dd4)  # defaultdict(None, {'name': 'ravi'})

    # dd5 = defaultdict()
    # print(dd5["name"]) # key error


def deque_test():
    """
    Deque/Doubly linked list
    O(1) -> front and rear insert and delete performance
    O(n) -> for middle fetch or delete
    """
    d = deque([1, 2, 3, 4, 1])
    d.append(10)
    d.append(120)
    d.appendleft(10)
    d.extendleft([22, 33, 44])
    d.extend([55, 66])  # deque([44, 33, 22, 10, 1, 2, 3, 4, 1, 10, 120, 55, 66])
    print(d)
    d.rotate(2)
    print(d)  # deque([55, 66, 44, 33, 22, 10, 1, 2, 3, 4, 1, 10, 120])
    d.rotate(-3)
    print(d)  # deque([33, 22, 10, 1, 2, 3, 4, 1, 10, 120, 55, 66, 44])
    print(d.count(1))  # 2


# Counter
def counter_test():
    """Multiset"""
    c = Counter()
    ddict = {'a': 1, 'b': 2, 'c': 5}
    c.update(ddict)
    print(c)
    ddict1 = {'a': 2, 'b': 1}
    c.update(ddict1)
    print(c)
    print(list(c.elements()))
    print(c.most_common(2))

    c1 = Counter()
    c1.update(ddict1)
    print(c1)
    c1.subtract(c)
    print(c1)


if __name__ == "__main__":
    named_tuple_test()
    ordered_dict()
    default_dict()
    deque_test()
    counter_test()
