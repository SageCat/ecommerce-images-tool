import pandas as pd
import globals


def transpose(product_cat, single_pro_photo_count, csv_file):
    df = pd.read_csv(csv_file, encoding='utf-8')
    df = df[df['ProductCategory'] == product_cat]
    new_data = [df['Link'][i:i + single_pro_photo_count].values for i in
                range(0, len(df['Link']), single_pro_photo_count)]

    columns = []
    for i in range(single_pro_photo_count):
        columns.append('Image URL ' + str(i+1))
    print('========= Data Transpose Finished! ==========')
    return pd.DataFrame(new_data, columns=columns)
