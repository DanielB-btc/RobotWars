class Map:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

        self.map_data: list[list[str]]

        self.generate_map()

    def generate_map(self) -> None:
        self.map_data = [["." for _ in range(self.width)] for _ in range(self.height)]

    def display_map(self) -> None:
        frame = "x" + self.width * "=" + "x"
        print(frame)
        for row in self.map_data:
            print("|" + "".join(row) + "|")
        print(frame)
