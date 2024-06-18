___


### 1st Normal Form (1NF)

**Goal**: Eliminate duplicate data by ensuring each column contains only atomic (indivisible) values.

**Explanation**:

- Each column in a table should contain only one value (no lists or sets).
- Each row should be unique.
- There should be no repeating groups of columns.

**Example**: Suppose you have a table storing customer orders:

| OrderID | CustomerName | Items           |
|---------|--------------|-----------------|
| 1       | John Doe     | Apple, Banana   |
| 2       | Jane Smith   | Orange, Apple   |

In 1NF, you would split the `Items` column so each item is in its own row:

| OrderID | CustomerName | Item    |
|---------|--------------|---------|
| 1       | John Doe     | Apple   |
| 1       | John Doe     | Banana  |
| 2       | Jane Smith   | Orange  |
| 2       | Jane Smith   | Apple   |

### 2nd Normal Form (2NF)

**Goal**: Eliminate redundant data by ensuring all non-key columns are fully dependent on the primary key.

**Explanation**:

- The table must already be in 1NF.
- All non-key columns should depend on the whole primary key. There should not be a partial relationship between the primary key and the non-key columns.

**Example**: Consider a table storing order details with a composite key (OrderID, Item):

| OrderID | Item    | CustomerName | CustomerAddress    |
|---------|---------|--------------|--------------------|
| 1       | Apple   | John Doe     | 123 Main St        |
| 1       | Banana  | John Doe     | 123 Main St        |
| 2       | Orange  | Jane Smith   | 456 Oak St         |
| 2       | Apple   | Jane Smith   | 456 Oak St         |

In 2NF, you separate data into two tables to remove partial dependencies:

- Orders table:

| OrderID | CustomerName | CustomerAddress    |
|---------|--------------|--------------------|
| 1       | John Doe     | 123 Main St        |
| 2       | Jane Smith   | 456 Oak St         |

- OrderItems table:

| OrderID | Item    |
|---------|---------|
| 1       | Apple   |
| 1       | Banana  |
| 2       | Orange  |
| 2       | Apple   |


### 3rd Normal Form (3NF)

**Goal**: Eliminate transitive dependencies by ensuring non-key columns depend only on the primary key.

**Explanation**:

- The table must already be in 2NF.
- No non-key column should depend on another non-key column.

**Example**: Consider the Orders table from 2NF:

| OrderID | CustomerName | CustomerAddress    |
|---------|--------------|--------------------|
| 1       | John Doe     | 123 Main St        |
| 2       | Jane Smith   | 456 Oak St         |

If `CustomerAddress` depends on `CustomerName`, you would split this into two tables in 3NF:

- Orders table:

| OrderID | CustomerName |
|---------|--------------|
| 1       | John Doe     |
| 2       | Jane Smith   |

- Customers table:

| CustomerName | CustomerAddress    |
|--------------|--------------------|
| John Doe     | 123 Main St        |
| Jane Smith   | 456 Oak St         |


This way, `CustomerAddress` depends directly on `CustomerName`, which is a unique identifier.

### Summary

1. **1NF**: Make sure each column contains only atomic values and each row is unique.
2. **2NF**: Ensure all non-key columns depend on the whole primary key.
3. **3NF**: Remove transitive dependencies so that non-key columns depend only on the primary key.