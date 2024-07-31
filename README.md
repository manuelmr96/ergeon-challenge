# ergeon-challenge

## Taks 1

Describe in your own words what is GIL in python, and the pros and cons of it.

```
The Global Interpreter Lock is in charge of limiting the amount of threats working and orchestrating them.
```

## Task 2

Write a decorator in python that will count how many times the decorated function was called. It should print the number every time the decorated function is executed. Each function should be counted separately.
[Decorator](./Task-2/decorator.py)

## Task 3

If you see that a SQL SELECT query is slow - what would you do to improve it?

1. Analyze the Query:
   - Understand the Query: Ensure you understand what the query is supposed to do and the data it is working with.
2. Indexing:
   - Add Indexes: Ensure that the columns used in WHERE, JOIN, ORDER BY, and GROUP BY clauses are indexed.
   - Composite Indexes: Create composite indexes for columns that are frequently used together in queries.
   - Index Maintenance: Ensure indexes are not fragmented and are up-to-date.
3. Query Optimization:
   - Simplify the Query: Break complex queries into simpler subqueries or use common table expressions (CTEs).
   - **Avoid SELECT \***: Select only the columns you need instead of using SELECT \*.
   - Use Appropriate Joins: Ensure you're using the most efficient join type (e.g., INNER JOIN vs. LEFT JOIN).
   - Filter Early: Apply filters as early as possible in the query to reduce the number of rows processed.
4. Database Design:
   - Normalize or Denormalize: Depending on the use case, consider normalizing or denormalizing the database schema.
   - Partitioning: Partition large tables to improve performance.
   - Proper Data Types: Use appropriate data types for columns to optimize storage and performance.
5. Caching and Materialized Views:
   - Caching: Use caching mechanisms to store the results of expensive queries.
   - Materialized Views: Use materialized views for complex queries that don't need real-time data.
6. Hardware and Configuration:
   - Upgrade Hardware: Ensure the database server has adequate CPU, memory, and disk I/O capacity.
   - Database Configuration: Tune database configuration parameters (e.g., buffer pool size, cache size) to optimize performance.
7. Monitor and Profile:
   - Performance Monitoring: Use performance monitoring tools to track query performance over time.
   - Profile Queries: Use profiling tools to identify slow queries and understand their execution characteristics.

## Task 4

What are the differences between “arrow” and “traditional” functions in javascript?

1. Syntax: Arrow functions have a more concise syntax.
2. `this` Binding: Arrow functions lexically bind this, whereas traditional functions dynamically bind this based on the call site.
3. Arguments Object: Arrow functions do not have their own arguments object.
4. Constructor: Arrow functions cannot be used as constructors.
5. Implied Return: Arrow functions can implicitly return single expressions without braces.

## Task 5

Write a basic React component showing number of clicks on it’s button, use images below as example, allow to configure initial value of click count.
[Click Counter](./Task-5/ClickCounter.jsx)

## Task 6

Task 6
Let’s say we have the following models in Django project:

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

[Django](./Task-6/Django.py)

- Assume we have ~100 books and ~25 authors in our database.
- Try to write efficient queries, keep in mind how many requests the ORM can make to the database.

  6.1 Using Django ORM, write a function that will print the book title and the author name (who wrote it) for all the books we have in the database. Like this:

  ```
  “War and Peace”. Leo Tolstoy
  “Anna Karenina”. Leo Tolstoy
  “Resurrection”. Leo Tolstoy
  “The Three Musketeers”. Alexandre Dumas
  “The Count of Monte Cristo”. Alexandre Dumas
  ```

  6.2 Write another function that will print the author’s name and all the books he wrote. For all the authors we have in the database. Like this:

  ```
    Leo Tolstoy: “War and Peace”, “Anna Karenina”, “Resurrection”
    Alexandre Dumas: “The Three Musketeers”, “The Count of Monte Cristo”
  ```

  6.3 Implement the third function, it should print the author’s name and the number of books he wrote. Order by the number of books written, descending. Like this:

  ```
  Leo Tolstoy: 3
  Alexandre Dumas: 2
  ```
