from mcpi.minecraft import Minecraft
Aerin = Minecraft.create()
from random import randrange
for i in range(10):
    x,y,z = Aerin.player.getTilePos()
    z = z+i
    for j in range(10):
        color = randrange(0,16)
        x = x+1
        Aerin.setBlock(x,y,z,35,color)
ans = randrange(0,16)
while True:
    hits = Aerin.events.pollBlockHits()
    if len(hits)>0:
        h = hits[0]
        block = Aerin.getBlockWithData(h.pos)
        data = block.data
        if data == ans:
            Aerin.postToChat("恭喜你找到啦")
            Aerin.setBlock(h.pos,57)
            break
        elif data < ans:
            Aerin.postToChat("找錯囉~~~ 找大一點的吧!")
        elif data > ans:
            Aerin.postToChat("找錯囉~~~ 找小一點的吧!")








