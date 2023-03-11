def calculating_averages(df):
    media = []
    for _,row in df.iterrows():
        indiv_media = (row['G1'] + row['G2'] + row['G3'])/3
        media.append(round(indiv_media, 2))
    
    df['media'] = media
    return df

def list_students(df):
    result = df.sort_values(by=['Name'])
    return result