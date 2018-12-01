def checkPositive(myValue, myVariableName):
    """ Checks the value to see if it's negative
    :param myValue : float
    :param myVariableName : str
    :return: valueError
    """
    if myValue < 0.0:
        negValueError = ValueError(myVariableName + ' should be a positive')
        raise negValueError