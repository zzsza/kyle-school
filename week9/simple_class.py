class Queue:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def first(self):
        return self.items[0]

    def last(self):
        return self.items[-1]

    def length(self):
        return len(self.items)

