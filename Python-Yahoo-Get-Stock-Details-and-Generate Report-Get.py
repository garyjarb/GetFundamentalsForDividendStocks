#A python script to get stock ticker fundamentals from Yahoo finance for dividend paying companies
#and generate a CSV report to calculate total cash vs dept, earnings quarterly growth, Payout ratio,
#dividend yield vs 5-year dividend yield and dividend growth.


#import libraries
import yfinance as yf
import csv
import time

INPUT_FILE_NAME = "symbols.csv"
OUTPUT_REPORT_NAME = "symbol_details_report.csv"

symbols_lst=[]

# read input ticker symbols file
file_in = open(INPUT_FILE_NAME, encoding="utf8")
with file_in as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            #uTitle=uTitle.replace("?","")
            symbols_lst.append(row[0])
                        
file_in.close()
############################
# Start formating data
for i in range(len(symbols_lst)):
    print(symbols_lst[i])


print("totalCash", end=",")
print("totalDebt", end=",")
print("earningsQuarterlyGrowth", end=",")
print("payoutRatio", end=",")
print("dividendYield", end=",")
print("fiveYearAvgDividendYield")
print("\n")


### Output generated results into a CSV file
file_out = open(OUTPUT_REPORT_NAME, "w")
file_out.write("Symbol")
file_out.write(",")
file_out.write("totalCash")
file_out.write(",")
file_out.write("totalDebt")
file_out.write(",")
file_out.write("earningsQuarterlyGrowth")
file_out.write(",")
file_out.write("payoutRatio")
file_out.write(",")
file_out.write("dividendYield")
file_out.write(",")
file_out.write("fiveYearAvgDividendYield")
file_out.write("\n")

# Get data from yahoo finance and start writing to a CSV file
for i in range(len(symbols_lst)):
    try:
            stock_details = yf.Ticker(symbols_lst[i])
            print(symbols_lst[i], end=",")
            file_out.write(symbols_lst[i])
            file_out.write(",")
            
            #print(stock_details.info['totalCash'], end=",")
            file_out.write(str(stock_details.info['totalCash']))
            file_out.write(",")
            
            #print(stock_details.info['totalDebt'], end=",")
            file_out.write(str(stock_details.info['totalDebt']))
            file_out.write(",")
            
            #print(stock_details.info['earningsQuarterlyGrowth'], end=",")
            file_out.write(str(stock_details.info['earningsQuarterlyGrowth']))
            file_out.write(",")
            
            #print(stock_details.info['payoutRatio'], end=",")
            file_out.write(str(stock_details.info['payoutRatio']))
            file_out.write(",")
            
            #print(stock_details.info['dividendYield'], end=",")
            file_out.write(str(stock_details.info['dividendYield']))
            file_out.write(",")
            
            #print(stock_details.info['fiveYearAvgDividendYield'])
            file_out.write(str(stock_details.info['fiveYearAvgDividendYield']))
            
            print("\n")
            file_out.write("\n")
            time.sleep(3)
    except:
        pass
    else:
        pass
    finally:
        pass
            
file_out.close()    



