
import pandas as pd
from sqlalchemy import create_engine

from .master_reader import BaseReader


class SQLReader(BaseReader):
    def __init__(
        self, id_, user, password, db, host, port, driver, resource,
        type_read='query'
    ):
        super().__init__(id)
        self.user = user
        self.password = password
        self.db = db
        self.host = host
        self.port = port
        self.driver = driver
        self.type_read = type_read
        self.resource = resource

    def get_df(self):
        engine = self._create_engine()
        # I know that exists pd.read_sql but I'm playing
        reader = {
            'query': pd.read_sql_query,
            'table': pd.read_sql_table
        }

        df = reader[self.type_read](self.resource, engine)

        return df

    def _create_engine(self):
        string_conn_dict = {
            "mysql": "mysql+pymysql://",
            "postgres": "postgresql://",
            "maria": "mysql+pymysql://"
        }
        string_conn = (
            f"{string_conn_dict[self.driver]}{self.user}:{self.password}@"
            f"{self.host}:{self.port}/{self.db}"
        )
        engine = create_engine(string_conn)

        return engine


if __name__ == '__main__':
    # @NOTE: with mysql use `` and with postgres use "" in tables
    filer = SQLReader(
        1, 'neimv', 'prueba_neimv', 'neimv', 'localhost', 5432, 'postgres',
        'SELECT * FROM "dataframe_iris.csv.tar.gz"'
    )
    filer.main()
