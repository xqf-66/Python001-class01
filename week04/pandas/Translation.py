# _*_ coding : UTF-8 _*_
# 开发人员：xieqiaofa
# 开发时间：2020年6月28日
# 项目需求：请将以下的 SQL 语句翻译成 pandas 语句：


import pandas as pd
import numpy as np

data = pd.read_csv('data.csv')
table1 = pd.read_csv('table1.csv')
table2 = pd.read_csv('table2.csv')

# 1. SELECT * FROM data;
#
print(data)

# 2. SELECT * FROM data LIMIT 10;
#
print(data.head(10))

# 3. SELECT id FROM data;  //id 是 data 表的特定一列
#
print(data[['id']])
# 4. SELECT COUNT(id) FROM data;
#
print(data[['id']].count)

# 5. SELECT * FROM data WHERE id<1000 AND age>30;
#
print(data[(data['id'] > 1000) & (data['age'] < 30)])

# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
#
print(table1.groupby('user_id').aggregate({'id': 'count', }))

# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
#
print(data.merge(table1, left_on='id', right_on='user_id'))

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
#
print(pd.concat([table1, table2]))

# 9. DELETE FROM table1 WHERE id=10;
#
print(data.loc[data['id'] != 10])

# 10. ALTER TABLE table1 DROP COLUMN column_name;
print(data.rename(columns={'gender': 'sex'}, inplace=True))