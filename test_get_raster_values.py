import landcover_rf

#locate input files
train_sample =  "sample/sample_train_tdx20130810.shp"
tsx_img = "tsx/tdx20130810.tif"

#extract
r_values = landcover_rf.stack_values(shp = train_sample, raster = tsx_img)