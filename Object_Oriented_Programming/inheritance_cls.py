class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f'Device {self.name!r} {self.connected_by!r}'

    def disconnect(self):
        self.connected = False
        print("Disconnected!!")

    def connect(self):
        self.connected = True
        print("Connected!!")


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} {self.remaining_pages} pages remaining"

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected")
            return
        print(f"Printing {self.remaining_pages} of pages")
        self.remaining_pages -= pages


printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)
printer.disconnect()
printer.print(20)
printer.connect()