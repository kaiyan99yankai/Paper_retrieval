from joblib import Parallel, delayed
import multiprocessing
import pandas as pd
import requests


def fill_info(paper):
    if paper['abstract'] == '':
        title_formatted = paper['title'].replace(' ', '+')
        data = requests.get(
            f'https://api.semanticscholar.org/graph/v1/paper/search?query={title_formatted}&limit=1&fields=abstract,referenceCount,citationCount,influentialCitationCount'
        ).json()
        if data.get('message') is not None:
            return paper
        if data:
            data = data.get('data')[0]
            paper['abstract'] = data.get('abstract')
            paper['citationCount'] = data.get('citationCount')
            paper['referenceCount'] = data.get('referenceCount')
            paper['influentialCitationCount'] = data.get(
                'influentialCitationCount')
    return paper


def temp_func(df):
    df = df.apply(fill_info, axis=1)
    return df


def apply_parallel(dfs, func, n_jobs=None):
    if n_jobs is None:
        n_jobs = multiprocessing.cpu_count()
    results = Parallel(n_jobs=n_jobs)(delayed(func)(df)
                                      for _, df in dfs.groupby('area'))
    return pd.concat(results)


if __name__ == '__main__':
    total_df = pd.read_csv('./data/total_results.csv')
    total_df['pdf_link'].fillna('', inplace=True)
    total_df['abstract'].fillna('', inplace=True)
    df_all = apply_parallel(total_df, temp_func, n_jobs=None)
    df_all.to_csv('./data/total_results_with_info.csv', index=False)
