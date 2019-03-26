import pytest

@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 40),
    (20, 2, 38),
])
def test_transactions(wallet, earned, spent, expected):
    wallet.add_cash(earned)
    wallet.spend_cash(spent)
    assert wallet.balance == expected