from mcpi.minecraft import Minecraft
mc=Minecraft.create()
from random import randrange
for i in range(10):
    x,y,z=mc.player.getTilePos()
    z=z+i
    for j in range(10):
        c=randrange(0,16)
        x=x+1
        mc.setBlock(x,y,z,35,c)
        
A=randrange(0,16)
while True:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
        h=hits[0]
        b=mc.getBlockWithData(h.pos)
        data=b.data
        if data == A:
            mc.postToChat("找到了!")
            mc.setBlock(h.pos,57)
            break
        elif data<A:
            mc.postToChat("找錯了!再找大一點的!")
        elif data>A:
            mc.postToChat("找錯了!再找小一點的!")