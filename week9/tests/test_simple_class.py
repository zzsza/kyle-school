from simple_class import Queue

def test_firstlast():
    q = Queue()

    q.add_item(5)
    q.add_item(17)
    q.add_item("hello")

    assert q.first() == 5
    assert q.last() == "hello"

def test_len():
    q = Queue()

    assert q.length() == 0

    q.add_item(1)

    assert q.length() == 1

    for i in range(10):
        q.add_item(i)

    assert q.length() == 10

