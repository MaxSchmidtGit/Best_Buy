import pytest
from products import Product, NonStockedProduct, LimitedProduct
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree


def test_create_normal_product():
    product = Product("Test Product", price=100, quantity=10)
    assert product.name == "Test Product"
    assert product.price == 100
    assert product.quantity == 10
    assert product.is_active()


def test_create_product_with_invalid_details():
    with pytest.raises(ValueError):
        Product("", price=100, quantity=10)
    with pytest.raises(ValueError):
        Product("Test Product", price=-100, quantity=10)
    with pytest.raises(ValueError):
        Product("Test Product", price=100, quantity=-10)


def test_product_reaches_zero_quantity():
    product = Product("Test Product", price=100, quantity=1)
    product.buy(1)
    assert not product.is_active()


def test_product_purchase_modifies_quantity_and_returns_price():
    product = Product("Test Product", price=100, quantity=10)
    total_price = product.buy(2)
    assert product.quantity == 8
    assert total_price == 200


def test_buying_larger_quantity_than_exists():
    product = Product("Test Product", price=100, quantity=10)
    with pytest.raises(ValueError):
        product.buy(11)


def test_non_stocked_product():
    product = NonStockedProduct("Non-Stocked Product", price=50)
    assert product.quantity == 0
    total_price = product.buy(5)
    assert total_price == 250


def test_limited_product():
    product = LimitedProduct("Limited Product", price=20, quantity=50, maximum=5)
    total_price = product.buy(5)
    assert total_price == 100
    with pytest.raises(ValueError):
        product.buy(6)


def test_percent_discount_promotion():
    product = Product("Test Product", price=100, quantity=10)
    promotion = PercentDiscount("20% off", 20)
    product.set_promotion(promotion)
    total_price = product.buy(5)
    assert total_price == 400  # 20% off on 500


def test_second_half_price_promotion():
    product = Product("Test Product", price=100, quantity=10)
    promotion = SecondHalfPrice("Second half price")
    product.set_promotion(promotion)
    total_price = product.buy(4)
    assert total_price == 300  # 100 + 50 + 100 + 50


def test_third_one_free_promotion():
    product = Product("Test Product", price=100, quantity=10)
    promotion = ThirdOneFree("Third one free")
    product.set_promotion(promotion)
    total_price = product.buy(6)
    assert total_price == 400  # 100 + 100 + 0 + 100 + 100 + 0


if __name__ == "__main__":
    pytest.main()
