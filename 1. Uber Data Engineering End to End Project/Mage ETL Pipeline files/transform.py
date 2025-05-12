@transformer
def transform(df, *args, **kwargs):
    import pandas as pd

    df['trip_id'] = df.index  # ✅ Add this line

    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

    datetime_dim = df[['trip_id','tpep_pickup_datetime','tpep_dropoff_datetime']].copy()
    datetime_dim['pick_hour'] = datetime_dim['tpep_pickup_datetime'].dt.hour
    datetime_dim['pick_day'] = datetime_dim['tpep_pickup_datetime'].dt.day
    datetime_dim['pick_month'] = datetime_dim['tpep_pickup_datetime'].dt.month
    datetime_dim['pick_year'] = datetime_dim['tpep_pickup_datetime'].dt.year
    datetime_dim['pick_weekday'] = datetime_dim['tpep_pickup_datetime'].dt.weekday

    datetime_dim['drop_hour'] = datetime_dim['tpep_dropoff_datetime'].dt.hour
    datetime_dim['drop_day'] = datetime_dim['tpep_dropoff_datetime'].dt.day
    datetime_dim['drop_month'] = datetime_dim['tpep_dropoff_datetime'].dt.month
    datetime_dim['drop_year'] = datetime_dim['tpep_dropoff_datetime'].dt.year
    datetime_dim['drop_weekday'] = datetime_dim['tpep_dropoff_datetime'].dt.weekday

    datetime_dim['datetime_id'] = datetime_dim['trip_id']
    datetime_dim = datetime_dim[['datetime_id', 'tpep_pickup_datetime', 'pick_hour', 'pick_day', 'pick_month', 'pick_year', 'pick_weekday',
                                 'tpep_dropoff_datetime', 'drop_hour', 'drop_day', 'drop_month', 'drop_year', 'drop_weekday']]

    passenger_count_dim = df[['trip_id', 'passenger_count']].copy()
    passenger_count_dim = passenger_count_dim.rename(columns={'trip_id': 'passenger_count_id'})

    trip_distance_dim = df[['trip_id', 'trip_distance']].copy()
    trip_distance_dim = trip_distance_dim.rename(columns={'trip_id': 'trip_distance_id'})

    rate_code_type = {
        1:"Standard rate",
        2:"JFK",
        3:"Newark",
        4:"Nassau or Westchester",
        5:"Negotiated fare",
        6:"Group ride"
    }

    rate_code_dim = df[['trip_id', 'RatecodeID']].copy()
    rate_code_dim['rate_code_name'] = rate_code_dim['RatecodeID'].map(rate_code_type)
    rate_code_dim = rate_code_dim.rename(columns={'trip_id': 'rate_code_id'})

    pickup_location_dim = df[['trip_id', 'pickup_longitude', 'pickup_latitude']].copy()
    pickup_location_dim = pickup_location_dim.rename(columns={'trip_id': 'pickup_location_id'})

    dropoff_location_dim = df[['trip_id', 'dropoff_longitude', 'dropoff_latitude']].copy()
    dropoff_location_dim = dropoff_location_dim.rename(columns={'trip_id': 'dropoff_location_id'})

    payment_type_name = {
        1:"Credit card",
        2:"Cash",
        3:"No charge",
        4:"Dispute",
        5:"Unknown",
        6:"Voided trip"
    }

    payment_type_dim = df[['trip_id', 'payment_type']].copy()
    payment_type_dim['payment_type_name'] = payment_type_dim['payment_type'].map(payment_type_name)
    payment_type_dim = payment_type_dim.rename(columns={'trip_id': 'payment_type_id'})

    fact_table = df.merge(passenger_count_dim, left_on='trip_id', right_on='passenger_count_id') \
                   .merge(trip_distance_dim, left_on='trip_id', right_on='trip_distance_id') \
                   .merge(rate_code_dim, left_on='trip_id', right_on='rate_code_id') \
                   .merge(pickup_location_dim, left_on='trip_id', right_on='pickup_location_id') \
                   .merge(dropoff_location_dim, left_on='trip_id', right_on='dropoff_location_id') \
                   .merge(datetime_dim, left_on='trip_id', right_on='datetime_id') \
                   .merge(payment_type_dim, left_on='trip_id', right_on='payment_type_id') \
                   [['trip_id','VendorID', 'datetime_id', 'passenger_count_id',
                     'trip_distance_id', 'rate_code_id', 'store_and_fwd_flag', 'pickup_location_id', 'dropoff_location_id',
                     'payment_type_id', 'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount',
                     'improvement_surcharge', 'total_amount']]

    # Save each dimension and fact table as CSV (to mage's default 'data_export' folder)
    # import os

    # EXPORT_DIR = os.path.join(os.getcwd(), 'data_export')
    # os.makedirs(EXPORT_DIR, exist_ok=True)

    # datetime_dim.to_csv(os.path.join(EXPORT_DIR, 'datetime_dim.csv'), index=False)
    # passenger_count_dim.to_csv(os.path.join(EXPORT_DIR, 'passenger_count_dim.csv'), index=False)
    # trip_distance_dim.to_csv(os.path.join(EXPORT_DIR, 'trip_distance_dim.csv'), index=False)
    # rate_code_dim.to_csv(os.path.join(EXPORT_DIR, 'rate_code_dim.csv'), index=False)
    # pickup_location_dim.to_csv(os.path.join(EXPORT_DIR, 'pickup_location_dim.csv'), index=False)
    # dropoff_location_dim.to_csv(os.path.join(EXPORT_DIR, 'dropoff_location_dim.csv'), index=False)
    # payment_type_dim.to_csv(os.path.join(EXPORT_DIR, 'payment_type_dim.csv'), index=False)
    # fact_table.to_csv(os.path.join(EXPORT_DIR, 'fact_table.csv'), index=False)


    Limit = 100

    return {"datetime_dim":datetime_dim.head(Limit).to_dict(orient="dict"),
    "passenger_count_dim":passenger_count_dim.head(Limit).to_dict(orient="dict"),
    "trip_distance_dim":trip_distance_dim.head(Limit).to_dict(orient="dict"),
    "rate_code_dim":rate_code_dim.head(Limit).to_dict(orient="dict"),
    "pickup_location_dim":pickup_location_dim.head(Limit).to_dict(orient="dict"),
    "dropoff_location_dim":dropoff_location_dim.head(Limit).to_dict(orient="dict"),
    "payment_type_dim":payment_type_dim.head(Limit).to_dict(orient="dict"),
    "fact_table":fact_table.head(Limit).to_dict(orient="dict")}

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
