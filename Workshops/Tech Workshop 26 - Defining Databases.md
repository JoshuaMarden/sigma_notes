___

[Excalidraw](https://link.excalidraw.com/l/6gPaBlSh8PG/14QCkCxDboZ) Doc
### Prework:

##### ACID in Database Context:
- **Atomicity**: All parts of a transaction are completed or none are.
- **Consistency**: Transactions bring the database from one valid state to another.
- **Isolation**: Transactions do not interfere with each other.
- **Durability**: Once a transaction is committed, it remains so, even in the event of a crash.

##### DML vs. DDL SQL:

- **DML (Data Manipulation Language)**: Used for managing data within schema objects.
    - Examples: `SELECT`, `INSERT`, `UPDATE`, `DELETE`
- **DDL (Data Definition Language)**: Used for defining and modifying database schema.
    - Examples: `CREATE`, `ALTER`, `DROP`, `TRUNCATE`

(The schema being the sort of 'workspace' or virtual desk, and the data within being what we generally call 'tables' (though many other data types are possible))

##### Postgres Options for Storing Text Values:

- **TEXT**: Variable-length text.
- **VARCHAR(n)**: Variable-length text with a limit.
- **CHAR(n)**: Fixed-length text.

##### Constraint in SQL:

A **constraint** is a rule applied to data in a table to enforce data integrity.
- Examples: `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `NOT NULL`, `CHECK`


____

We basically recap building SQL tables with constraints, idempotency, and efficiency.

We also spoke about using EXPLAIN to measure database response times.

__Search using id's__! They can be indexed so you need not use a sequential search! This is key for performance.

You can set a column to be an index. It hashes the columns so they can be searched via tree not sequential scan.

Indexes make __querys__ faster _but_ __adding and removing__ is slower. It is ideal to index data that does not often need updating and is regularly searched.


![[Screenshot 2024-06-25 at 10.22.22.png]]

![[Pasted image 20240625102457.png]]




