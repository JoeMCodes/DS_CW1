setup: requirements.txt
	pip install -r requirements.txt

get_raw_data:
	src\data-gathering\get_data.py



make_plots: \src\data-gathering\get_data.py \src\data-cleaning\extract_data.py \src\creat-plots\make_figure-1.py \src\creat-plots\make_figure-2.py

