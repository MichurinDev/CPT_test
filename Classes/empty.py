class EmptyObj:
    def __init__(self, min_permis_dist, start_x=0, start_y=0, name="Объект"):
        self.min_permis_dist = min_permis_dist
        self.x = start_x
        self.y = start_y
        self.name = name

    async def set_coords(self, x, y, others) -> None:
        self.x = x
        self.y = y
        dist_to_other_obj = await self.check_distance(others)
        return dist_to_other_obj

    async def get_coords(self) -> tuple:
        return (self.x, self.y)
    
    async def get_distance(self, other) -> float:
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    async def check_distance(self, others=None) -> str:
        if not others:
            return None

        return [(f"{other.name} in {self.name}", await self.get_distance(other) <= self.min_permis_dist) for other in others]
