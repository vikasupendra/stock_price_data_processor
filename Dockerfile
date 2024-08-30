FROM python:3.9-slim-buster

RUN mkdir /home/app
COPY csv_data_processor.py /home/app
COPY apple_data.csv /home/app
COPY requirements.txt /home/app/requirements.txt

RUN pip3 install --no-cache-dir -r /home/app/requirements.txt

CMD ["python3", "/home/app/csv_data_processor.py", "--csv_input_file_name", "/home/app/apple_data.csv", "--csv_output_file_below_avg_vol", "filtered.csv", "--csv_output_file_aggregates", "aggregates.csv"]