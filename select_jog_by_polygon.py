
import arcpy

user_input = '''POLYGON ((93.7825988660001 31.0,97.0246144870001 34.4845636900001,101.57533366
                35.40660483,105.62041737 31.5697239580001,101.277901035 27.0,98.3333180400001 
                28.654884226,93.7825988660001 31.0))'''


arcpy.CreateFeatureclass_management('in_memory', 'sel', 'POLYGON')

with arcpy.da.InsertCursor('in_memory/sel', ['SHAPE@']) as cursor:
    polygon = arcpy.FromWKT(user_input)
    cursor.insertRow([polygon])

arcpy.MakeFeatureLayer_management('shp/jog.shp', 'jog_lyr') 
arcpy.SelectLayerByLocation_management('jog_lyr', 'intersect', 'in_memory/sel')

# arcpy.CopyFeatures_management('jog_lyr', r'C:\Users\Esri\Desktop\select.shp')

with arcpy.da.SearchCursor('jog_lyr', '*') as cursor:
    for row in cursor:
        print('{0}, {1}, {2}'.format(row[4], row[5], row[6]))
