
import pandas as pd

from master_reader import BaseReader


class FileReader(BaseReader):
    def __init__(self, id_, path, separator=None):
        super().__init__(id)
        self.path = path
        self.readers = (
            pd.read_csv, pd.read_excel, pd.read_parquet, pd.read_json,
            pd.read_xml
        )
        self.separators = (separator,) if separator is None \
            else (',', ';', ':', '|')

    def get_df(self):
        for i, reader in enumerate(self.readers):
            if i == 0:
                for sep in self.separators:
                    try:
                        df = reader(self.path, sep=sep)

                        return df
                    except Exception as e:
                        print(e)
            else:
                try:
                    df = reader(self.path)

                    return df
                except Exception as e:
                    print(e)


if __name__ == '__main__':
    filer = FileReader(1, 'iris.csv')
    filer.main()
