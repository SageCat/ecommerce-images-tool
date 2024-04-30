import pandas as pd


def transpose(product_cat, single_pro_photo_count, csv_file):
    df = pd.read_csv(csv_file)
    df = df[df['Product Category'] == product_cat]
    new_data = [df['Link'][i:i + single_pro_photo_count].values for i in
                range(0, len(df['Link']), single_pro_photo_count)]

    columns = []
    for i in range(single_pro_photo_count):
        columns.append('Image URL ' + str(i+1))

    return pd.DataFrame(new_data, columns=columns)


product_category = 'Phone Case'
single_product_photo_count = 4
csv_filename = 'share_links.csv'
converted_data = transpose(product_category, single_product_photo_count, csv_filename)
converted_data.to_excel(f'NIS {product_category} Photos URL.xlsx', index=False)
