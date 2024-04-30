from AutomationProjectClass.PytestPractice.src.calculator import multiply

# all positive test cases
# assert use to compare original result & expected result

def test_mul_positive_numbers():
    assert multiply(2,5)==10

def test_mul_negative_numbers():
    assert multiply(-2,-3)==6

def test_mul_mixed_numbers():
    assert multiply(2,-3)==-6

