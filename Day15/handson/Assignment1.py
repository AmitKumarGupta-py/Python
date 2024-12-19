import pandas as pd
data1={
'employee_names' : ["Alice", "Bob", "Charlie", "David"],
'employee_ids'  : [101, 102, 103, 104],
'salaries' : [60000, 75000, 50000, 90000]
}
data2 = {
'company_names' : ["TechCorp", "BizInc", "WebSolutions", "DevWorks"],
'salaries' : [60000, 75000, 50000, 90000]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

df3 = pd.merge(df1,df2,on= 'salaries')


print(df3)