from Classes.empty import EmptyObj as emp
import asyncio
import time

async def main():
    a = emp(min_permis_dist=10, name="Трактор")
    b = emp(min_permis_dist=3, name="Грузовик")
    ent = emp(min_permis_dist=0, name="Вход")

    with open('coords.txt') as f:
        coords = f.readlines()
    
    objs = [a, b, ent]

    for line in coords:
        new_a_coords, new_b_coords = list(map(lambda x: list(map(int, x.split(","))), line[:-1].split(';')))
        responce = [await a.set_coords(*new_a_coords, objs),
                    await b.set_coords(*new_b_coords, objs)]

        print(" | ".join([f"{obj.name}: {await obj.get_coords()}" for obj in objs]))
        print(responce)

        time.sleep(1)
    

if __name__ == '__main__':
    asyncio.run(main())
