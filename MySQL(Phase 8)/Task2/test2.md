# 二.表操作
```
1.MySQL表数据类型
2.用SQL语句创建表
    语句解释     设定列类型 、大小、约束     设定主键 3. 用SQL语句向表中添加数据
    语句解释     多种添加方式（指定列名；不指定列名） 4. 用SQL语句删除表
    语句解释     DELETE     DROP     TRUNCATE     不同方式的区别 5. 用SQL语句修改表
    修改列名     修改表中数据     删除行     删除列     新建列     新建行
```
## 项目三：超过5名学生的课（难度：简单）
- 创建如下所示的courses 表 ，有: student (学生) 和 class (课程)。 
表:

| student | class |  
| --- | --- |  
| A       | Math       |  
| B       | English    |  
| C       | Math       |  
| D       | Biology    |  
| E       | Math       |    
| F       | Computer   |  
| G       | Math       |   
| H       | Math       |  
| I       | Math       |  
| A       | Math       |  
```mysql
/*Create Table*/
CREATE TABLE courses 
( student VARCHAR(8) NOT NULL, class VARCHAR(255) );

/*INSERT Value*/
INSERT INTO courses VALUES('A','Math'); 
INSERT INTO courses VALUES('B','English'); 
INSERT INTO courses VALUES('C','Math');
INSERT INTO courses VALUES('D','Biology'); 
INSERT INTO courses VALUES('E','English'); 
INSERT INTO courses VALUES('F','Math');
INSERT INTO courses VALUES('G','Math'); 
INSERT INTO courses VALUES('H','English'); 
INSERT INTO courses VALUES('I','Math');
INSERT INTO courses VALUES('A','Math');
```


- 编写一个 SQL 查询，列出所有超过或等于5名学生的课。 应该输出:
```mysql
SELECT class
FROM courses
GROUP BY class
WHERE COUNT(DISTINCT class) >= 5;  --unique值
```

| class   |
| --- |
| Math    |

```mysql
/* To Do 3 */
SELECT class
FROM courses
GROUP BY class
HAVING COUNT(DISTINCT Email)>=5;
```

\* Note: 学生在每个课中不应被重复计算。

## 项目四：交换工资（难度：简单）
创建一个 salary 表，如下所示，有m=男性 和 f=女性的值 。 例如:
 
| id | name | sex | salary |  
|----|------|-----|--------|  
| 1  | A    | m   | 2500   |  
| 2  | B    | f   | 1500   |  
| 3  | C    | m   | 5500   |  
| 4  | D    | f   | 500    |  

```mysql
/*Create Table*/
CREATE TABLE salary ( 
id      INT         NOT NULL    PRIMARY KEY,
name    VARCHAR(8)  NULL,
sex     VARCHAR(8)  NOT NULL, 
salary  INT         NULL);

/*INSERT Value*/
INSERT INTO salary VALUES(1,'A','m',2500); 
INSERT INTO salary VALUES(2,'B','f',1500); 
INSERT INTO salary VALUES(3,'C','m',5500);
INSERT INTO salary VALUES(4,'D','f',500); 
```

交换所有的 f 和 m 值(例如，将所有 f 值更改为 m，反之亦然)。
要求使用一个更新查询，并且没有中间临时表。 
运行你所编写的查询语句之后，将会得到以下表: 

```mysql
UPDATE salary
SET sex = CASE
            WHEN sex = 'f' THEN 'm'
            ELSE 'f'
            END
```

| id | name | sex | salary | 
|----|------|-----|--------| 
| 1  | A    | f  | 2500   | 
| 2  | B    | m   | 1500   | 
| 3  | C    | f   | 5500   | 
| 4  | D    | m   | 500    |

```mysql
/* To Do 4*/
UPDATE  salary
SET     sex = CASE
                WHEN    sex = 'f' THEN 'm'
                ELSE    'f'
                END
```

## 项目五：有趣的电影 （难度：简单）
编写一个 SQL查询，找出所有影片描述为非 boring (不无聊) 的
并且 id 为奇数 的影片，结果请按等级 rating 排列。

例如，下表 cinema:

|   id    | movie     |  description |  rating   |  
| --- | --- | --- | --- |  
|   1     | War       |   great 3D   |   8.9     |   
|   2     | Science   |   fiction    |   8.5     | 
|   3     | irish     |   boring     |   6.2     | 
|   4     | Ice song  |   Fantacy    |   8.6     | 
|   5     | House card|   Interesting|   9.1     |

