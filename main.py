import os
import glob
import csv
import pandas as pd
from sqlalchemy import create_engine, types

# NEED TO REMOVE PT PASSWORD
ENGINE = create_engine('mysql+pymysql://root:passwd@localhost/INTERVIEW')
PATH = '/root/data/'

def get_csv_list(root_path):
    """ Find all csv data files in all subdirectories """
    
    os.chdir(root_path)
    result = glob.glob( '*/data/*.csv' )
    non_empty_result = list(filter(lambda file: os.stat(file).st_size > 0, result))
    return non_empty_result

def load_data(ENGINE, PATH, files):
    """ Derive table name, load csv data and answers to Questions (1,3) into database INTERVIEW """
    ttl_rows = ttl_columns = 0

    for f in files:
        table_name = f.replace('/','_')[:-4].upper()
        # MySQL Table Name Length Check
        if len(table_name) > 63:
            table_name = table_name[:63]
        print('Table Name: ' + table_name)
        df = pd.read_csv(PATH + str(f), sep=None, quotechar='\"', encoding='utf8')

        # Store cumulative number of columns/fields and rows
        r, c = df.shape
        ttl_rows += r
        ttl_columns += c

        df.to_sql(table_name, con=ENGINE, index=False, if_exists='replace')

    # Questions 1 and 3 Data Load
    ttl_rows_avg_columns = [(3, ttl_rows), (1, ttl_columns/len(files))]
    answers = pd.DataFrame(ttl_rows_avg_columns, columns =['Question', 'Answer'])
    answers.to_sql('ANSWER_TABLE_1_3', con=ENGINE, index=False, if_exists='replace')

    return


def question_two(ENGINE, PATH, file_list):
    """ Create word frequency count for all text within files load to table"""

    frequency = {}
    for file in file_list:
        document_text = open(PATH + file, 'r')
        document_string = re.sub(r'[^\w\s]', ' ', document_text.read()).lower()
        for word in document_string.split():
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1

    df = pd.DataFrame(list(frequency.items()),columns = ['value','cnt'])
    df.to_sql('ANSWER_TABLE_2', con=ENGINE, index=False, if_exists='replace')


def main():
    # Gather list of csv files
    file_list = get_csv_list(PATH)
    # Load tables in DB, load answers to Question #1 and #3
    load_data(ENGINE, PATH, file_list)
    # Load answers to Question #2
    question_two(ENGINE, PATH, file_list)

