import pandas as pd
orders_df = pd.read_csv("Amazon Sale Report.csv",low_memory=False)

orders = pd.DataFrame(
    {
         "order_id":orders_df["Order ID"],
         "index1":orders_df["index"],
         "Date":orders_df["Date"],
         "status":orders_df["Status"],
         "fulfilment":orders_df["Fulfilment"],
         "sales_channel":orders_df["Sales Channel "],
         "ship_service_level":orders_df["ship-service-level"],
         "style":orders_df["Style"],
         "promotion_ids":orders_df["promotion-ids"],
         "b2b":orders_df["B2B"],
         "fulfilled_by":orders_df["fulfilled-by"]
    }
)

orders.to_csv("orders.csv", index=False)
print(orders_df )

products_df = pd.read_csv("Amazon Sale Report.csv",low_memory=False)
products = pd.DataFrame(
    {
       "order_id":products_df["Order ID"],
        "sku":products_df["sku"],
        "size":products_df["Size"],
        "asin":products_df["ASIN"],
        "style":products_df["Style"],
        "category":products_df["Category"],
    }

)

products.to_csv("products_df.csv", index=False)
print(products_df )



shipping_df = pd.read_csv("Amazon Sale Report.csv",low_memory=False)
shipping  = pd.DataFrame(
    {
       "order_id":shipping_df["Order ID"],
       "ship_city":shipping_df["ship-city"],
       "ship_state":shipping_df["ship-state"],
       "ship_postal_code":shipping_df["ship-postal-code"],
       "ship_country":shipping_df["ship-country"],
       "courier_status":shipping_df["Courier Status"]
    }

).dropna().drop_duplicates().reset_index(drop=True)

shipping.to_csv("shipping.csv", index=False)
print(shipping)


payments_df = pd.read_csv("Amazon Sale Report.csv",low_memory=False)
payments = pd.DataFrame(
    {
       "order_id":payments_df["Order ID"],
       "qty":payments_df["Qty"],
        "currency":payments_df["currency"],
        "amount":payments_df["Amount"]

   }
)


payments.to_csv("payments.csv", index=False)
print(payments)


promotions_df = pd.read_csv("Amazon Sale Report.csv",low_memory=False)

promotions = pd.DataFrame(
    {
        "order_id":promotions_df["Order ID"],
        "sales_channel":promotions_df["Sales Channel "],
        "promotion_ids":promotions_df["promotion-ids"]
    }
)

promotions.to_csv("promotions.csv",index=False)
print(promotions)
