def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
