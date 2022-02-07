
import pprint
from abc import ABCMeta, abstractmethod

import pandas as pd


# Delete only to beautiful print
pp = pprint.PrettyPrinter(indent=2)


class BaseReader(metaclass=ABCMeta):
    FLOATS = {"float16": 4, "float32": 8, "float64": 1024}
    INTS = {
        "int8": (-128, 127),
        "int16": (-32768, 32767),
        "int32": (-2147483648, 2147483647),
        "int64": (-9223372036854775808, 9223372036854775807)
    }
    UINTS = {
        "uint8": (0, 255),
        "uint16": (0, 65535),
        "uint32":  (0, 4294967295),
        "uint64":  (0, 18446744073709551615)
    }

    def __init__(self, id_):
        self.id_ = id_
        self.des_stats = None

    @abstractmethod
    def main(self):
        pass

    @abstractmethod
    def get_df(self):
        pass

    def get_descriptive_stats(self, df):
        des_stats = df.describe(include='all')

        self.des_stats = des_stats.to_dict()
        # pp.pprint(des_stats)
        # Sending to api rest

    def get_types_recommendations(self, df):
        recommendation = {}

        for index, value in df.dtypes.iteritems():
            data = self.des_stats[index]
            print(data)
            print(str(value))

            if str(value) == "float64":
                min_val = data['min']
                max_val = data['max']
                len_min = len(str(min_val).split('.')[1])
                len_max = len(str(max_val).split('.')[1])

                for k, v in self.FLOATS.items():
                    limit_min = len_min in range(v)
                    limit_max = len_max in range(v)

                    if limit_min is True and limit_max is True:
                        recommend_type = k
                        break
            elif str(value) == "int64":
                min_val = data['min']
                max_val = data['max']
                int_rec = [
                    k
                    for k, v in self.INTS.items()
                    if v[0] >= min_val and v[1] <= max_val
                ]
                uint_rec = [
                    k
                    for k, v in self.UINTS.items()
                    if v[0] >= min_val and v[1] <= max_val
                ]

                try:
                    int_rec = int_rec[0]
                except Exception:
                    int_rec = None

                try:
                    uint_rec = uint_rec[0]
                except Exception:
                    uint_rec = None

                if uint_rec is not None:
                    # @TODO: saved int type rec
            elif str(value) == "object":
                counts = data['count']
                unique = data['unique']

                count_uniq = int(counts / 3)

                if unique == 2:
                    recommend_type = 'bool'
                elif unique <= count_uniq:
                    recommend_type = 'category'
                else:
                    recommend_type = str(value)
            else:
                recommend_type = str(value)

            recommendation[index] = {
                "original": str(value),
                "recommendation": recommend_type
            }

        pp.pprint(recommendation)

    def get_inferential_stats(self):
        pass

    def get_correlation(self, df):
        correlations = ('pearson', 'kendall', 'spearman')
        corr_dict = {k: df.corr(method=k).to_dict() for k in correlations}

        # Sending to api rest


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

    def main(self):
        df = self.get_df()

        if df is None:
            raise Exception('FAILED dataframe read')

        # print(df)
        names = [
            ''.join([alpha for alpha in name if alpha.isalpha()])
            for name in df.columns
        ]
        df.columns = names
        self.get_descriptive_stats(df)
        self.get_types_recommendations(df)
        self.get_correlation(df)

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
    df_file = FileReader(1, 'loan_data_set.csv')
    df_file.main()

