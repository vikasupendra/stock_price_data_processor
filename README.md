1. Compute some basic information about the data set:
    a. What is the max, min, and average value (you may use the close price for the calculation or any other derivative if you’d like)
    b. Ensure that the time series data is clean. In the event a row is out of order or a
duplicate exists please ignore the record and report them out after the processing (the current data set does not include any dirty records)

2. Find the average volume for the entire data set, please filter out any rows that are below this value and save the result set to a new csv file
3. Please also add the actual day of the entry into its own column (e.g., Monday, Tuesday, etc.)
4. Please aggregate the data sets to a week level and save the new data set as a separate csv file
5. Please graph the results from step #3 visually as a candlestick chart (you may utilize any open source library for this portion of the exercise)

Run the code using Docker
===========================
> Unzip the compressed files

Package installation:
> cd to <directory which has the raw csv file apple_data.csv and python file>

Run 
> pip3 install --no-cache-dir -r requirements.txt
OR
> pip3 install pandas==2.2.2
> pip3 install mplfinance==0.12.10b0

Run the code for all the queries:
> python3 csv_data_processor.py --csv_input_file_name apple_data.csv --csv_output_file_below_avg_vol <output_file.csv> --csv_output_file_aggregates <output_file_for_aggregates.csv>
> ex: python3 csv_data_processor.py --csv_input_file_name apple_data.csv --csv_output_file_below_avg_vol filtered.csv --csv_output_file_aggregates aggregates.csv
