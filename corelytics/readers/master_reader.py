
from abc import ABCMeta, abstractmethod

import pandas as pd


class BaseReader(metaclass=ABCMeta):
    @abstractmethod
    def main(self):
        pass

    @abstractmethod
    def get_df(self):
        pass

    def get_descriptive_stats(self):
        des_stats = self.df.describe(include='all')

        return des_stats

    def get_types_recommendations(self):
        print(self.df.dtypes)

    def get_inferential_stats(self):
        pass

    def get_correlation(self):
        correlations = ('pearson', 'kendall', 'spearman')
        corr_dict = {k: self.df.corr(method=k) for k in correlations}

        return corr_dict


class FileReader(BaseReader):
    def __init__(self, path, separator=None):
        self.path = path
        self.readers = (
            pd.read_csv, pd.read_excel, pd.read_parquet, pd.read_json,
            pd.read_xml
        )
        self.df = None
        self.separators = (separator,) if separator is None \
            else (',', ';', ':', '|')

    def main(self):
        self.get_df()

        if self.df is None:
            raise Exception('FAILED dataframe read')

        print(self.df)
        des_stats = self.get_descriptive_stats()
        print(des_stats)
        self.get_types_recommendations()
        corrs = self.get_correlation()
        print(corrs)

    def get_df(self):
        for i, reader in enumerate(self.readers):
            if i == 0:
                for sep in self.separators:
                    try:
                        self.df = reader(self.path, sep=sep)

                        return
                    except Exception as e:
                        print(e)
            else:
                try:
                    self.df = reader(self.path)

                    return
                except Exception as e:
                    print(e)


if __name__ == '__main__':
    df_file = FileReader('iris.csv')
    df_file.main()

