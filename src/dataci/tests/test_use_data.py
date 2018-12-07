from dataci import use_data


data_simple_2_kwargs = (
    {
        'input_obj': 'hello',
        'expect': 'world',
    },
    {
        'input_obj': 'hello',
        'expect': 666,
    },
)


def test_basic_func():
    got = []
 
    @use_data(data_simple_2_kwargs)
    def merge(input_obj, expect):
        got.append('%s--%s' % (input_obj, expect))
    
    merge()

    expect = [
        '%s--%s' % (i['input_obj'], i['expect']) for i in data_simple_2_kwargs
    ]

    assert got == expect
