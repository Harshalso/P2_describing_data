import arcpy

raster_path = r"D:\Bharati\Sem_3\Programming_3\P2_describing_data\Practical_2_ProProject\Practical_2_ProProject\RASTER_DATA\erelev"
desc_obj = arcpy.Describe(raster_path)
dataset_type = desc_obj.datasetType

print(dataset_type)
print(desc_obj.bandCount)
print(desc_obj.format)
print(desc_obj.pixelType)
