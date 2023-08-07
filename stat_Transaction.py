import zipfile

files_0 = ["0to99999_Transaction.zip"]
files_1 = ["100000to199999_Transaction.zip"]
files_2 = ["200000to299999_Transaction.zip"]
files_3 = ["300000to309999_Transaction.zip", "310000to319999_Transaction.zip", "320000to329999_Transaction.zip", "330000to339999_Transaction.zip", "340000to349999_Transaction.zip", "350000to359999_Transaction.zip", "360000to369999_Transaction.zip", "370000to379999_Transaction.zip", "380000to389999_Transaction.zip", "390000to399999_Transaction.zip"]
files_4 = ["400000to309999_Transaction.zip", "410000to319999_Transaction.zip", "420000to329999_Transaction.zip", "430000to339999_Transaction.zip", "440000to349999_Transaction.zip", "450000to359999_Transaction.zip", "460000to369999_Transaction.zip", "470000to379999_Transaction.zip", "480000to389999_Transaction.zip", "490000to399999_Transaction.zip"]
files_5 = ["500000to309999_Transaction.zip", "510000to319999_Transaction.zip", "520000to329999_Transaction.zip", "530000to339999_Transaction.zip", "540000to349999_Transaction.zip", "550000to359999_Transaction.zip", "560000to369999_Transaction.zip", "570000to379999_Transaction.zip", "580000to389999_Transaction.zip", "590000to399999_Transaction.zip"]
files_6 = ["600000to309999_Transaction.zip", "610000to319999_Transaction.zip", "620000to329999_Transaction.zip", "630000to339999_Transaction.zip", "640000to349999_Transaction.zip", "650000to359999_Transaction.zip", "660000to369999_Transaction.zip", "670000to379999_Transaction.zip", "680000to389999_Transaction.zip", "690000to399999_Transaction.zip"]
files_7 = ["700000to309999_Transaction.zip", "710000to319999_Transaction.zip", "720000to329999_Transaction.zip", "730000to339999_Transaction.zip", "740000to349999_Transaction.zip", "750000to359999_Transaction.zip", "760000to369999_Transaction.zip", "770000to379999_Transaction.zip", "780000to389999_Transaction.zip", "790000to399999_Transaction.zip"]

fileDir = "./"
files = files_0 + files_1 + files_2 + files_3 + files_4 + files_5 + files_6 + files_7

tx_count = 0

for file in files:
    print(file)
    theZIP = zipfile.ZipFile(fileDir+file+".zip", 'r')
    theCSV = theZIP.open(file+".csv")
    head = theCSV.readline()

    oneLine = theCSV.readline().decode("utf-8").strip()
    while (oneLine!=""):
        oneArray = oneLine.split(",")

        # Height,Timestamp,Txid,Size,Weight,SpentTxid:Vout[],InputAddrs:Value[],OutputAddrs:Value[]
        Height              = int(oneArray[0])
        Timestamp           = int(oneArray[1])
        Txid                = oneArray[2]
        Size                = int(oneArray[3])
        Weight              = int(oneArray[4])
        SpentTxidVout       = oneArray[5].split(";")
        InputAddrsValue     = oneArray[6].split(";")
        OutputAddrsValue    = oneArray[7].split(";")
        
        for item in SpentTxidVout:
            arr = item.split(":")
            SpentTxid = arr[0]
            Vout = arr[1]
        
        for item in InputAddrsValue:
            arr = item.split(":")
            InputAddrs = arr[0].split("-")
            Value = arr[1]
            
        for item in OutputAddrsValue:
            arr = item.split(":")
            OutputAddrs = arr[0].split("-")
            Value = arr[1]
        

        tx_count += 1

        if(tx_count%100000==0):
            print(Height, tx_count, flush=True)
        oneLine = theCSV.readline().decode("utf-8").strip()

    theCSV.close()
    theZIP.close()

print(tx_count)
# 0to779999:     812386973
# 780000to800000: 56574532