import lccrf

#locate input files
train_table =  "sample/sample_train_tdx20130810.dbf"
output = "input arrays/train_classID.npy"

#call function
gt_array = lccrf.read_class(tabular_data = train_table, gt_array_file = output)