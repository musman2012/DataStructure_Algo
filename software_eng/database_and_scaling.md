## Database Scaling 

### Database Sharding
Row wise partitioning the database tables into multiple instances to improve the query speed. Ths partitioning can be based on Zipcode, geolocation or using some consistent hashing.
In contrast to this, Horizontal Partitioning partitions the data in the same database.

**Pros:** Scale (Memory, Data), Security (User access control), Optimal and Small Index

**Cons:** Complex Client, Transactions across shards, Roll backs, Schema changes, Joins
