## 项目一：查找重复的电子邮箱（难度：简单）
- 编写一个 SQL 查询，查找 Email 表中所有重复的电子邮箱。   
根据以上输入，你的查询应返回以下结果：  
 +---------+ | Email   |
 +---------+ | a@b.com |
 +---------+   

```mysql
SELECT Email
FROM email
GROUP BY Email
HAVING COUNT(Email)>1;
```

## 项目二：查找大国（难度：简单）
- 如果一个国家的面积超过300万平方公里，或者(人口超过2500万并且gdp超过2000万)，那么这个国家就是大国家。
- 编写一个SQL查询，输出表中所有大国家的名称、人口和面积。 
根据上表，我们应该输出:
 +--------------+-------------+--------------+ | name         | population  | area         |
 +--------------+-------------+--------------+ | Afghanistan  | 25500100    | 652230       |
 +--------------+-------------+--------------+ | Algeria      | 37100000    | 2381741      |
```mysql
SELECT name, population, area
FROM world
WHERE area>3000000
OR (population>25000000 AND gdp>20000000);
```