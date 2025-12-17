from praktikum.bun import Bun


class TestBun:
    def test_bun_initializes_with_name_and_price(self):
        bun = Bun(name="Black Bun", price=100)

        assert bun.name == "Black Bun"
        assert bun.price == 100

    def test_get_name_returns_bun_name(self):
        bun = Bun(name="Black Bun", price=100)

        assert bun.get_name() == "Black Bun"

    def test_get_price_returns_bun_price(self):
        bun = Bun(name="Black Bun", price=100)

        assert bun.get_price() == 100