import arcpy
import os

gdb_path = r"D:\Bharati\Sem_3\Programming_3\P2_describing_data\Practical_2_ProProject\Practical_2_ProProject\02_Describing_Data.gdb"
fc_class_list = ["Freeways", "MajorAttractions"]

for fc in fc_class_list:
    fc_path = os.path.join(gdb_path, fc)
    fc_obj = arcpy.Describe(fc_path)
    print("The geometry of {} is {}".format(fc,fc_obj.shapeType))
    shape_type = fc_obj.shapeType
    fc_name = fc_obj.name
    dataset_Type = fc_obj.datasetType
    print("The datasets are {} is {} and the type is {}".format(dataset_Type, fc_name, shape_type))

    sr_obj = fc_obj.spatialReference
    print(sr_obj.name)
    print(sr_obj.type)

    field_list = fc_obj.fields
    for field in field_list:
            print(field.name)
            print(field.type)
