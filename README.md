# How to Run Project

To recreate the plots and compile the pdf the following scripts should be ran in order, and can be done so from the command.

First we you need to create a virtual environment and download the required packages.

- py -m venv venv

If on windows
- . venv/Scripts/activate

Unix
- venv/Bin/activate

Now you download the required packages
- pip install -r requirements.txt

Now you can run these scripts in order;

To download the data from the online database (This may take a while)
- py src/data_gathering/get_data.py

Extract the data and create csv file of useful information
- py src/data_cleaning/extract_data.py

Now create the two plots/ figures
- py src/create_plots/make_figure-1.py
- py src/create_plots/make_figure-2.py

Now to compile the tex file and create a pdf
- py src/create_report_pdf/compile_pdf.py

And now in the reports folder there is a markdown version of the report and a pdf version. Note that figures have been saved as pdf but also svg files for better quality and so the size can be easily manipulated