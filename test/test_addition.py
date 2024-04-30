from AutomationProjectClass.PytestPractice.src.calculator import add

# all positive test cases
# assert use to compare original result & expected result

def test_add_positive_numbers():
    assert add(2,5)==7

def test_add_negative_numbers():
    assert add(-2,-9)==-11

def test_add_mixed_numbers():
    assert add(2,-5)==-3