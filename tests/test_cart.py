import pytest
from src.cart import ShoppingCart

class TestShoppingCart:
    
    def test_calculate_total_standard(self):
        # Cas 1 : Somme simple
        cart = ShoppingCart()
        cart.add_item("Pomme", 10.0)
        cart.add_item("Banane", 5.0)
        assert cart.calculate_total() == 15.0

    def test_calculate_total_limit_100(self):
        # Cas 2 : Limite pile (100€) -> PAS de réduction
        cart = ShoppingCart()
        cart.add_item("Article A", 50.0)
        cart.add_item("Article B", 50.0)
        assert cart.calculate_total() == 100.0

    def test_calculate_total_with_discount(self):
        # Cas 3 : Réduction (> 100€) -> -10%
        cart = ShoppingCart()
        cart.add_item("Champagne", 100.0)
        cart.add_item("Caviar", 100.0) # Total 200
        # 200 - 10% = 180
        assert cart.calculate_total() == 180.0