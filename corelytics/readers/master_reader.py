
import pprint
from abc import ABCMeta, abstractmethod

import pandas as pd


# @TODO: Delete only to beautiful print
pp = pprint.PrettyPrinter(indent=2)
# @TODO: adding requests and logging to file and console


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

    def main(self):
        df = self.get_df()

        if df is None:
            raise Exception('FAILED dataframe read')

        names = [
            ''.join([alpha for alpha in name if alpha.isalpha()])
            for name in df.columns
        ]
        df.columns = names
        self.get_descriptive_stats(df)
        self.get_types_recommendations(df)
        self.get_correlation(df)

    @abstractmethod
    def get_df(self):
        pass

    def get_descriptive_stats(self, df):
        des_stats = df.describe(include='all')

        self.des_stats = des_stats.to_dict()

    def get_types_recommendations(self, df):
        # @TODO: this function is necesary the refactor
        # in each type
        recommendation = {}

        for index, value in df.dtypes.iteritems():
            data = self.des_stats[index]

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
                unique_values = df[index].value_counts()
                size = data['count'] / 3
                int_rec = [
                    k
                    for k, v in self.INTS.items()
                    if min_val >= v[0] and max_val <= v[1]
                ]
                uint_rec = [
                    k
                    for k, v in self.UINTS.items()
                    if min_val >= v[0] and max_val <= v[1]
                ]

                if unique_values.shape[0] <= size:
                    recommend_type = 'category'
                elif uint_rec:
                    recommend_type = uint_rec[0]
                elif int_rec:
                    recommend_type = int_rec[0]
                else:
                    recommend_type = str(value)
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

