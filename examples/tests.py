import dataci


add_testcases = [
    {
        'a': 1,
        'b': 2,
        'expect': 3,
    },
    {
        'a': 0,
        'b': 2,
        'expect': 2,
    },
]


def add_func(a, b):
    return a + b


@dataci.use_data(add_testcases)
def test_add(a, b, expect):
    assert add_func(a, b) == expect



def multiply_func(a, b):
    return a * b


@dataci.use_json_data('multiply.json')
def test_multiply_func(a, b, expect):
    assert multiply_func(a, b) == expect
