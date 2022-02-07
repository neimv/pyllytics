
import pandas as pd
import requests as req

from master_reader import BaseReader


class WSReader(BaseReader):
    def __init__(self, id_, url, status_code):
        super().__init__(id)
        self.url = url
        self.status_code = status_code

    def get_df(self):
        data_ws = req.get(self.url)

        if data_ws.status_code == self.status_code:
            try:
                body = data_ws.json()
                df = pd.DataFrame(body)
            except Exception:
                df = None
        else:
            df = None

        return df


if __name__ == '__main__':
    # @NOTE: the varibale status_code is if the response is <> 200
    filer = WSReader(
        1, 'http://localhost:5000/iris.csv.tar.gz', 200
    )
    filer.main()
