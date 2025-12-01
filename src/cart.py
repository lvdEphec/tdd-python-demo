class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append(price)

    def calculate_total(self):
        total = sum(self.items)
        
        # Règle métier : Si supérieur STRICTEMENT à 100
        if total > 100:
            # 10% de réduction au final, on me l'a bien confirmé !
            return total * (1 - 0.10)
            
        return total
    