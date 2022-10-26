def plotTAC():
    plt.plot(list(time_series_with_lag[0:60]), counts_with_lag[0:60], label='Liver')
    plt.plot(list(time_series_with_lag[0:60]),counts_with_lag_heart[0:60],label='Heart')

    plt.title('Time activity curve (cat)')
    plt.legend()
    plt.xlabel('Time (seconds)')
    plt.ylabel('Counts')
    plt.show()

    liver_counts=np.sum(counts_with_lag[lag:lag+14])
    heart_counts=np.sum(counts_with_lag_heart[lag:lag+14])
    shunt_index= heart_counts/(heart_counts+liver_counts)
    shunt_index = round(((shunt_index))*100,1)
    print ("Shunt index calculated from this curve is {} %.".format(shunt_index))
