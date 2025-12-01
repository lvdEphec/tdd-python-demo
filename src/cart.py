class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append(price)

    def calculate_total(self):
        total = sum(self.items)
        
        # Règle métier : Si supérieur STRICTEMENT à 100, on applique 10%
        if total > 100:
            return total * 0.90
            
        return total