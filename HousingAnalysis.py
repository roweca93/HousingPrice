
import pandas as pd
with open('C:/Users/Chris/Desktop/test.txt', encoding="utf-8") as f:
    df = pd.read_csv(f)
    pd.set_option('display.max_columns', None, "display.precision", 10)
    df.columns = df.columns.str.replace(' ','')
    df.columns = df.columns.str.replace("'",'')
    df.columns = df.columns.str.replace("[", '')
    df.columns = df.columns.str.replace("]", '')
    df = df.drop(['Address', 'County', 'Pool'], axis=1)

    covariance_matrix = {}
    num_cols = len(df.keys())
    col_names = list(df.keys())

    for i in range(0, num_cols):
        cov_list = []
        corr_list = []
        for j in range(0, num_cols):
            print(df[col_names[i]].count(), col_names[i], df[col_names[j]].count(), col_names[j],'here')
            t1 = df[col_names[i]].dropna()
            n1 =t1.count()
            t2 = df[col_names[j]].dropna()
            n2 = t2.count()
            if (n1 <= n2):
                t1 = t1[0:n1]
                t2 = t2[0:n1]
            else:
                t1 = t1[0:n2]
                t2 = t2[0:n2]
            covariance = t1.cov(t2)
            cov_list.append(covariance)
            correlation = t1.corr(t2)
            corr_list.append(correlation)
        print(col_names[i], cov_list)
        print(col_names[i], corr_list)


