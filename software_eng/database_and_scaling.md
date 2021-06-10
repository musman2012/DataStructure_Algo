## Database Scaling 

### Database Sharding
Row wise partitioning the database tables into multiple instances to improve the query speed. Ths partitioning can be based on Zipcode, geolocation or using some consistent hashing.
In contrast to this, Horizontal Partitioning partitions the data in the same database.

**Pros:** Scale (Memory, Data), Security (User access control), Optimal and Small Index

**Cons:** Complex Client, Transactions across shards, Roll backs, Schema changes, Joins

## SQL vs NoSQL

SQL databases are used to manage data in relational databases. Relational databases use relations (typically called tables) to store data and then match that data by using common characteristics within the dataset. On the other hand, NoSQL does not require a schema. Nor does it enforce relations between tables in all cases. All its documents are JSON documents, which are complete entities that one can readily read and understand.

SQL databases are table-based which makes them a better option for applications that require multi-row transactions. 

SQL databases are vertically scalable. This means that the load on a single server can be increased by increasing things like RAM, CPU, or SSD. (More floors can be added to this building). On the other hand, NoSQL databases are horizontally scalable. This means that more traffic can be handled by sharding, or adding more servers in your NoSQL database. (More buildings can be added to the neighborhood).

In the long run, it is better to add more buildings than floors as that is more stable (Less chance of creating a Leaning Tower of Pisa!!!). Thus, NoSQL can ultimately become larger and more powerful, making NoSQL databases the preferred choice for large or ever-changing data sets.

### Usage

SQL is a good choice for:

- Any organization that will benefit from a predefined structure and set schemas, particularly if they require multi-row transactions.
- Situations when all data must be consistent without leaving room for error, such as with accounting systems.

NoSQL is a good choice for those companies experiencing rapid growth with no clear schema definitions. NoSQL offers much more flexibility than a relational database and is a solid option for companies who must analyze large quantities of data or whose data structures they manage are variable.
