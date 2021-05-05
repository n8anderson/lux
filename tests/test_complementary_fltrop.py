from lux.action import filter


def test_complemetary_fltrop():
    test_lessthan = []
    for op in filter.get_complementary_ops("<"):
        test_lessthan.append(op)
    assert test_lessthan[0] == ">="
    assert test_lessthan[1] == ">"

    test_greaterthan = []
    for op in filter.get_complementary_ops(">"):
        test_greaterthan.append(op)
    assert test_greaterthan[0] == "<="
    assert test_greaterthan[1] == "<"

    test_lessthan_equal = []
    for op in filter.get_complementary_ops("<="):
        test_lessthan_equal.append(op)
    assert test_lessthan_equal[0] == ">"
    assert test_lessthan_equal[1] == ">="

    test_greaterthan_equal = []
    for op in filter.get_complementary_ops(">="):
        test_greaterthan_equal.append(op)
    assert test_greaterthan_equal[0] == "<"
    assert test_greaterthan_equal[1] == "<="

    test_equal = []
    for op in filter.get_complementary_ops("="):
        test_equal.append(op)
    assert test_equal[0] == "<"
    assert test_equal[1] == ">"
    assert test_equal[2] == "<="
    assert test_equal[3] == ">="
