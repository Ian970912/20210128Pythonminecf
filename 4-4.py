from mcpi.minecraft import Minecraft
mc=Minecraft.create()
list2=[[12,41,14],[35,73,86]]
ID=mc.getPlayerEntityId("ian0912")
x,y,z=mc.entity.getTilePos(ID)
startX=x
for i in list2:
    for j in i:
        mc.setBlock(x,y,z,j)
        x=x+1
    x=startX
    z=z-1