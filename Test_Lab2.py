import Lab2

def test_min_max():

    inputarray = [1, 2, 3, 4, 5]
    testresult = [1, 5]

    result = Lab2.find_min_max(inputarray)

    assert (result == testresult)

def test_avg():

    inputarray = [1, 2, 3, 4, 5]
    testresult = 3

    result = Lab2.calc_average(inputarray)

    assert (result == testresult)

def test_median():

    inputarray = [2, 4, 6, 8]
    testresult = 5

    result = Lab2.calc_median_temperature(inputarray)

    assert (result == testresult)