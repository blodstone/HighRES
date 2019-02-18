# Production Enviroment should be set to 'production'
FLASK_ENV="development"
# First and second arguments are only used in unittest
FLASK_APP="backend.app:create_app(None, False)"

# Uncomment this to debug:
FLASK_DEBUG=1

# Generate secret key using: python -c 'import os; print(os.urandom(24))'
SECRET_KEY=b'\xcf\xdcp\xe0\xbd;\xd4%#\x16\xdf\x05\xfc\xcd_\x0f'

# Change this in accordance to the server setting
DB_URI="mysql://root:wildanimus@localhost/harness_test"


# Uncomment this to initialize dataset (document, summary and the sanity questions)
# using data from DATASET_PATH, BE CAREFUL! All tables will be dropped! (Dump the schema first!)
# IS_INIT_DB=1
DATASET_PATH='/home/acp16hh/Projects/Research/Experiments/Exp_Elly_Human_Evaluation/src/harness/dataset/BBC'


