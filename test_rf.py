import lccrf

#locate input files
train_table =  "sample/sample_train_tdx20130810.dbf"
test_table =  "sample/sample_test_tdx20130810.dbf"
train_sample =  "sample/sample_train_tdx20130810.shp"
test_sample = "sample/sample_test_tdx20130810.shp"
tsx_img = "tsx/tdx20130810.tif"

#Locate output files
out_train_class = "input arrays/train_classID.npy"
out_train_multi = "input arrays/train_multiband.npy"
out_test_class = "input arrays/test_classID.npy"
out_test_multi = "input arrays/test_multiband.npy"
out_sav = "model sav/rf.sav"
out_predict_test = "output arrays/test_result.npy"
tsx_img_array = "input arrays/raster.npy"
out_predict_raster = "output arrays/raster_result.npy"
out_raster = "output raster/class_tdx20130810.tif"

"""
1) train RF
"""
#Read Class ID from train sample
train_class = lccrf.read_class(tabular_data = train_table, gt_array_file = out_train_class)
#Read raster values based on train sample
train_values = lccrf.stack_values(shp = train_sample, raster = tsx_img, multibandfile = out_train_multi)
#train rf
model = lccrf.train_rf(trees = 400, train_multiband_array = train_values,
	train_class_array = train_class, model_sav = out_sav)

"""
2) predict test sample
"""
#Read Class ID from test sample
test_class = lccrf.read_class(tabular_data = test_table, gt_array_file = out_test_class)
#Read raster values based on test sample
test_values = lccrf.stack_values(shp = test_sample, raster = tsx_img, multibandfile = out_test_multi)
#predict test sample raster values
test_result = lccrf.predict_rf(rf = model, img = test_values, result_array_file = out_predict_test)

#assess accuracy and confusion matrix
lccrf.test_accuracy(test_array = test_result, gt_test_array = test_class)

"""
3) predict the whole image
"""
#save raster into Numpy array
raster_array = lccrf.read_img(TSXimage = tsx_img, multiband_array_file = tsx_img_array)
#predict test samples raster values
raster_result = lccrf.predict_rf(rf = model, img = raster_array, result_array_file = out_predict_raster)
#draw rasterfile from the result
lccrf.rasterize(img_path = tsx_img, result_array = raster_result, result_raster = out_raster)