```mysql
/*Create Table*/
CREATE TABLE cinema ( 
id      INT NOT NULL, 
name    VARCHAR(32), 
description VARCHAR(64), rating DOUBLE );

/*INSERT Value*/
INSERT INTO cinema VALUES(1,'War','great 3D',8.9); 
INSERT INTO cinema VALUES(2,'Science','fiction',8.5); 
INSERT INTO cinema VALUES(3,'irish','boring',6.2);
INSERT INTO cinema VALUES(4,'Ice song','Fantacy',8.6); 
INSERT INTO cinema VALUES(5,'House card','Interesting',9.1); 
```

对于上面的例子，则正确的输出是为：

```mysql
SELECT *
FROM cinema
WHERE description != 'boring'
        AND MOD(id, 2) = 1    --奇数
ORDER BY rating DESC
```

|   id    | movie     |  description |  rating   |  
| --- | --- | --- | --- |
|   5     | House card|   Interesting|   9.1     |   
|   1     | War       |   great 3D   |   8.9     |  

```mysql
SELECT * FROM cinema 
WHERE description != 'boring' 
        AND MOD(id,2) = 1 
ORDER BY rating  DESC           --desc, 倒序
```


# 三.表联结
```
MySQL别名
INNER JOIN
LEFT JOIN
CROSS JOIN
自连接
UNION
以上几种方式的区别和联系
```
## 项目六：组合两张表 （难度：简单）

在数据库中创建表1和表2，并各插入三行数据（自己造） 
表1 Person   

| 列名 | 类型 |
| --- | --- |
| PersonId | int | 
| FirstName | varchar | 
| LastName | varchar | 

\* PersonId 是上表主键

表2: Address   

| 列名 | 类型 |
| --- | --- |
| AddressId | int | 
| PersonId | int | 
| City | varchar | 
| State | varchar | 

\*AddressId 是上表主键

编写一个 SQL 查询，满足条件：
无论 person 是否有地址信息，
都需要基于上述两表提供 person 的以下信息：
FirstName, LastName, City, State

```mysql
SELECT  Person.FirstName,
        Person.LastName,
        Address.City,
        Address.State
From Person
Left JOIN Address
ON Person.PersonID = Address.PersionID
```

## 项目七：删除重复的邮箱（难度：简单）
- 编写一个 SQL 查询，来删除 email 表中所有重复的电子邮箱，
重复的邮箱里只保留 **Id ***最小 *的那个。

| Id | Email | 
| --- | --- |
| 1 | a@b.com | 
| 2 | c@d.com | 
| 3 | a@b.com |

\* Id 是这个表的主键。 

-  Person表应返回以下几行: 

| Id | Email |
| --- | --- |
| 1 | a@b.com | 
| 2 | c@d.com |

```mysql
DELETE a.*
FROM email AS a JOIN email AS b       --表格别名
ON a.Email = b.Email                  --联结依据
AND a.ID > b.ID;
```

## 项目八：从不订购的客户 （难度：简单）
某网站包含两个表，Customers 表和 Orders 表。
编写一个 SQL 查询，找出所有从不订购任何东西的客户。

- Customers 表：

| Id | Name  |
| --- | --- |
| 1  | Joe   | 
| 2  | Henry | 
| 3  | Sam   | 
| 4  | Max   |

- Orders 表：

| Id | CustomerId | 
| --- | --- |
| 1  | 3          | 
| 2  | 1          | 

- 例如给定上述表格，你的查询应返回：

| Customers |
| --- |
| Henry     |
| Max       |

```mysql
SELECT Name AS Customers 
FROM Customers AS c LEFT JOIN Orders AS o 
ON c.Id = o.CustomerId  
WHERE o.Id IS NULL;

SELECT Name AS Customers 
FROM Customers 
WHERE Id NOT IN
            (SELECT CustomerId FROM Orders);
```

## 项目九：超过经理收入的员工（难度：简单）
Employee 表包含所有员工，他们的经理也属于员工。
每个员工都有一个 Id，此外还有一列对应员工的经理的 Id。

| Id | Name  | Salary | ManagerId |   
| --- | --- | --- | --- |
| 1  | Joe   | 70000  | 3         |   
| 2  | Henry | 80000  | 4         |   
| 3  | Sam   | 60000  | NULL      |   
| 4  | Max   | 90000  | NULL      |   

- 给定 Employee 表，编写一个 SQL 查询，
该查询可以获取收入超过他们经理的员工的姓名。
在上面的表格中，Joe 是唯一一个收入超过他的经理的员工:

| Employee |
| --- |
| Joe      |

```mysql
SELECT e.Name AS Employee 
FROM Employee AS e JOIN Employee AS m 
ON e.ManagerId = m.Id
WHERE e.Salary > m.Salary;
```









