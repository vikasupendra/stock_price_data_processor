import argparse
import pandas as pd
import mplfinance as mpf


class CSVDataProcessor():
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file)
        
           
    def query_1(self):
        #1. Compute some basic information about the data set:
            #a. What is the max, min, and average value (you may use the close price for the calculation or any other derivative if you’d like)
            #b. Ensure that the time series data is clean. In the event a row is out of order or a duplicate exists please ignore the record and report them out after the processing (the current data set does not include any dirty records)
        
        duplicate_rows = self.df[self.df.duplicated()]
        
        if duplicate_rows.empty:
            print('No Duplicates present')
        else:
            print('Duplicates present: {}'.format(duplicate_rows))
            

        self.df.drop_duplicates()
        min_price = self.df['AAPL.Close'].min()
        max_price = self.df['AAPL.Close'].max()
        avg_price = self.df['AAPL.Close'].mean()        

        print('---------------------------------- Min, Max and Average price of AAPL.Close ---------------------------------------')
        print('min_price: {} | max_price: {} | avg_price: {}'.format(min_price, max_price, avg_price))
        print('\n')

    def query_2(self, csv_output_file):
        # 2. Find the average volume for the entire data set, please filter out any rows that are below this value and save the result set to a new csv file

        avg_volume = self.df['AAPL.Volume'].mean()     
        print('---------------------------------- Average volume of the AAPL stock ---------------------------------------')
        print('avg_volume: {}'.format(avg_volume))
        print('\n')

        rows_below_avg_volume = self.df[self.df['AAPL.Volume'] < avg_volume]
        rows_below_avg_volume.to_csv(csv_output_file, index=False)                          # write filtered rows to a new CSV

    def query_3(self):
        # 3. Please also add the actual day of the entry into its own column (e.g., Monday, Tuesday, etc.)
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self.df['DayOfWeek'] = self.df['Date'].dt.day_name()

        print('---------------------------------- Stock Data with the Day of the week column added ---------------------------------------')
        print(self.df.head())
        print('\n')


    def query_4(self, csv_output_file):        
        # 4. Please aggregate the data sets to a week level and save the new data set as a separate csv file      
        
        self.df.set_index('Date', inplace=True)                                                             # Set the Date column as the index - needed for resample()

        self.grouped_df = self.df['AAPL.Close'].resample('W-Fri').agg(['min', 'max', 'mean'])               # Resample date field by end of week as Friday and group by date + aggregate min, max, and avg of 'AAPL.Close'. 
        self.grouped_df.reset_index(inplace=True)
        
        self.grouped_df.to_csv(csv_output_file, index=False)       

    def query_5(self):

        self.df.reset_index(inplace=True)
        
        cols = ['Date', 'AAPL.Open', 'AAPL.High', 'AAPL.Low', 'AAPL.Close', 'AAPL.Volume']

        new_df = self.df[cols]
        new_df['Date'] = pd.to_datetime(new_df['Date'])
        new_df.rename(columns={'AAPL.Open': 'Open', 'AAPL.High': 'High', 'AAPL.Low': 'Low', 'AAPL.Close': 'Close'}, inplace=True)
        new_df.set_index('Date', inplace=True)

        mpf.plot(new_df, type='candle', volume=False, style='yahoo')                    # Create the candlestick chart

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Process csv data ...')
    parser.add_argument('--csv_input_file_name', help = 'csv_input_file_name')
    parser.add_argument('--csv_output_file_below_avg_vol', help = 'csv_output_file_below_avg_vol')
    parser.add_argument('--csv_output_file_aggregates', help = 'csv_output_file_aggregates')

    args = parser.parse_args()
    csv_input_file = args.csv_input_file_name
    csv_output_file_below_avg_vol = args.csv_output_file_below_avg_vol
    csv_output_file_aggregates = args.csv_output_file_aggregates

    csv_data_proc_obj = CSVDataProcessor(csv_input_file)
    csv_data_proc_obj.query_1()
    csv_data_proc_obj.query_2(csv_output_file_below_avg_vol)
    csv_data_proc_obj.query_3()
    csv_data_proc_obj.query_4(csv_output_file_aggregates)
    csv_data_proc_obj.query_5()

