import pandas as pd
import requests
from io import StringIO

def main():
    url = 'https://docs.google.com/spreadsheets/d/1chkvChMO_c_oeWhb9SipwtBIomF-Gdt3ymHzQy6yRp8/gviz/tq?tqx=out:csv&gid=0'
    r = requests.get(url).text
    df = pd.read_csv(StringIO(r))
    df.to_csv('apuntes/data.csv', index=False)

if __name__ == "__main__":
    main()