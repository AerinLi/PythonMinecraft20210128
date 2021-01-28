from mcpi.minecraft import Minecraft
Aerin = Minecraft.create()
list2 = [[14,15,16],[56,129,20]]
myID = Aerin.getPlayerEntityId("APE_43")
x,y,z = Aerin.entity.getTilePos(myID)
startX = x
for i in list2:
    for j in i:
        Aerin.setBlock(x,y,z,j)
        x = x+1
    x = startX
    z = z-1