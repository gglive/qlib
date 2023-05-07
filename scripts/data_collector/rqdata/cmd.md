cd .\scripts\data_collector\rqdata\
python collector.py download_data --source_dir E:/data/qlib_data/ebs_data/csv_data --start 2005-01-01 --end 2023-05-05 --delay 0 --interval 1d --region CN
python collector.py normalize_data --source_dir E:/data/qlib_data/ebs_data/csv_data --normalize_dir E:/data/qlib_data/ebs_data/normalize --region cn --interval 1d

cd ..
cd ..
python dump_bin.py dump_all --csv_path E:/data/qlib_data/ebs_data/normalize --qlib_dir E:/data/qlib_data/ebs_data --freq day --date_field_name date --include_fields prev_close,open,high,low,close,factor,volume,total_turnover