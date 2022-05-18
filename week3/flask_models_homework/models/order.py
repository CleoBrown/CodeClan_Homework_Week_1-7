class Order:
    def __init__(self, customer_name, order_date, quantity, game_title, order_ref):
        self.name = customer_name
        self.date = order_date
        self.quantity = quantity
        self.title = game_title
        self.order_ref = order_ref
