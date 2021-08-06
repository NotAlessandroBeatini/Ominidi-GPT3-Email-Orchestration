class Order:
    def __init__(self, po, categories, positions, action):
        self.po = po
        self.categories = categories
        self._positions = positions if positions else ["alle"]
        self.action = action

    @property
    def is_open(self):
        return self.action == "Open"

    @property
    def positions(self):
        return ", ".join(self._positions)

    def to_dict_item(self):
        return {
                'PO': self.po,
                'Positions': self._positions,
                'Action': self.action,
                'Type': self.categories
                }

class JsonOrder(Order):
    def __init__(self, json_data):
        super().__init__(
                json_data["PO"],
                json_data["Type"],
                json_data["Positions"],
                json_data["Action"])
