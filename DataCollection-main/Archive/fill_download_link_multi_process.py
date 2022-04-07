from joblib import Parallel, delayed
import multiprocessing
import pandas as pd
import requests
import xmltodict


def fill_download_link(paper):
    if paper['pdf_link'] == '':
        title_formatted = paper['title'].replace(' ', '+')
        response = requests.get(
            f'http://export.arxiv.org/api/query?search_query=ti:{title_formatted}&start=0&max_results=1'
        )
        data = xmltodict.parse(response.text)['feed']
        if 'entry' in data:
            paper['pdf_link'] = data['entry']['link'][1]['@href']
        if paper['abstract'] == '' and 'entry' in data:
            paper['abstract'] = data['entry']['summary'].replace('\n', ' ')
    if paper['abstract'] == '':
        title_formatted = paper['title'].replace(' ', '+')
        response = requests.get(
            f'http://export.arxiv.org/api/query?search_query=ti:{title_formatted}&start=0&max_results=1'
        )
        data = xmltodict.parse(response.text)['feed']
        if 'entry' in data:
            paper['abstract'] = data['entry']['summary'].replace('\n', ' ')
    return paper


def temp_func(df):
    df = df.apply(fill_download_link, axis=1)
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
