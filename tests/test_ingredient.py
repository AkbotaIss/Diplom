from praktikum.ingredient import Ingredient


def test_ingredient_initializes_with_type_name_and_price():
    ingredient = Ingredient(ingredient_type="sauce", name="Cheese", price=50)

    assert ingredient.type == "sauce"
    assert ingredient.name == "Cheese"
    assert ingredient.price == 50


def test_get_price_returns_ingredient_price():
    ingredient = Ingredient(ingredient_type="sauce", name="Cheese", price=50)

    assert ingredient.get_price() == 50


def test_get_name_returns_ingredient_name():
    ingredient = Ingredient(ingredient_type="sauce", name="Cheese", price=50)

    assert ingredient.get_name() == "Cheese"


def test_get_type_returns_ingredient_type():
    ingredient = Ingredient(ingredient_type="sauce", name="Cheese", price=50)

    assert ingredient.get_type() == "sauce"
