def shuntFraction(PSS):
    #increment = 10
    time_series= range(1,61,1)
    counts=np.cumsum(list(time_series))
    K=200
    counts=(x*K for x in counts)


    #Alterd time series is used to generate some counts for the heart
    #(not actually used as time in the time activity plot).
    #Because the kactor "K" is less than one, counts in heart will be
    #less than counts in liver.
    K=0.9
    altered_time_series = [x * K for x in (list(time_series))]
    counts_heart=np.cumsum(list(altered_time_series))


    #add noise to counts for liver
    noisy_counts=[]
    for item in counts:
        r = random.randint(-5,5)
        n=(item+(r*item)/100)
        noisy_counts.append(n)

        #add noise to counts for heart
    noisy_counts_heart=[]
    for item in counts_heart:
        r = random.randint(-10,10)
        n=(item+(r*item)/100)
        noisy_counts_heart.append(n)


    # Variable to indicate time between
    global lag
    lag=random.randint(15, 25)
    lag_heart=lag+PSS

    #choosing 20 here as an arbitary max backgrounnd
    randomlist = []
    for i in range(1,lag):
        n = random.randint(1,20)
        randomlist.append(n)
    counts_in_lag=randomlist


    #choosing 20 here as an arbitary max backgrounnd
    randomlist = []
    for i in range(1,lag_heart):
        n = random.randint(1,20)
        randomlist.append(n)
    counts_in_lag_heart=randomlist

    global time_series_with_lag
    time_series_with_lag=[x + lag-1 for x in list(time_series)]
    time_series_with_lag=list(range(1,lag,1))+time_series_with_lag
    global counts_with_lag
    counts_with_lag=list(counts_in_lag) + list(noisy_counts)
    global counts_with_lag_heart
    counts_with_lag_heart=list(counts_in_lag_heart) + list(noisy_counts_heart)

