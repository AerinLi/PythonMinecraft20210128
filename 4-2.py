from mcpi.minecraft import Minecraft
Aerin = Minecraft.create()
import random
x,y,z = Aerin.player.getTilePos()
for i in range(20):
    r = random.randrange(1,7)
    if r == 1:
        Aerin.setBlocks(x,y,z,x,y,z+4,79)
        z = z+4
    if r == 2:
        Aerin.setBlocks(x,y,z,x,y,z-4,57)
        z = z-4
    if r == 3:
        Aerin.setBlocks(x,y,z,x+4,y,z,56)
        x = x+4
    if r == 4:
        Aerin.setBlocks(x,y,z,x-4,y,z,22)
        x = x-4
    if r == 5:
        Aerin.setBlocks(x,y,z,x,y+4,z,21)
        y = y+4
    if r == 6:
        Aerin.setBlocks(x,y,z,x,y-4,z,20)
        y = y-4