# Add your imports here
import modules.sinu5oid as sinu5oid
import modules.baseRasteriser as rasteriser

if __name__ == "__main__":
    # Add your method calls below here:
    
    list = sinu5oid.generateList(15)
    print(list)
    print(sinu5oid.bubbleSort(list))
    # and above here
   
    buffer = rasteriser.createBuffer(48, 48)

    rasteriser.putPoint(buffer, 6, 16)
    rasteriser.putLine(buffer, 4, 56, 48, 16)
    rasteriser.putTriangle(buffer, 4, 4, 24, 6, 16, 24)
    rasteriser.putFilledTriangle(buffer, 16, 48, 48, 36, 24, 16)
    
    rasteriser.printBuffer(buffer)

    pass
