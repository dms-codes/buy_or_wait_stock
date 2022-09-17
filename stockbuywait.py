import ihsg
import moving_average as ma
import descriptive as ds
 
def proc():
    import time
    interval_minutes = 5
    while True:
        res = []
        ticker = ihsg.get_ticker("IHSG")
        df_daily = ihsg.get_dataframe(ticker,"max","1d")
        df_intra = ihsg.get_dataframe(ticker,"day","1m")
        ma21 = ds.get_MA(df_daily['Close'],21)[-1]
        last_price = df_intra['Close'][-1]
        ma21 = 3
        last_price = 2
        if last_price > ma21:
            if len(res):
                if res[0] == "BUY":
                    pass
                elif res[0] == "WAIT":
                    res[0]="BUY"
                    print("{} - {:.2f} > {:.2f}".format(res[0],last_price,ma21))
            else:
                res.append("BUY")
                print("{} - {:.2f} > {:.2f}".format(res[0],last_price,ma21))
        else:
            if len(res):
                if res[0] == "WAIT":
                    pass
                elif res[0] == "BUY":
                    res[0]="WAIT"
                    print("{} - {:.2f} < {:.2f}".format(res[0],last_price,ma21))
            else:
                res.append("WAIT")
                print("{} - {:.2f} < {:.2f}".format(res[0],last_price,ma21))
        time.sleep(interval_minutes*60)
