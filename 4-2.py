from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
import random
for i in range(20):
    r=random.randrange(1,6)
    if r==1:
        mc.setBlocks(x,y,z,x,y,z+4,41)
        z=z+4
    if r==2:
        mc.setBlocks(x,y,z,x,y,z-4,41)
        z=z-4
    if r==3:
        mc.setBlocks(x+4,y,z,x,y,z,41)
        x=x+4
    if r==4:
        mc.setBlocks(x-4,y,z,x,y,z,41)
        x=x-4
    if r==5:
        mc.setBlocks(x,y-4,z,x,y,z,41)
        y-4
    if r==6:
        mc.setBlocks(x,y+4,z,x,y,z,41)
        y+4