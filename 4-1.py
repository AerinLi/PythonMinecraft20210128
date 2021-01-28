from mcpi.minecraft import Minecraft
Aerin = Minecraft.create()
import random
x,y,z = Aerin.player.getTilePos()
for i in range(20):
    r = random.randrange(1,5)
    if r == 1:
        Aerin.setBlocks(x,y,z,x,y,z+4,95)
        z = z+4
    if r == 2:
        Aerin.setBlocks(x,y,z,x,y,z-4,95)
        z = z-4
    if r == 3:
        Aerin.setBlocks(x,y,z,x+4,y,z,95)
        x = x+4
    if r == 4:
        Aerin.setBlocks(x,y,z,x-4,y,z,95)
        x = x-4