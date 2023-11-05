import pandas as pd

def load_dataset_taylor(path):
    df_taylor = pd.read_csv(path+"/taylor_album_songs.csv")
    df_taylor_clean = df_taylor.drop(columns=['ep', 'lyrics', 'album_release', 'featuring', 'artist', 'bonus_track', 'promotional_release', 'single_release', 'track_release', 'explicit'])
    df_taylor_clean['is_folklore_or_evermore'] = [(alb== 'folklore' or alb == 'evermore') for alb in df_taylor_clean['album_name'].tolist()]
    df_taylor_clean = df_taylor_clean.drop(columns=['key_name', 'mode_name', 'key_mode', 'track_number', 'album_name'])
    df_taylor_clean = df_taylor_clean.dropna()
    return df_taylor_clean
