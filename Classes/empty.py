class EmptyObj:
    def __init__(self, min_permis_dist, start_x=0, start_y=0, name="Объект"):
        self.min_permis_dist = min_permis_dist
        self.x = start_x
        self.y = start_y
        self.name = name

    async def set_coords(self, x, y, others) -> None:
        self.x = x
        self.y = y
        self.check_distance(others)

    async def get_coords(self) -> tuple:
        return (self.x, self.y)
    
    async def get_distance(self, other) -> float:
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    async def check_distance(self, others=None) -> str:
        if not others:
            return None

        for other in others:
            return (other, await self.get_distance(other) <= self.min_permis_dist)
