import csv

csvFile = open("/data/python/link_configs.py.csv", "w")  #创建csv文件
writer = csv.writer(csvFile) #创建写的对象
#先写入columns_name
writer.writerow(["index","a_name","b_name"]) #写入列的名称
#写入多行用writerows
writer.writerow([[1,"a","b"],[2,"c","d"],[3,"d","e"]])
writer.writerow([[4,"a","b"],[5,"c","d"],[6,"d","e"]])
csvFile.close() #关闭IO资源
