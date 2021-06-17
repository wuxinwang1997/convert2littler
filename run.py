from src.read_hy2b import read_hy2b
from src.make_littler import header_record, data_record, ending_record
import argparse
import os
import gc
import logging

def create_logger(log_name, log_file):
    """
    This function is used to generate logger for the whole program
    :param log_name: The name of the logger
    :param log_file: The output log file to save logging
    :return: logger
    """
    logger = logging.getLogger(log_name)
    logger.setLevel(level=logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    stream_handlers = logging.StreamHandler()  # 往屏幕上输出
    stream_handlers.setFormatter(formatter)
    logger.addHandler(stream_handlers)

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

def hy2b2littler(logger, input_file, output_folder):
    """
    This function is used to convert hy2b into littler format
    :param logger: the logger to log the whole process
    :param input_file: the path of raw hdf5 format hy2b file
    :param output_folder: the folder where to save littler format files
    :return: None
    """
    hy2b, date = read_hy2b(input_file)
    output_path = f'{output_folder}/{date}'
    if not os.path.exists(output_path):
        os.mkdir(output_path)
        logger.info(f"Makeing output folder for {input_file}")
    output_file = f'{output_path}/obs.{date}'
    logger.info(f"Start converting {input_file} into {output_file}")
    file = open(output_file, mode='a')
    for i in range(len(hy2b)):
        hr = header_record(lat=hy2b['lat'][i],
                           lon=hy2b['lon'][i],
                           date=date)
        hr.write(file)
        del hr
        file.write('\n')
        dr = data_record(wind_speed=hy2b['wind_speed'][i],
                         wind_dir=hy2b['wind_dir'][i])
        dr.write(file)
        del dr
        file.write('\n')
        er = ending_record()
        er.write(file)
        del er
        file.write('\n')
        gc.collect()
    file.close()
    logger.info(f"{input_file}'s convertion is done.")

def main():
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument("--input_folder", type=str, default="./data/hy2b")
    parser.add_argument("--output_folder", type=str, default="./data/littler")
    parser.add_argument("--log_path", type=str, default="./logs/run.log")
    args = parser.parse_args()
    input_folder = args.input_folder
    output_folder = args.output_folder
    log_path = args.log_path
    logger = create_logger('convert2littler', log_path)

    logger.info("Start logging!")
    logger.info("Start searching qscat files")
    input_files = os.listdir(input_folder)
    qscat_filenames = []
    for input_file in input_files:
        if os.path.splitext(input_file)[1] == '.h5':
            qscat_filenames.append(f'{input_folder}/{input_file}')
    logger.info("Qscat file paths are ready!")

    for qscat_filename in qscat_filenames:
        hy2b2littler(logger, qscat_filename, output_folder)

    logger.info("Converting done!")

if __name__ == '__main__':
    main()