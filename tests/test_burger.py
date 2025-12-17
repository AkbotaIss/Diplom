import pytest
from unittest.mock import Mock

from praktikum.burger import Burger


class TestBurger:
    def test_burger_initial_state(self):
        burger = Burger()

        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns_sets_bun(self):
        burger = Burger()
        bun_mock = Mock()

        burger.set_buns(bun_mock)

        assert burger.bun is bun_mock

    def test_add_ingredient_adds_ingredient_to_list(self):
        burger = Burger()
        ingredient_mock = Mock()

        burger.add_ingredient(ingredient_mock)

        assert burger.ingredients == [ingredient_mock]

    def test_remove_ingredient_removes_ingredient_by_index(self):
        burger = Burger()
        ingredient_1 = Mock()
        ingredient_2 = Mock()
        ingredient_3 = Mock()
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.add_ingredient(ingredient_3)

        burger.remove_ingredient(1)

        assert burger.ingredients == [ingredient_1, ingredient_3]

    def test_move_ingredient_changes_ingredients_order(self):
        burger = Burger()
        ingredient_1 = Mock()
        ingredient_2 = Mock()
        ingredient_3 = Mock()
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.add_ingredient(ingredient_3)

        burger.move_ingredient(0, 2)

        assert burger.ingredients == [ingredient_2, ingredient_3, ingredient_1]

    @pytest.mark.parametrize(
        "bun_price, ingredient_prices, expected_price",
        [
            (100, [], 200),
            (50, [10, 20], 130),
        ],
    )
    def test_get_price_returns_total_price(self, bun_price, ingredient_prices, expected_price):
        burger = Burger()

        bun_mock = Mock()
        bun_mock.get_price.return_value = bun_price
        burger.set_buns(bun_mock)

        for price in ingredient_prices:
            ingredient_mock = Mock()
            ingredient_mock.get_price.return_value = price
            burger.add_ingredient(ingredient_mock)

        total_price = burger.get_price()

        assert total_price == expected_price

    def test_get_receipt_returns_formatted_receipt(self):
        burger = Burger()

        bun_mock = Mock()
        bun_mock.get_name.return_value = "Test Bun"
        bun_mock.get_price.return_value = 100
        burger.set_buns(bun_mock)

        ingredient_mock = Mock()
        ingredient_mock.get_name.return_value = "Cheese"
        ingredient_mock.get_type.return_value = "sauce"
        ingredient_mock.get_price.return_value = 20
        burger.add_ingredient(ingredient_mock)

        receipt = burger.get_receipt()

        expected_receipt = "\n".join(
            [
                "(==== Test Bun ====)",
                "= sauce Cheese =",
                "(==== Test Bun ====)\n",
                "Price: 220",
            ]
        )

        assert receipt == expected_receipt
