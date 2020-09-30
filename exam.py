def cp(hrs,rt):
    hrs = float(hrs)
    rt = float(rt)
    if(hrs>40):
        act_pay = (40*rt)
        ext_hr = (hrs - 40)
        ext_pay = (ext_hr*rt*1.5)
        final = (act_pay + ext_pay)
        print("Pay",final)
    else:
        orgpay = (hrs * rt)
        print("Pay",orgpay)
    
