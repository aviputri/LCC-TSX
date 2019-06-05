import lccrf

#locate input files
train_sample =  "sample/sample_train_tdx20130810.shp"
tsx_img = "tsx/tdx20130810.tif"

#extract
r_values = lccrf.stack_values(shp = train_sample, raster = tsx_img)