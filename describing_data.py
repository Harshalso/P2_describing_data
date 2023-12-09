import arcpy
import os

MajorAttractions_feature_class_path =  r"D:\Bharati\Sem_3\Programming_3\P2_describing_data\Practical_2_ProProject\Practical_2_ProProject\02_Describing_Data.gdb\MajorAttractions"
MajorAttractions_desc_Object = arcpy.Describe(MajorAttractions_feature_class_path)

print(MajorAttractions_desc_Object.shapeType)

gdb_path = r"D:\Bharati\Sem_3\Programming_3\P2_describing_data\Practical_2_ProProject\Practical_2_ProProject\02_Describing_Data.gdb"
freeway_fc_name = "Freeways"
freeway_fc_path = os.path.join(gdb_path,freeway_fc_name)
freeway_desc_object = arcpy.Describe(freeway_fc_path)
print(freeway_desc_object.shapeType)
