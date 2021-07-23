from emailLogic import validateInputs

def test_validateInputs_GivenValidInputs_ShouldReturnTrue():
    input = {
        "To": ["bj.mccotter@veteransunited.com"],
        "From": "pyf5@no-reply.com",
        "Subject": "Hello",
        "Bcc": [""],
        "Cc" : [""],
        "Body": "Hello! Did you get this test email?"
    }
    actual = validateInputs(input)[0]
    assert True == actual

def test_validateInputs_GivenInValidToAddress_ShouldReturnFalse():
    input = {
        "To": [""],
        "From": "pyf5@no-reply.com",
        "Subject": "Hello",
        "Bcc": [""],
        "Cc" : [""],
        "Body": "Hello! Did you get this test email?"
    }
    actual = validateInputs(input)[0]
    assert False == actual

def test_validateInputs_GivenOneInValidToAddress_ShouldReturnFalse():
    input = {
        "To": ["bj.mccotter@veteransunited.com", ""],
        "From": "pyf5@no-reply.com",
        "Subject": "Hello",
        "Bcc": [""],
        "Cc" : [""],
        "Body": "Hello! Did you get this test email?"
    }
    actual = validateInputs(input)[0]
    assert False == actual

def test_validateInputs_GivenInValidFromAddress_ShouldReturnFalse():
    input = {
        "To": ["bj.mccotter@veteransunited.com"],
        "From": "",
        "Subject": "Hello",
        "Bcc": [""],
        "Cc" : [""],
        "Body": "Hello! Did you get this test email?"
    }
    actual = validateInputs(input)[0]
    assert False == actual

def test_validateInputs_GivenInValidBody_ShouldReturnFalse():
    input = {
        "To": ["bj.mccotter@veteransunited.com"],
        "From": "pyf5@no-reply.com",
        "Subject": "Hello",
        "Bcc": [""],
        "Cc" : [""],
        "Body": ""
    }
    actual = validateInputs(input)[0]
    assert False == actual
