# convert2littler

## 📌&nbsp;&nbsp;Introduction

This project is used to convert some other format observation data into LITTLER format file to prepare for WRFDA.

**Why you should use it**: it allows you to convert a lot of HY-2B L2B h5 file into LITTLER using a simple command.

## Project Structure

The directory structure of this project looks like this:

```
├── src                 <- Source of the codes
│   ├── make_littler           <- Making LITTLER format files
│   ├── read_hy2b              <- Reading wind speed and wind direction from a HY-2B L2B h5 file.
│   ├── utils                  <- Utils for the project.
│
├── data                    <- Project data
│	├── hy2b           			<- Folder to save input HY-2B files
│   ├── littler                 <- Folder to save output LITTLER files
│
├── logs                    <- Logs generated by logging
│
├── run.py                  <- Run the whole program to convert hdf5 into littler
│
├── .gitignore              <- List of files/folders ignored by git
├── requirements.txt        <- File for installing python dependencies
├── LICENSE
└── README.md
```

<br>

## 🚀&nbsp;&nbsp;Quickstart

```yaml
# clone project
git clone https://github.com/wuxinwang1997/hy2b2littler
cd hy2b2littler

# [OPTIONAL] create conda environment
conda env create -n myenv python=3.8
conda activate myenv

# install requirements
pip install -r requirements.txt
```

When running `python run.py --input_folder ./data/hy2b --output_folder ./data/littler --log_path ./logs/run.log` you should see something like this:

```
2021-06-17 20:02:35,132 - convert2littler - INFO - Start logging!
2021-06-17 20:02:35,132 - convert2littler - INFO - Start searching qscat files
2021-06-17 20:02:35,134 - convert2littler - INFO - Qscat file paths are ready!
2021-06-17 20:02:35,255 - convert2littler - INFO - Makeing output folder for ./data/hy2b/H2B_OPER_SCA_L2B_OR_20210426T200703_20210
426T215126_12546_pwp_250_07_owv.h5
2021-06-17 20:02:35,255 - convert2littler - INFO - Start converting ./data/hdf5/H2B_OPER_SCA_L2B_OR_20210426T200703_20210426T21512
6_12546_pwp_250_07_owv.h5 into ./data/littler/2021042620/obs.2021042620
2021-06-17 20:21:08,660 - convert2littler - INFO - ./data/hy2b/H2B_OPER_SCA_L2B_OR_20210426T200703_20210426T215126_12546_pwp_250_0
7_owv.h5's convertion is done.
2021-06-17 20:21:08,666 - convert2littler - INFO - Converting done!
```

## Todo List

If there are other format that need to be converted into LITTLER format I will add the code.

## Contributing

Feel free to dive in! [Open an issue](https://github.com/wuxinwang1997/convert2littler/issues/new) or submit PRs.

## License

[MIT © Richard McRichface.](../LICENSE)

