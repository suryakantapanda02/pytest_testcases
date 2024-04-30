from AutomationProjectClass.PytestPractice.src.calculator import substract

# all positive test cases
# assert use to compare original result & expected result

def test_substract_positive_numbers():
    assert substract(2,5)==-3

def test_substract_negative_numbers():
    assert substract(-2,-3)==1

def test_substract_mixed_numbers():
    assert substract(2,-3)==5

def test_substract_mixed_numbers2():
    assert substract(-2,3)==-5