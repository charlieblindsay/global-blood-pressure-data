import pandas as pd

from utilities.file_paths import raw_data_path, processed_data_path
from utilities.data_cleaning import produce_processed_world_bank_data

produce_processed_world_bank_data('population_data.csv')
produce_processed_world_bank_data('GDP_data.csv')