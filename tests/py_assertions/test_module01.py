def test_a1():
    assert 4 < 5

def test_a2():
    assert 1

def test_a3():
    assert 'abcd' == 'abcd'

def test_a4():
    assert 1 in divmod(9,5)
    assert 'put' not in 'this pytest'
    assert [1,2] < [1,2,4]
