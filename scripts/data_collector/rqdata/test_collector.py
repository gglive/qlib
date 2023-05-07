from collector import Run


run = Run(source_dir = 'E:/data/qlib_data/ebs_data/csv_data', normalize_dir = 'E:/data/qlib_data/ebs_data/normalize', interval='1d')
#--source_dir E:/data/qlib_data/ebs_data/csv_data --normalize_dir E:/data/qlib_data/ebs_data/normalize
run.normalize_data()