# Redis_Commands
Redis is a powerful in-memory data structure store, and it provides a wide array of commands to manipulate and query data. Below is a list of some of the most commonly used Redis commands

### 1. **SET**
   - **Description**: Sets the value of a key.
   - **Syntax**: `SET key value`
   - **Example**:
     ```sh
     SET mykey "Hello"
     ```
   - **Output**:
     ```sh
     OK
     ```

### 2. **GET**
   - **Description**: Gets the value of a key.
   - **Syntax**: `GET key`
   - **Example**:
     ```sh
     GET mykey
     ```
   - **Output**:
     ```sh
     "Hello"
     ```

### 3. **DEL**
   - **Description**: Deletes a key.
   - **Syntax**: `DEL key`
   - **Example**:
     ```sh
     DEL mykey
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 4. **EXPIRE**
   - **Description**: Set a timeout on a key.
   - **Syntax**: `EXPIRE key seconds`
   - **Example**:
     ```sh
     EXPIRE mykey 60
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 5. **TTL**
   - **Description**: Get the time to live for a key.
   - **Syntax**: `TTL key`
   - **Example**:
     ```sh
     TTL mykey
     ```
   - **Output**:
     ```sh
     (integer) 30
     ```

### 6. **INCR**
   - **Description**: Increments the integer value of a key by one.
   - **Syntax**: `INCR key`
   - **Example**:
     ```sh
     INCR counter
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 7. **LPUSH**
   - **Description**: Inserts a value at the head of a list.
   - **Syntax**: `LPUSH key value [value ...]`
   - **Example**:
     ```sh
     LPUSH mylist "world"
     LPUSH mylist "hello"
     ```
   - **Output**:
     ```sh
     (integer) 2
     ```

### 8. **LRANGE**
   - **Description**: Gets a range of elements from a list.
   - **Syntax**: `LRANGE key start stop`
   - **Example**:
     ```sh
     LRANGE mylist 0 -1
     ```
   - **Output**:
     ```sh
     1) "hello"
     2) "world"
     ```

### 9. **SADD**
   - **Description**: Adds one or more members to a set.
   - **Syntax**: `SADD key member [member ...]`
   - **Example**:
     ```sh
     SADD myset "one"
     SADD myset "two"
     ```
   - **Output**:
     ```sh
     (integer) 2
     ```

### 10. **SMEMBERS**
   - **Description**: Gets all members in a set.
   - **Syntax**: `SMEMBERS key`
   - **Example**:
     ```sh
     SMEMBERS myset
     ```
   - **Output**:
     ```sh
     1) "one"
     2) "two"
     ```

### 11. **HSET**
   - **Description**: Sets the value of a field in a hash.
   - **Syntax**: `HSET key field value`
   - **Example**:
     ```sh
     HSET myhash field1 "foo"
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 12. **HGET**
   - **Description**: Gets the value of a field in a hash.
   - **Syntax**: `HGET key field`
   - **Example**:
     ```sh
     HGET myhash field1
     ```
   - **Output**:
     ```sh
     "foo"
     ```

### 13. **HGETALL**
   - **Description**: Gets all fields and values in a hash.
   - **Syntax**: `HGETALL key`
   - **Example**:
     ```sh
     HGETALL myhash
     ```
   - **Output**:
     ```sh
     1) "field1"
     2) "foo"
     ```

### 14. **ZADD**
   - **Description**: Adds one or more members to a sorted set, or updates the score if it already exists.
   - **Syntax**: `ZADD key score member [score member ...]`
   - **Example**:
     ```sh
     ZADD myzset 1 "one"
     ZADD myzset 2 "two"
     ```
   - **Output**:
     ```sh
     (integer) 2
     ```

### 15. **ZRANGE**
   - **Description**: Gets a range of members in a sorted set, by index.
   - **Syntax**: `ZRANGE key start stop [WITHSCORES]`
   - **Example**:
     ```sh
     ZRANGE myzset 0 -1
     ```
   - **Output**:
     ```sh
     1) "one"
     2) "two"
     ```

### 16. **KEYS**
   - **Description**: Finds all keys matching the given pattern.
   - **Syntax**: `KEYS pattern`
   - **Example**:
     ```sh
     KEYS *
     ```
   - **Output**:
     ```sh
     1) "mylist"
     2) "myset"
     3) "myhash"
     ```

### 17. **FLUSHALL**
   - **Description**: Removes all keys from all databases.
   - **Syntax**: `FLUSHALL`
   - **Example**:
     ```sh
     FLUSHALL
     ```
   - **Output**:
     ```sh
     OK
     ```

### 18. **PING**
   - **Description**: Checks if the server is alive.
   - **Syntax**: `PING`
   - **Example**:
     ```sh
     PING
     ```
   - **Output**:
     ```sh
     PONG
     ```

### 19. **MULTI**
   - **Description**: Marks the start of a transaction block.
   - **Syntax**: `MULTI`
   - **Example**:
     ```sh
     MULTI
     ```
   - **Output**:
     ```sh
     OK
     ```

### 20. **EXEC**
   - **Description**: Executes all commands issued after MULTI.
   - **Syntax**: `EXEC`
   - **Example**:
     ```sh
     EXEC
     ```
   - **Output**:
     ```sh
     1) "value1"
     2) "value2"
     ```

### 21. **DISCARD**
   - **Description**: Flushes all commands issued after MULTI.
   - **Syntax**: `DISCARD`
   - **Example**:
     ```sh
     DISCARD
     ```
   - **Output**:
     ```sh
     OK
     ```

 
### 22. **APPEND**
   - **Description**: Appends a value to a key.
   - **Syntax**: `APPEND key value`
   - **Example**:
     ```sh
     SET mykey "Hello"
     APPEND mykey " World"
     ```
   - **Output**:
     ```sh
     (integer) 11
     ```

### 23. **SUBSTR**
   - **Description**: Get a substring of a key’s value.
   - **Syntax**: `SUBSTR key start end`
   - **Example**:
     ```sh
     SET mykey "Hello World"
     SUBSTR mykey 0 4
     ```
   - **Output**:
     ```sh
     "Hello"
     ```

### 24. **SREM**
   - **Description**: Removes one or more members from a set.
   - **Syntax**: `SREM key member [member ...]`
   - **Example**:
     ```sh
     SADD myset "one" "two" "three"
     SREM myset "two"
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 25. **SISMEMBER**
   - **Description**: Checks if a member is part of a set.
   - **Syntax**: `SISMEMBER key member`
   - **Example**:
     ```sh
     SISMEMBER myset "one"
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 26. **HDEL**
   - **Description**: Deletes one or more fields from a hash.
   - **Syntax**: `HDEL key field [field ...]`
   - **Example**:
     ```sh
     HSET myhash field1 "foo"
     HSET myhash field2 "bar"
     HDEL myhash field1
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 27. **HINCRBY**
   - **Description**: Increments the integer value of a hash field by the given number.
   - **Syntax**: `HINCRBY key field increment`
   - **Example**:
     ```sh
     HSET myhash field1 10
     HINCRBY myhash field1 5
     ```
   - **Output**:
     ```sh
     15
     ```

### 28. **HKEYS**
   - **Description**: Gets all the fields in a hash.
   - **Syntax**: `HKEYS key`
   - **Example**:
     ```sh
     HSET myhash field1 "foo"
     HSET myhash field2 "bar"
     HKEYS myhash
     ```
   - **Output**:
     ```sh
     1) "field1"
     2) "field2"
     ```

### 29. **HVALS**
   - **Description**: Gets all the values in a hash.
   - **Syntax**: `HVALS key`
   - **Example**:
     ```sh
     HSET myhash field1 "foo"
     HSET myhash field2 "bar"
     HVALS myhash
     ```
   - **Output**:
     ```sh
     1) "foo"
     2) "bar"
     ```

### 30. **ZREM**
   - **Description**: Removes one or more members from a sorted set.
   - **Syntax**: `ZREM key member [member ...]`
   - **Example**:
     ```sh
     ZADD myzset 1 "one"
     ZADD myzset 2 "two"
     ZREM myzset "one"
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 31. **ZINCRBY**
   - **Description**: Increments the score of a member in a sorted set.
   - **Syntax**: `ZINCRBY key increment member`
   - **Example**:
     ```sh
     ZADD myzset 1 "one"
     ZINCRBY myzset 2 "one"
     ```
   - **Output**:
     ```sh
     3
     ```

### 32. **ZREVRANGE**
   - **Description**: Gets a range of members in a sorted set, by index, with scores ordered from highest to lowest.
   - **Syntax**: `ZREVRANGE key start stop [WITHSCORES]`
   - **Example**:
     ```sh
     ZADD myzset 1 "one"
     ZADD myzset 2 "two"
     ZREVRANGE myzset 0 -1 WITHSCORES
     ```
   - **Output**:
     ```sh
     1) "two"
     2) "2"
     3) "one"
     4) "1"
     ```

### 33. **ZCARD**
   - **Description**: Gets the number of members in a sorted set.
   - **Syntax**: `ZCARD key`
   - **Example**:
     ```sh
     ZADD myzset 1 "one"
     ZADD myzset 2 "two"
     ZCARD myzset
     ```
   - **Output**:
     ```sh
     (integer) 2
     ```

### 34. **ZREMRANGEBYRANK**
   - **Description**: Removes all members in a sorted set within the given indexes.
   - **Syntax**: `ZREMRANGEBYRANK key start stop`
   - **Example**:
     ```sh
     ZADD myzset 1 "one"
     ZADD myzset 2 "two"
     ZADD myzset 3 "three"
     ZREMRANGEBYRANK myzset 0 1
     ```
   - **Output**:
     ```sh
     (integer) 2
     ```

### 35. **ZREMRANGEBYSCORE**
   - **Description**: Removes all members in a sorted set within the given scores.
   - **Syntax**: `ZREMRANGEBYSCORE key min max`
   - **Example**:
     ```sh
     ZADD myzset 1 "one"
     ZADD myzset 2 "two"
     ZADD myzset 3 "three"
     ZREMRANGEBYSCORE myzset 1 2
     ```
   - **Output**:
     ```sh
     (integer) 2
     ```

### 36. **GEORADIUS**
   - **Description**: Query a sorted set by geographical location (longitude and latitude).
   - **Syntax**: `GEORADIUS key longitude latitude radius unit [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count]`
   - **Example**:
     ```sh
     GEOADD mygeokey 13.361389 38.115556 "Palermo"
     GEOADD mygeokey 15.087269 37.502669 "Catania"
     GEORADIUS mygeokey 15 37 200 km
     ```
   - **Output**:
     ```sh
     1) "Catania"
     ```

### 37. **GEOADD**
   - **Description**: Adds a geospatial item (longitude and latitude) to a sorted set.
   - **Syntax**: `GEOADD key longitude latitude member`
   - **Example**:
     ```sh
     GEOADD mygeokey 13.361389 38.115556 "Palermo"
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 38. **GEOHASH**
   - **Description**: Gets the geohash of the members in a geospatial index.
   - **Syntax**: `GEOHASH key member [member ...]`
   - **Example**:
     ```sh
     GEOADD mygeokey 13.361389 38.115556 "Palermo"
     GEOHASH mygeokey "Palermo"
     ```
   - **Output**:
     ```sh
     1) "scoords"
     ```

### 39. **GEODIST**
   - **Description**: Gets the distance between two members in a geospatial index.
   - **Syntax**: `GEODIST key member1 member2 unit`
   - **Example**:
     ```sh
     GEOADD mygeokey 13.361389 38.115556 "Palermo"
     GEOADD mygeokey 15.087269 37.502669 "Catania"
     GEODIST mygeokey "Palermo" "Catania" km
     ```
   - **Output**:
     ```sh
     "166.2746"
     ```

### 40. **SCAN**
   - **Description**: Iterates through a collection of keys.
   - **Syntax**: `SCAN cursor [MATCH pattern] [COUNT count]`
   - **Example**:
     ```sh
     SET key1 "value1"
     SET key2 "value2"
     SCAN 0 MATCH key*
     ```
   - **Output**:
     ```sh
     1)

 "0"
     2) 1) "key1"
        2) "key2"
     ```

### 41. **HSCAN**
   - **Description**: Iterates through fields in a hash.
   - **Syntax**: `HSCAN key cursor [MATCH pattern] [COUNT count]`
   - **Example**:
     ```sh
     HSET myhash field1 "foo"
     HSET myhash field2 "bar"
     HSCAN myhash 0 MATCH field*
     ```
   - **Output**:
     ```sh
     1) "0"
     2) 1) "field1"
        2) "foo"
        3) "field2"
        4) "bar"
     ```

### 42. **SSCAN**
   - **Description**: Iterates through members in a set.
   - **Syntax**: `SSCAN key cursor [MATCH pattern] [COUNT count]`
   - **Example**:
     ```sh
     SADD myset "one"
     SADD myset "two"
     SSCAN myset 0 MATCH *one*
     ```
   - **Output**:
     ```sh
     1) "0"
     2) 1) "one"
     ```

### 43. **ZSCAN**
   - **Description**: Iterates through members in a sorted set.
   - **Syntax**: `ZSCAN key cursor [MATCH pattern] [COUNT count]`
   - **Example**:
     ```sh
     ZADD myzset 1 "one"
     ZADD myzset 2 "two"
     ZSCAN myzset 0 MATCH *o*
     ```
   - **Output**:
     ```sh
     1) "0"
     2) 1) "one"
        2) "1"
     ```
### 44. **BITSET**
   - **Description**: Sets or clears the bit at offset in the string value stored at key.
   - **Syntax**: `BITSET key offset value`
   - **Example**:
     ```sh
     BITSET mykey 7 1
     ```
   - **Output**:
     ```sh
     OK
     ```

### 45. **BITGET**
   - **Description**: Returns the bit value at offset in the string value stored at key.
   - **Syntax**: `BITGET key offset`
   - **Example**:
     ```sh
     BITGET mykey 7
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 46. **BITOP**
   - **Description**: Performs bitwise operations between multiple strings.
   - **Syntax**: `BITOP operation destkey key [key ...]`
   - **Example**:
     ```sh
     SET bitkey1 "\x01"
     SET bitkey2 "\x02"
     BITOP OR resultbitkey bitkey1 bitkey2
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 47. **PFADD**
   - **Description**: Adds elements to the HyperLogLog data structure.
   - **Syntax**: `PFADD key element [element ...]`
   - **Example**:
     ```sh
     PFADD myhll "element1" "element2"
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 48. **PFCOUNT**
   - **Description**: Returns the approximated cardinality (number of unique elements) of the HyperLogLog data structure.
   - **Syntax**: `PFCOUNT key [key ...]`
   - **Example**:
     ```sh
     PFCOUNT myhll
     ```
   - **Output**:
     ```sh
     (integer) 2
     ```

### 49. **PFMERGE**
   - **Description**: Merges multiple HyperLogLog data structures into one.
   - **Syntax**: `PFMERGE destkey sourcekey [sourcekey ...]`
   - **Example**:
     ```sh
     PFMERGE mergedhll myhll1 myhll2
     ```
   - **Output**:
     ```sh
     OK
     ```

### 50. **XADD**
   - **Description**: Adds a message to a stream.
   - **Syntax**: `XADD key ID field value [field value ...]`
   - **Example**:
     ```sh
     XADD mystream * field1 value1 field2 value2
     ```
   - **Output**:
     ```sh
     "1680279308445-0"
     ```

### 51. **XRANGE**
   - **Description**: Returns a range of messages from a stream.
   - **Syntax**: `XRANGE key start end [COUNT count]`
   - **Example**:
     ```sh
     XRANGE mystream 0 1680279308445-0
     ```
   - **Output**:
     ```sh
     1) 1) "1680279308445-0"
        2) 1) "field1"
           2) "value1"
           3) "field2"
           4) "value2"
     ```

### 52. **XREVRANGE**
   - **Description**: Returns a range of messages from a stream, in reverse order.
   - **Syntax**: `XREVRANGE key end start [COUNT count]`
   - **Example**:
     ```sh
     XREVRANGE mystream 1680279308445-0 0
     ```
   - **Output**:
     ```sh
     1) 1) "1680279308445-0"
        2) 1) "field1"
           2) "value1"
           3) "field2"
           4) "value2"
     ```

### 53. **XTRIM**
   - **Description**: Trims a stream to a specific length.
   - **Syntax**: `XTRIM key MAXLEN count [MINID minid]`
   - **Example**:
     ```sh
     XTRIM mystream MAXLEN 1000
     ```
   - **Output**:
     ```sh
     (integer) 0
     ```

### 54. **ZINTERSTORE**
   - **Description**: Computes the intersection of multiple sorted sets and stores the resulting sorted set in a new key.
   - **Syntax**: `ZINTERSTORE destination numkeys key [key ...]`
   - **Example**:
     ```sh
     ZADD zset1 1 "one" 2 "two"
     ZADD zset2 2 "two" 3 "three"
     ZINTERSTORE interzset 2 zset1 zset2
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 55. **ZUNIONSTORE**
   - **Description**: Computes the union of multiple sorted sets and stores the resulting sorted set in a new key.
   - **Syntax**: `ZUNIONSTORE destination numkeys key [key ...]`
   - **Example**:
     ```sh
     ZADD zset1 1 "one" 2 "two"
     ZADD zset2 2 "two" 3 "three"
     ZUNIONSTORE unionzset 2 zset1 zset2
     ```
   - **Output**:
     ```sh
     (integer) 3
     ```

### 56. **SDIFF**
   - **Description**: Computes the difference between multiple sets.
   - **Syntax**: `SDIFF key [key ...]`
   - **Example**:
     ```sh
     SADD set1 "a" "b" "c"
     SADD set2 "b" "c" "d"
     SDIFF set1 set2
     ```
   - **Output**:
     ```sh
     1) "a"
     ```

### 57. **SDIFFSTORE**
   - **Description**: Computes the difference between multiple sets and stores the resulting set in a new key.
   - **Syntax**: `SDIFFSTORE destination key [key ...]`
   - **Example**:
     ```sh
     SADD set1 "a" "b" "c"
     SADD set2 "b" "c" "d"
     SDIFFSTORE diffset set1 set2
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 58. **SINTER**
   - **Description**: Computes the intersection of multiple sets.
   - **Syntax**: `SINTER key [key ...]`
   - **Example**:
     ```sh
     SADD set1 "a" "b" "c"
     SADD set2 "b" "c" "d"
     SINTER set1 set2
     ```
   - **Output**:
     ```sh
     1) "b"
     2) "c"
     ```

### 59. **SINTERSTORE**
   - **Description**: Computes the intersection of multiple sets and stores the resulting set in a new key.
   - **Syntax**: `SINTERSTORE destination key [key ...]`
   - **Example**:
     ```sh
     SADD set1 "a" "b" "c"
     SADD set2 "b" "c" "d"
     SINTERSTORE interset set1 set2
     ```
   - **Output**:
     ```sh
     (integer) 2
     ```

### 60. **SUNION**
   - **Description**: Computes the union of multiple sets.
   - **Syntax**: `SUNION key [key ...]`
   - **Example**:
     ```sh
     SADD set1 "a" "b" "c"
     SADD set2 "b" "c" "d"
     SUNION set1 set2
     ```
   - **Output**:
     ```sh
     1) "a"
     2) "b"
     3) "c"
     4) "d"
     ```

### 61. **SUNIONSTORE**
   - **Description**: Computes the union of multiple sets and stores the resulting set in a new key.
   - **Syntax**: `SUNIONSTORE destination key [key ...]`
   - **Example**:
     ```sh
     SADD set1 "a" "b" "c"
     SADD set2 "b" "c" "d"
     SUNIONSTORE unionset set1 set2
     ```
   - **Output**:
     ```sh
     (integer) 4
     ```

### 62. **SORT**
   - **Description**: Sorts the elements of a list, set, or sorted set.
   - **Syntax**: `SORT key [BY pattern] [LIMIT offset count] [GET pattern] [ASC|DESC] [ALPHA]`
   - **Example**:
     ```sh
     LPUSH mylist 2
     LPUSH mylist

 1
     LPUSH mylist 3
     SORT mylist
     ```
   - **Output**:
     ```sh
     1) "1"
     2) "2"
     3) "3"
     ```

### 63. **EVAL**
   - **Description**: Executes a Lua script.
   - **Syntax**: `EVAL script numkeys key [key ...] arg [arg ...]`
   - **Example**:
     ```sh
     EVAL "return redis.call('SET', KEYS[1], ARGV[1])" 1 mykey "myvalue"
     ```
   - **Output**:
     ```sh
     OK
     ```

### 64. **SCRIPT LOAD**
   - **Description**: Loads a Lua script into the script cache.
   - **Syntax**: `SCRIPT LOAD script`
   - **Example**:
     ```sh
     SCRIPT LOAD "return redis.call('GET', KEYS[1])"
     ```
   - **Output**:
     ```sh
     "0e85d5f915a8b6d7b2ed2c9d597c1c2b"
     ```

### 65. **SCRIPT FLUSH**
   - **Description**: Removes all the scripts from the script cache.
   - **Syntax**: `SCRIPT FLUSH`
   - **Example**:
     ```sh
     SCRIPT FLUSH
     ```
   - **Output**:
     ```sh
     OK
     ```

### 66. **SCRIPT KILL**
   - **Description**: Kills the script currently in execution.
   - **Syntax**: `SCRIPT KILL`
   - **Example**:
     ```sh
     SCRIPT KILL
     ```
   - **Output**:
     ```sh
     OK
     ```

### 67. **LATENCY DOCTOR**
   - **Description**: Provides information on latency spikes in Redis.
   - **Syntax**: `LATENCY DOCTOR`
   - **Example**:
     ```sh
     LATENCY DOCTOR
     ```
   - **Output**:
     ```sh
     1) 1) "latency"
        2) "value"
     ```

### 68. **LATENCY HISTORY**
   - **Description**: Returns the latency history for a specified event.
   - **Syntax**: `LATENCY HISTORY event`
   - **Example**:
     ```sh
     LATENCY HISTORY command
     ```
   - **Output**:
     ```sh
     1) 1) 1625182325
        2) 1) 123
     ```

### 69. **LATENCY LATEST**
   - **Description**: Returns the latest latency information for a specified event.
   - **Syntax**: `LATENCY LATEST event`
   - **Example**:
     ```sh
     LATENCY LATEST command
     ```
   - **Output**:
     ```sh
     1) 1) 1625182325
        2) 1) 123
     ```

### 70. **PUBLISH**
   - **Description**: Posts a message to a channel.
   - **Syntax**: `PUBLISH channel message`
   - **Example**:
     ```sh
     PUBLISH mychannel "Hello, Redis!"
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 71. **SUBSCRIBE**
   - **Description**: Subscribes to one or more channels.
   - **Syntax**: `SUBSCRIBE channel [channel ...]`
   - **Example**:
     ```sh
     SUBSCRIBE mychannel
     ```
   - **Output**:
     ```sh
     1) "subscribe"
     2) "mychannel"
     3) (integer) 1
     ```

### 72. **UNSUBSCRIBE**
   - **Description**: Unsubscribes from one or more channels.
   - **Syntax**: `UNSUBSCRIBE channel [channel ...]`
   - **Example**:
     ```sh
     UNSUBSCRIBE mychannel
     ```
   - **Output**:
     ```sh
     1) "unsubscribe"
     2) "mychannel"
     3) (integer) 0
     ```

### 73. **PUBSUB CHANNELS**
   - **Description**: Lists the currently active channels.
   - **Syntax**: `PUBSUB CHANNELS [pattern]`
   - **Example**:
     ```sh
     PUBSUB CHANNELS
     ```
   - **Output**:
     ```sh
     1) "mychannel"
     ```

### 74. **PUBSUB NUMSUB**
   - **Description**: Returns the number of subscribers (clients) for the given channels.
   - **Syntax**: `PUBSUB NUMSUB channel [channel ...]`
   - **Example**:
     ```sh
     PUBSUB NUMSUB mychannel
     ```
   - **Output**:
     ```sh
     1) "mychannel"
     2) (integer) 1
     ```

### 75. **PUBSUB NUMPAT**
   - **Description**: Returns the number of patterns currently subscribed to.
   - **Syntax**: `PUBSUB NUMPAT`
   - **Example**:
     ```sh
     PUBSUB NUMPAT
     ```
   - **Output**:
     ```sh
     (integer) 0
     ```

### 76. **SLOWLOG GET**
   - **Description**: Retrieves the slow log entries.
   - **Syntax**: `SLOWLOG GET [count]`
   - **Example**:
     ```sh
     SLOWLOG GET 10
     ```
   - **Output**:
     ```sh
     1) 1) (integer) 1
        2) (integer) 1625182325
        3) (integer) 123
        4) 1) "SET"
           2) "key"
           3) "value"
     ```

### 77. **SLOWLOG LEN**
   - **Description**: Returns the length of the slow log.
   - **Syntax**: `SLOWLOG LEN`
   - **Example**:
     ```sh
     SLOWLOG LEN
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 78. **SLOWLOG RESET**
   - **Description**: Clears all the slow log entries.
   - **Syntax**: `SLOWLOG RESET`
   - **Example**:
     ```sh
     SLOWLOG RESET
     ```
   - **Output**:
     ```sh
     OK
     ```

### 79. **CLIENT LIST**
   - **Description**: Returns information and statistics about the connected clients.
   - **Syntax**: `CLIENT LIST`
   - **Example**:
     ```sh
     CLIENT LIST
     ```
   - **Output**:
     ```sh
     1) "id=1"
        2) "addr=127.0.0.1:6379"
        3) "fd=6"
        4) "name=redis-cli"
     ```

### 80. **CLIENT GETNAME**
   - **Description**: Gets the name of the current connection.
   - **Syntax**: `CLIENT GETNAME`
   - **Example**:
     ```sh
     CLIENT GETNAME
     ```
   - **Output**:
     ```sh
     "myclient"
     ```

### 81. **CLIENT SETNAME**
   - **Description**: Sets the name of the current connection.
   - **Syntax**: `CLIENT SETNAME name`
   - **Example**:
     ```sh
     CLIENT SETNAME "myclient"
     ```
   - **Output**:
     ```sh
     OK
     ```

### 82. **CLIENT PAUSE**
   - **Description**: Blocks all the clients for the specified amount of time.
   - **Syntax**: `CLIENT PAUSE timeout`
   - **Example**:
     ```sh
     CLIENT PAUSE 5000
     ```
   - **Output**:
     ```sh
     OK
     ```

### 83. **BGSAVE**
   - **Description**: Asynchronously saves the dataset to disk.
   - **Syntax**: `BGSAVE`
   - **Example**:
     ```sh
     BGSAVE
     ```
   - **Output**:
     ```sh
     OK
     ```

### 84. **SAVE**
   - **Description**: Synchronously saves the dataset to disk.
   - **Syntax**: `SAVE`
   - **Example**:
     ```sh
     SAVE
     ```
   - **Output**:
     ```sh
     OK
     ```

### 85. **SHUTDOWN**
   - **Description**: Shuts down the Redis server.
   - **Syntax**: `SHUTDOWN [NOSAVE|SAVE]`
   - **Example**:
     ```sh
     SHUTDOWN SAVE
     ```
   - **Output**:
     ```sh
     OK
     ```

### 86. **INFO**
   - **Description**: Provides information and statistics about the Redis server.
   - **Syntax**: `INFO [section]`
   - **Example**:
     ```sh
     INFO memory
     ```
   - **Output**:
     ```sh
     # Memory
     used_memory:1024000
     ```
   
### 87

. **CONFIG GET**
   - **Description**: Gets the value of a configuration parameter.
   - **Syntax**: `CONFIG GET parameter`
   - **Example**:
     ```sh
     CONFIG GET maxmemory
     ```
   - **Output**:
     ```sh
     1) "maxmemory"
     2) "0"
     ```

### 88. **CONFIG SET**
   - **Description**: Sets the value of a configuration parameter.
   - **Syntax**: `CONFIG SET parameter value`
   - **Example**:
     ```sh
     CONFIG SET maxmemory 104857600
     ```
   - **Output**:
     ```sh
     OK
     ```

### 89. **CONFIG RESETSTAT**
   - **Description**: Resets the statistics reported by INFO.
   - **Syntax**: `CONFIG RESETSTAT`
   - **Example**:
     ```sh
     CONFIG RESETSTAT
     ```
   - **Output**:
     ```sh
     OK
     ```

### 90. **LATENCY GRAPH**
   - **Description**: Provides a graphical representation of latency over time.
   - **Syntax**: `LATENCY GRAPH`
   - **Example**:
     ```sh
     LATENCY GRAPH
     ```
   - **Output**:
     ```sh
     1) 1) "latency"
        2) "value"
     ```

### 91. **WAIT**
   - **Description**: Waits for the specified number of replicas to acknowledge the write.
   - **Syntax**: `WAIT numreplicas timeout`
   - **Example**:
     ```sh
     WAIT 2 5000
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```


### 92. **DEBUG OBJECT**
   - **Description**: Provides information about the internal representation of a key.
   - **Syntax**: `DEBUG OBJECT key`
   - **Example**:
     ```sh
     SET mykey "somevalue"
     DEBUG OBJECT mykey
     ```
   - **Output**:
     ```sh
     1) "serialize"
     2) "refcount:1"
     3) "encoding:embstr"
     4) "idletime:0"
     ```

### 93. **DEBUG SEGFAULT**
   - **Description**: Forces a server crash for debugging purposes.
   - **Syntax**: `DEBUG SEGFAULT`
   - **Example**:
     ```sh
     DEBUG SEGFAULT
     ```
   - **Output**: The server will crash and restart.

### 94. **CLUSTER INFO**
   - **Description**: Provides information about the cluster.
   - **Syntax**: `CLUSTER INFO`
   - **Example**:
     ```sh
     CLUSTER INFO
     ```
   - **Output**:
     ```sh
     cluster_state:ok
     cluster_slots_assigned:16384
     cluster_slots_ok:16384
     ```

### 95. **CLUSTER NODES**
   - **Description**: Lists all nodes in the cluster.
   - **Syntax**: `CLUSTER NODES`
   - **Example**:
     ```sh
     CLUSTER NODES
     ```
   - **Output**:
     ```sh
     1) "d6e81e9f5e2c7d86311cc8aeff3e2bbf2b1e3e51 127.0.0.1:6379@16379 master - 0 1625182326000 1 connected 5461-10922"
     ```

### 96. **CLUSTER MEET**
   - **Description**: Makes the current node join a cluster.
   - **Syntax**: `CLUSTER MEET ip port`
   - **Example**:
     ```sh
     CLUSTER MEET 127.0.0.1 6379
     ```
   - **Output**:
     ```sh
     OK
     ```

### 97. **CLUSTER LEAVE**
   - **Description**: Makes the current node leave the cluster.
   - **Syntax**: `CLUSTER LEAVE`
   - **Example**:
     ```sh
     CLUSTER LEAVE
     ```
   - **Output**:
     ```sh
     OK
     ```

### 98. **CLUSTER FORGET**
   - **Description**: Removes a node from the cluster.
   - **Syntax**: `CLUSTER FORGET nodeid`
   - **Example**:
     ```sh
     CLUSTER FORGET d6e81e9f5e2c7d86311cc8aeff3e2bbf2b1e3e51
     ```
   - **Output**:
     ```sh
     OK
     ```

### 99. **CLUSTER SLAVES**
   - **Description**: Lists the replicas of a master node.
   - **Syntax**: `CLUSTER SLAVES nodeid`
   - **Example**:
     ```sh
     CLUSTER SLAVES d6e81e9f5e2c7d86311cc8aeff3e2bbf2b1e3e51
     ```
   - **Output**:
     ```sh
     1) "d4e81e9f5e2c7d86311cc8aeff3e2bbf2b1e3e52 127.0.0.1:6380@16380"
     ```

### 100. **CLUSTER SETSLOT**
   - **Description**: Assigns a hash slot to a node or a node to a hash slot.
   - **Syntax**: `CLUSTER SETSLOT slot IMPORTING|MIGRATING|STABLE nodeid`
   - **Example**:
     ```sh
     CLUSTER SETSLOT 0 IMPORTING d6e81e9f5e2c7d86311cc8aeff3e2bbf2b1e3e51
     ```
   - **Output**:
     ```sh
     OK
     ```

### 101. **CLUSTER BUMPEPOCH**
   - **Description**: Increases the cluster epoch.
   - **Syntax**: `CLUSTER BUMPEPOCH`
   - **Example**:
     ```sh
     CLUSTER BUMPEPOCH
     ```
   - **Output**:
     ```sh
     OK
     ```

### 102. **CLUSTER REPLICATE**
   - **Description**: Makes the current node a replica of the specified master node.
   - **Syntax**: `CLUSTER REPLICATE nodeid`
   - **Example**:
     ```sh
     CLUSTER REPLICATE d6e81e9f5e2c7d86311cc8aeff3e2bbf2b1e3e51
     ```
   - **Output**:
     ```sh
     OK
     ```

### 103. **CLUSTER RESET**
   - **Description**: Resets the cluster state of the node.
   - **Syntax**: `CLUSTER RESET [HARD|SOFT]`
   - **Example**:
     ```sh
     CLUSTER RESET HARD
     ```
   - **Output**:
     ```sh
     OK
     ```

### 104. **READONLY**
   - **Description**: Marks the current connection as read-only.
   - **Syntax**: `READONLY`
   - **Example**:
     ```sh
     READONLY
     ```
   - **Output**:
     ```sh
     OK
     ```

### 105. **READWRITE**
   - **Description**: Marks the current connection as read-write.
   - **Syntax**: `READWRITE`
   - **Example**:
     ```sh
     READWRITE
     ```
   - **Output**:
     ```sh
     OK
     ```

### 106. **LATENCY LATEST**
   - **Description**: Returns the latest latency information for a specified event.
   - **Syntax**: `LATENCY LATEST event`
   - **Example**:
     ```sh
     LATENCY LATEST command
     ```
   - **Output**:
     ```sh
     1) 1) 1625182325
        2) 1) 123
     ```

### 107. **MODULE LIST**
   - **Description**: Lists all modules loaded in the Redis server.
   - **Syntax**: `MODULE LIST`
   - **Example**:
     ```sh
     MODULE LIST
     ```
   - **Output**:
     ```sh
     1) 1) "name"
        2) "version"
        3) "path"
     ```

### 108. **MODULE LOAD**
   - **Description**: Loads a Redis module from the specified path.
   - **Syntax**: `MODULE LOAD path`
   - **Example**:
     ```sh
     MODULE LOAD /path/to/module.so
     ```
   - **Output**:
     ```sh
     OK
     ```

### 109. **MODULE UNLOAD**
   - **Description**: Unloads a Redis module.
   - **Syntax**: `MODULE UNLOAD name`
   - **Example**:
     ```sh
     MODULE UNLOAD mymodule
     ```
   - **Output**:
     ```sh
     OK
     ```

### 110. **MEMORY STATS**
   - **Description**: Provides detailed memory usage statistics.
   - **Syntax**: `MEMORY STATS`
   - **Example**:
     ```sh
     MEMORY STATS
     ```
   - **Output**:
     ```sh
     1) 1) "peak"
        2) "value"
     ```

### 111. **MEMORY USAGE**
   - **Description**: Returns the memory usage of a key.
   - **Syntax**: `MEMORY USAGE key`
   - **Example**:
     ```sh
     MEMORY USAGE mykey
     ```
   - **Output**:
     ```sh
     (integer) 64
     ```

### 112. **MEMORY PURGE**
   - **Description**: Purges the memory allocator's internal fragmentation.
   - **Syntax**: `MEMORY PURGE`
   - **Example**:
     ```sh
     MEMORY PURGE
     ```
   - **Output**:
     ```sh
     OK
     ```

### 113. **MONITOR**
   - **Description**: Streams all the commands received by the server in real time.
   - **Syntax**: `MONITOR`
   - **Example**:
     ```sh
     MONITOR
     ```
   - **Output**:
     ```sh
     1) 1) "1625182325000"
        2) "127.0.0.1:6379"
        3) "SET"
        4) "mykey"
        5) "myvalue"
     ```

### 114. **CLIENT SETNAME**
   - **Description**: Sets the name of the current connection.
   - **Syntax**: `CLIENT SETNAME name`
   - **Example**:
     ```sh


     CLIENT SETNAME "myclient"
     ```
   - **Output**:
     ```sh
     OK
     ```

### 115. **MODULE LOAD**
   - **Description**: Loads a Redis module from the specified path.
   - **Syntax**: `MODULE LOAD path`
   - **Example**:
     ```sh
     MODULE LOAD /path/to/module.so
     ```
   - **Output**:
     ```sh
     OK
     ```

### 116. **MODULE UNLOAD**
   - **Description**: Unloads a Redis module.
   - **Syntax**: `MODULE UNLOAD name`
   - **Example**:
     ```sh
     MODULE UNLOAD mymodule
     ```
   - **Output**:
     ```sh
     OK
     ```

### 117. **SETNX**
   - **Description**: Sets the value of a key only if it does not already exist.
   - **Syntax**: `SETNX key value`
   - **Example**:
     ```sh
     SETNX mykey "myvalue"
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 118. **SETEX**
   - **Description**: Sets the value of a key with an expiration time.
   - **Syntax**: `SETEX key seconds value`
   - **Example**:
     ```sh
     SETEX mykey 10 "myvalue"
     ```
   - **Output**:
     ```sh
     OK
     ```

### 119. **MSETNX**
   - **Description**: Sets multiple keys only if none of the keys exist.
   - **Syntax**: `MSETNX key value [key value ...]`
   - **Example**:
     ```sh
     MSETNX key1 "value1" key2 "value2"
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 120. **PSUBSCRIBE**
   - **Description**: Subscribes to multiple channels using pattern matching.
   - **Syntax**: `PSUBSCRIBE pattern [pattern ...]`
   - **Example**:
     ```sh
     PSUBSCRIBE "news.*"
     ```
   - **Output**:
     ```sh
     1) "psubscribe"
     2) "news.*"
     3) (integer) 1
     ```

### 121. **PUNSUBSCRIBE**
   - **Description**: Unsubscribes from multiple channels using pattern matching.
   - **Syntax**: `PUNSUBSCRIBE pattern [pattern ...]`
   - **Example**:
     ```sh
     PUNSUBSCRIBE "news.*"
     ```
   - **Output**:
     ```sh
     1) "punsubscribe"
     2) "news.*"
     3) (integer) 0
     ```

### 122. **SPOP**
   - **Description**: Removes and returns a random element from a set.
   - **Syntax**: `SPOP key [count]`
   - **Example**:
     ```sh
     SADD myset "one" "two" "three"
     SPOP myset
     ```
   - **Output**:
     ```sh
     "one"
     ```

### 123. **SRANDMEMBER**
   - **Description**: Returns a random element from a set without removing it.
   - **Syntax**: `SRANDMEMBER key [count]`
   - **Example**:
     ```sh
     SRANDMEMBER myset
     ```
   - **Output**:
     ```sh
     "two"
     ```

### 124. **SINTERSTORE**
   - **Description**: Computes the intersection of multiple sets and stores the result in a new set.
   - **Syntax**: `SINTERSTORE destination key [key ...]`
   - **Example**:
     ```sh
     SADD set1 "a" "b" "c"
     SADD set2 "b" "c" "d"
     SINTERSTORE inter result set1 set2
     ```
   - **Output**:
     ```sh
     (integer) 2
     ```

### 125. **SUNIONSTORE**
   - **Description**: Computes the union of multiple sets and stores the result in a new set.
   - **Syntax**: `SUNIONSTORE destination key [key ...]`
   - **Example**:
     ```sh
     SUNIONSTORE union result set1 set2
     ```
   - **Output**:
     ```sh
     (integer) 4
     ```

### 126. **SDIFFSTORE**
   - **Description**: Computes the difference of multiple sets and stores the result in a new set.
   - **Syntax**: `SDIFFSTORE destination key [key ...]`
   - **Example**:
     ```sh
     SDIFFSTORE diff result set1 set2
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 127. **ZADD**
   - **Description**: Adds one or more members to a sorted set, or updates their score if they already exist.
   - **Syntax**: `ZADD key score member [score member ...]`
   - **Example**:
     ```sh
     ZADD myzset 1 "one" 2 "two"
     ```
   - **Output**:
     ```sh
     (integer) 2
     ```

### 128. **ZINCRBY**
   - **Description**: Increments the score of a member in a sorted set.
   - **Syntax**: `ZINCRBY key increment member`
   - **Example**:
     ```sh
     ZINCRBY myzset 1 "one"
     ```
   - **Output**:
     ```sh
     "2"
     ```

### 129. **ZRANGE**
   - **Description**: Returns a range of members in a sorted set, by index.
   - **Syntax**: `ZRANGE key start stop [WITHSCORES]`
   - **Example**:
     ```sh
     ZRANGE myzset 0 -1 WITHSCORES
     ```
   - **Output**:
     ```sh
     1) "one"
     2) "2"
     3) "two"
     4) "2"
     ```

### 130. **ZREVRANGE**
   - **Description**: Returns a range of members in a sorted set, by index, with scores ordered from high to low.
   - **Syntax**: `ZREVRANGE key start stop [WITHSCORES]`
   - **Example**:
     ```sh
     ZREVRANGE myzset 0 -1 WITHSCORES
     ```
   - **Output**:
     ```sh
     1) "two"
     2) "2"
     3) "one"
     4) "2"
     ```

### 131. **ZCARD**
   - **Description**: Returns the number of members in a sorted set.
   - **Syntax**: `ZCARD key`
   - **Example**:
     ```sh
     ZCARD myzset
     ```
   - **Output**:
     ```sh
     (integer) 2
     ```

### 132. **ZREM**
   - **Description**: Removes one or more members from a sorted set.
   - **Syntax**: `ZREM key member [member ...]`
   - **Example**:
     ```sh
     ZREM myzset "one"
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 133. **ZPOPMIN**
   - **Description**: Removes and returns the member with the lowest score from a sorted set.
   - **Syntax**: `ZPOPMIN key [count]`
   - **Example**:
     ```sh
     ZPOPMIN myzset
     ```
   - **Output**:
     ```sh
     1) "one"
     2) "2"
     ```

### 134. **ZPOPMAX**
   - **Description**: Removes and returns the member with the highest score from a sorted set.
   - **Syntax**: `ZPOPMAX key [count]`
   - **Example**:
     ```sh
     ZPOPMAX myzset
     ```
   - **Output**:
     ```sh
     1) "two"
     2) "2"
     ```

### 135. **ZMSCORE**
   - **Description**: Returns the scores of one or more members in a sorted set.
   - **Syntax**: `ZMSCORE key member [member ...]`
   - **Example**:
     ```sh
     ZMSCORE myzset "one" "two"
     ```
   - **Output**:
     ```sh
     1) "2"
     2) "2"
     ```

### 136. **ZREMRANGEBYRANK**
   - **Description**: Removes all members in a sorted set within the given rank range.
   - **Syntax**: `ZREMRANGEBYRANK key start stop`
   - **Example**:
     ```sh
     ZREMRANGEBYRANK myzset 0 0
     ```
   - **Output**:
     ```sh
     (integer) 1
    

 

### 137. **ZREMRANGEBYSCORE**
   - **Description**: Removes all members in a sorted set within the given score range.
   - **Syntax**: `ZREMRANGEBYSCORE key min max`
   - **Example**:
     ```sh
     ZREMRANGEBYSCORE myzset 0 1
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 138. **ZRANGEBYSCORE**
   - **Description**: Returns all members in a sorted set with scores within the given range.
   - **Syntax**: `ZRANGEBYSCORE key min max [WITHSCORES] [LIMIT offset count]`
   - **Example**:
     ```sh
     ZRANGEBYSCORE myzset 0 2 WITHSCORES
     ```
   - **Output**:
     ```sh
     1) "one"
     2) "2"
     3) "two"
     4) "2"
     ```

### 139. **ZREVRANGEBYSCORE**
   - **Description**: Returns all members in a sorted set with scores within the given range, ordered from high to low.
   - **Syntax**: `ZREVRANGEBYSCORE key max min [WITHSCORES] [LIMIT offset count]`
   - **Example**:
     ```sh
     ZREVRANGEBYSCORE myzset 2 0 WITHSCORES
     ```
   - **Output**:
     ```sh
     1) "two"
     2) "2"
     3) "one"
     4) "2"
     ```

### 140. **ZRANGEBYLEX**
   - **Description**: Returns all members of a sorted set within the given lexicographical range.
   - **Syntax**: `ZRANGEBYLEX key min max [LIMIT offset count]`
   - **Example**:
     ```sh
     ZRANGEBYLEX myzset [a [z
     ```
   - **Output**:
     ```sh
     1) "a"
     ```

### 141. **ZREVRANGEBYLEX**
   - **Description**: Returns all members of a sorted set within the given lexicographical range, ordered from high to low.
   - **Syntax**: `ZREVRANGEBYLEX key max min [LIMIT offset count]`
   - **Example**:
     ```sh
     ZREVRANGEBYLEX myzset [z [a
     ```
   - **Output**:
     ```sh
     1) "z"
     ```

### 142. **ZINTERSTORE**
   - **Description**: Intersects multiple sorted sets and stores the result in a new sorted set.
   - **Syntax**: `ZINTERSTORE destination numkeys key [key ...]`
   - **Example**:
     ```sh
     ZINTERSTORE inter 2 set1 set2
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 143. **ZUNIONSTORE**
   - **Description**: Unions multiple sorted sets and stores the result in a new sorted set.
   - **Syntax**: `ZUNIONSTORE destination numkeys key [key ...]`
   - **Example**:
     ```sh
     ZUNIONSTORE union 2 set1 set2
     ```
   - **Output**:
     ```sh
     (integer) 3
     ```

### 144. **ZPOPMIN**
   - **Description**: Removes and returns the member with the lowest score from a sorted set.
   - **Syntax**: `ZPOPMIN key [count]`
   - **Example**:
     ```sh
     ZPOPMIN myzset
     ```
   - **Output**:
     ```sh
     1) "one"
     2) "1"
     ```

### 145. **ZPOPMAX**
   - **Description**: Removes and returns the member with the highest score from a sorted set.
   - **Syntax**: `ZPOPMAX key [count]`
   - **Example**:
     ```sh
     ZPOPMAX myzset
     ```
   - **Output**:
     ```sh
     1) "two"
     2) "2"
     ```


### 146. **BGSAVE**
   - **Description**: Asynchronously saves the dataset to disk.
   - **Syntax**: `BGSAVE`
   - **Example**:
     ```sh
     BGSAVE
     ```
   - **Output**:
     ```sh
     OK
     ```

### 147. **BGREWRITEAOF**
   - **Description**: Asynchronously rewrites the append-only file (AOF) to reduce its size.
   - **Syntax**: `BGREWRITEAOF`
   - **Example**:
     ```sh
     BGREWRITEAOF
     ```
   - **Output**:
     ```sh
     OK
     ```

### 148. **LASTSAVE**
   - **Description**: Returns the UNIX timestamp of the last successful save to disk.
   - **Syntax**: `LASTSAVE`
   - **Example**:
     ```sh
     LASTSAVE
     ```
   - **Output**:
     ```sh
     (integer) 1625182325
     ```

### 149. **SHUTDOWN**
   - **Description**: Shuts down the Redis server.
   - **Syntax**: `SHUTDOWN [SAVE|NOSAVE]`
   - **Example**:
     ```sh
     SHUTDOWN SAVE
     ```
   - **Output**:
     ```sh
     OK
     ```

### 150. **INFO**
   - **Description**: Provides information and statistics about the Redis server.
   - **Syntax**: `INFO [section]`
   - **Example**:
     ```sh
     INFO memory
     ```
   - **Output**:
     ```sh
     # Memory
     used_memory:10485760
     used_memory_human:10.00M
     ```

### 151. **FLUSHDB**
   - **Description**: Removes all keys from the currently selected database.
   - **Syntax**: `FLUSHDB`
   - **Example**:
     ```sh
     FLUSHDB
     ```
   - **Output**:
     ```sh
     OK
     ```

### 152. **FLUSHALL**
   - **Description**: Removes all keys from all databases.
   - **Syntax**: `FLUSHALL`
   - **Example**:
     ```sh
     FLUSHALL
     ```
   - **Output**:
     ```sh
     OK
     ```

### 153. **RENAME**
   - **Description**: Renames a key.
   - **Syntax**: `RENAME oldkey newkey`
   - **Example**:
     ```sh
     RENAME oldkey newkey
     ```
   - **Output**:
     ```sh
     OK
     ```

### 154. **RENAMENX**
   - **Description**: Renames a key only if the new key does not already exist.
   - **Syntax**: `RENAMENX oldkey newkey`
   - **Example**:
     ```sh
     RENAMENX oldkey newkey
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 155. **MOVE**
   - **Description**: Moves a key to a different database.
   - **Syntax**: `MOVE key db`
   - **Example**:
     ```sh
     MOVE mykey 1
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 156. **TYPE**
   - **Description**: Returns the type of the value stored at the key.
   - **Syntax**: `TYPE key`
   - **Example**:
     ```sh
     TYPE mykey
     ```
   - **Output**:
     ```sh
     string
     ```

### 157. **TTL**
   - **Description**: Returns the remaining time to live of a key in seconds.
   - **Syntax**: `TTL key`
   - **Example**:
     ```sh
     TTL mykey
     ```
   - **Output**:
     ```sh
     (integer) 120
     ```

### 158. **PTTL**
   - **Description**: Returns the remaining time to live of a key in milliseconds.
   - **Syntax**: `PTTL key`
   - **Example**:
     ```sh
     PTTL mykey
     ```
   - **Output**:
     ```sh
     (integer) 120000
     ```

### 159. **EXPIRE**
   - **Description**: Sets an expiration time on a key in seconds.
   - **Syntax**: `EXPIRE key seconds`
   - **Example**:
     ```sh
     EXPIRE mykey 3600
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 160. **PEXPIRE**
   - **Description**: Sets an expiration time on a key in milliseconds.
   - **Syntax**: `PEXPIRE key milliseconds`
   - **Example**:
     ```sh
     PEXPIRE mykey 60000
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 161. **EXPIREAT**
   - **Description**: Sets an expiration time on a key based on a UNIX timestamp.
   - **Syntax**: `EXPIREAT key timestamp`
   - **Example**:
     ```sh
     EXPIREAT mykey 1625182325
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 162. **PEXPIREAT**
   - **Description**: Sets an expiration time on a key based on a UNIX timestamp in milliseconds.
   - **Syntax**: `PEXPIREAT key milliseconds-timestamp`
   - **Example**:
     ```sh
     PEXPIREAT mykey 1625182325000
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 163. **PERSIST**
   - **Description**: Removes the expiration time from a key.
   - **Syntax**: `PERSIST key`
   - **Example**:
     ```sh
     PERSIST mykey
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 164. **DEBUG SEGFAULT**
   - **Description**: Forces the server to crash for debugging purposes.
   - **Syntax**: `DEBUG SEGFAULT`
   - **Example**:
     ```sh
     DEBUG SEGFAULT
     ```
   - **Output**: The server will crash and restart.

### 165. **SWAPDB**
   - **Description**: Swaps two Redis databases.
   - **Syntax**: `SWAPDB index1 index2`
   - **Example**:
     ```sh
     SWAPDB 0 1
     ```
   - **Output**:
     ```sh
     OK
     ```

### 166. **SUBSCRIBE**
   - **Description**: Subscribes to one or more channels.
   - **Syntax**: `SUBSCRIBE channel [channel ...]`
   - **Example**:
     ```sh
     SUBSCRIBE news
     ```
   - **Output**:
     ```sh
     1) "subscribe"
     2) "news"
     3) (integer) 1
     ```

### 167. **UNSUBSCRIBE**
   - **Description**: Unsubscribes from one or more channels.
   - **Syntax**: `UNSUBSCRIBE channel [channel ...]`
   - **Example**:
     ```sh
     UNSUBSCRIBE news
     ```
   - **Output**:
     ```sh
     1) "unsubscribe"
     2) "news"
     3) (integer) 0
     ```

### 168. **PSUBSCRIBE**
   - **Description**: Subscribes to one or more channels using patterns.
   - **Syntax**: `PSUBSCRIBE pattern [pattern ...]`
   - **Example**:
     ```sh
     PSUBSCRIBE "news.*"
     ```
   - **Output**:
     ```sh
     1) "psubscribe"
     2) "news.*"
     3) (integer) 1
     ```

### 169. **PUNSUBSCRIBE**
   - **Description**: Unsubscribes from one or more channels using patterns.
   - **Syntax**: `PUNSUBSCRIBE pattern [pattern ...]`
   - **Example**:
     ```sh
     PUNSUBSCRIBE "news.*"
     ```
   - **Output**:
     ```sh
     1) "punsubscribe"
     2) "news.*"
     3) (integer) 0
     ```

### 170. **SADD**
   - **Description**: Adds one or more members to a set.
   - **Syntax**: `SADD key member [member ...]`
   - **Example**:
     ```sh
     SADD myset "one" "two"
     ```
   - **Output**:
     ```sh
     (integer) 2
     ```

### 171. **SREM**
   - **Description**: Removes one or more members from a set.
   - **Syntax**: `SREM key member [member ...]`
   - **Example**:
     ```sh
     SREM myset "

one"
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 172. **SMEMBERS**
   - **Description**: Returns all members of a set.
   - **Syntax**: `SMEMBERS key`
   - **Example**:
     ```sh
     SMEMBERS myset
     ```
   - **Output**:
     ```sh
     1) "two"
     ```

### 173. **SISMEMBER**
   - **Description**: Checks if a member exists in a set.
   - **Syntax**: `SISMEMBER key member`
   - **Example**:
     ```sh
     SISMEMBER myset "two"
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 174. **SCARD**
   - **Description**: Returns the number of members in a set.
   - **Syntax**: `SCARD key`
   - **Example**:
     ```sh
     SCARD myset
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 175. **SMOVE**
   - **Description**: Moves a member from one set to another.
   - **Syntax**: `SMOVE source destination member`
   - **Example**:
     ```sh
     SMOVE myset1 myset2 "two"
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 176. **SPOP**
   - **Description**: Removes and returns a random member from a set.
   - **Syntax**: `SPOP key [count]`
   - **Example**:
     ```sh
     SPOP myset
     ```
   - **Output**:
     ```sh
     "two"
     ```

### 177. **SRANDMEMBER**
   - **Description**: Returns a random member from a set without removing it.
   - **Syntax**: `SRANDMEMBER key [count]`
   - **Example**:
     ```sh
     SRANDMEMBER myset
     ```
   - **Output**:
     ```sh
     "one"
     ```

### 178. **ZADD**
   - **Description**: Adds one or more members to a sorted set or updates their scores if they already exist.
   - **Syntax**: `ZADD key score member [score member ...]`
   - **Example**:
     ```sh
     ZADD myzset 1 "one" 2 "two"
     ```
   - **Output**:
     ```sh
     (integer) 2
     ```

### 179. **ZINCRBY**
   - **Description**: Increments the score of a member in a sorted set.
   - **Syntax**: `ZINCRBY key increment member`
   - **Example**:
     ```sh
     ZINCRBY myzset 1 "one"
     ```
   - **Output**:
     ```sh
     "2"
     ```

### 180. **ZRANGE**
   - **Description**: Returns a range of members in a sorted set, by index.
   - **Syntax**: `ZRANGE key start stop [WITHSCORES]`
   - **Example**:
     ```sh
     ZRANGE myzset 0 -1 WITHSCORES
     ```
   - **Output**:
     ```sh
     1) "one"
     2) "2"
     3) "two"
     4) "2"
     ```

### 181. **ZREVRANGE**
   - **Description**: Returns a range of members in a sorted set, by index, with scores ordered from high to low.
   - **Syntax**: `ZREVRANGE key start stop [WITHSCORES]`
   - **Example**:
     ```sh
     ZREVRANGE myzset 0 -1 WITHSCORES
     ```
   - **Output**:
     ```sh
     1) "two"
     2) "2"
     3) "one"
     4) "2"
     ```

### 182. **ZCARD**
   - **Description**: Returns the number of members in a sorted set.
   - **Syntax**: `ZCARD key`
   - **Example**:
     ```sh
     ZCARD myzset
     ```
   - **Output**:
     ```sh
     (integer) 2
     ```

### 183. **ZREM**
   - **Description**: Removes one or more members from a sorted set.
   - **Syntax**: `ZREM key member [member ...]`
   - **Example**:
     ```sh
     ZREM myzset "one"
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 184. **ZPOPMIN**
   - **Description**: Removes and returns the member with the lowest score from a sorted set.
   - **Syntax**: `ZPOPMIN key [count]`
   - **Example**:
     ```sh
     ZPOPMIN myzset
     ```
   - **Output**:
     ```sh
     1) "one"
     2) "2"
     ```

### 185. **ZPOPMAX**
   - **Description**: Removes and returns the member with the highest score from a sorted set.
   - **Syntax**: `ZPOPMAX key [count]`
   - **Example**:
     ```sh
     ZPOPMAX myzset
     ```
   - **Output**:
     ```sh
     1) "two"
     2) "2"
     ```

### 186. **ZMSCORE**
   - **Description**: Returns the scores of one or more members in a sorted set.
   - **Syntax**: `ZMSCORE key member [member ...]`
   - **Example**:
     ```sh
     ZMSCORE myzset "one" "two"
     ```
   - **Output**:
     ```sh
     1) "2"
     2) "2"
     ```

### 187. **ZREMRANGEBYRANK**
   - **Description**: Removes all members in a sorted set within the given rank range.
   - **Syntax**: `ZREMRANGEBYRANK key start stop`
   - **Example**:
     ```sh
     ZREMRANGEBYRANK myzset 0 0
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 188. **ZREMRANGEBYSCORE**
   - **Description**: Removes all members in a sorted set within the given score range.
   - **Syntax**: `ZREMRANGEBYSCORE key min max`
   - **Example**:
     ```sh
     ZREMRANGEBYSCORE myzset 0 1
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 189. **ZRANGEBYSCORE**
   - **Description**: Returns all members in a sorted set with scores within the given range.
   - **Syntax**: `ZRANGEBYSCORE key min max [WITHSCORES] [LIMIT offset count]`
   - **Example**:
     ```sh
     ZRANGEBYSCORE myzset 0 2 WITHSCORES
     ```
   - **Output**:
     ```sh
     1) "one"
     2) "2"
     3) "two"
     4) "2"
     ```

### 190. **ZREVRANGEBYSCORE**
   - **Description**: Returns all members in a sorted set with scores within the given range, ordered from high to low.
   - **Syntax**: `ZREVRANGEBYSCORE key max min [WITHSCORES] [LIMIT offset count]`
   - **Example**:
     ```sh
     ZREVRANGEBYSCORE myzset 2 0 WITHSCORES
     ```
   - **Output**:
     ```sh
     1) "two"
     2) "2"
     3) "one"
     4) "2"
     ```

### 191. **ZRANGEBYLEX**
   - **Description**: Returns all members of a sorted set within the given lexicographical range.
   - **Syntax**: `ZRANGEBYLEX key min max [LIMIT offset count]`
   - **Example**:
     ```sh
     ZRANGEBYLEX myzset [a [z
     ```
   - **Output**:
     ```sh
     1) "a"
     ```

### 192. **ZREVRANGEBYLEX**
   - **Description**: Returns all members of a sorted set within the given lexicographical range, ordered from high to low.
   - **Syntax**: `ZREVRANGEBYLEX key max min [LIMIT offset count]`
   - **Example**:
     ```sh
     ZREVRANGEBYLEX myzset [z [a
     ```
   - **Output**:
     ```sh
     1) "z"
     ```

### 193. **ZINTERSTORE**
   - **Description**: Intersects multiple sorted sets and stores

 the result in a new sorted set.
   - **Syntax**: `ZINTERSTORE destination numkeys key [key ...]`
   - **Example**:
     ```sh
     ZINTERSTORE inter 2 set1 set2
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

### 194. **ZUNIONSTORE**
   - **Description**: Unions multiple sorted sets and stores the result in a new sorted set.
   - **Syntax**: `ZUNIONSTORE destination numkeys key [key ...]`
   - **Example**:
     ```sh
     ZUNIONSTORE union 2 set1 set2
     ```
   - **Output**:
     ```sh
     (integer) 3
     ```

### 195. **ZPOPMIN**
   - **Description**: Removes and returns the member with the lowest score from a sorted set.
   - **Syntax**: `ZPOPMIN key [count]`
   - **Example**:
     ```sh
     ZPOPMIN myzset
     ```
   - **Output**:
     ```sh
     1) "one"
     2) "1"
     ```

### 196. **ZPOPMAX**
   - **Description**: Removes and returns the member with the highest score from a sorted set.
   - **Syntax**: `ZPOPMAX key [count]`
   - **Example**:
     ```sh
     ZPOPMAX myzset
     ```
   - **Output**:
     ```sh
     1) "two"
     2) "2"
     ```

---

### **Advanced Commands**

#### **1. **BITFIELD**
   - **Description**: Manipulates and queries a string representing a binary field.
   - **Syntax**: `BITFIELD key [GET type offset] [SET type offset value] [INCRBY type offset increment]`
   - **Example**:
     ```sh
     BITFIELD mykey SET u4 0 15
     BITFIELD mykey GET u4 0
     ```
   - **Output**:
     ```sh
     1) (integer) 15
     ```

#### **2. **BITOP**
   - **Description**: Performs bitwise operations between multiple strings and stores the result in the destination key.
   - **Syntax**: `BITOP operation destkey key [key ...]`
   - **Example**:
     ```sh
     BITOP AND destkey key1 key2
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

#### **3. **HSETNX**
   - **Description**: Sets the value of a field in a hash if the field does not exist.
   - **Syntax**: `HSETNX key field value`
   - **Example**:
     ```sh
     HSETNX myhash field1 value1
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

#### **4. **HINCRBYFLOAT**
   - **Description**: Increments the float value of a field in a hash.
   - **Syntax**: `HINCRBYFLOAT key field increment`
   - **Example**:
     ```sh
     HINCRBYFLOAT myhash field1 1.5
     ```
   - **Output**:
     ```sh
     "10.5"
     ```

#### **5. **GEOADD**
   - **Description**: Adds geospatial items (longitude, latitude) to a geospatial index.
   - **Syntax**: `GEOADD key longitude latitude member`
   - **Example**:
     ```sh
     GEOADD mygeo 13.361389 38.115556 "Palermo"
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

#### **6. **GEORADIUS**
   - **Description**: Returns members of a geospatial index within a given radius.
   - **Syntax**: `GEORADIUS key longitude latitude radius m [WITHDIST|WITHCOORD|WITHHASH|WITHPOINTER]`
   - **Example**:
     ```sh
     GEORADIUS mygeo 15 37 200 km
     ```
   - **Output**:
     ```sh
     1) "Palermo"
     ```

#### **7. **GEOHASH**
   - **Description**: Returns the geohash representation of members in a geospatial index.
   - **Syntax**: `GEOHASH key member [member ...]`
   - **Example**:
     ```sh
     GEOHASH mygeo "Palermo"
     ```
   - **Output**:
     ```sh
     1) "s6b9n"
     ```

#### **8. **GEOADD**
   - **Description**: Adds geospatial items (longitude, latitude) to a geospatial index.
   - **Syntax**: `GEOADD key longitude latitude member`
   - **Example**:
     ```sh
     GEOADD mygeo 13.361389 38.115556 "Palermo"
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

#### **9. **ZDIFFSTORE**
   - **Description**: Subtracts multiple sorted sets and stores the resulting set in a new key.
   - **Syntax**: `ZDIFFSTORE destination numkeys key [key ...]`
   - **Example**:
     ```sh
     ZDIFFSTORE result 2 set1 set2
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

#### **10. **ZUNIONSTORE**
   - **Description**: Unions multiple sorted sets and stores the resulting set in a new key.
   - **Syntax**: `ZUNIONSTORE destination numkeys key [key ...] [WEIGHTS weight [weight ...]] [AGGREGATE SUM|MIN|MAX]`
   - **Example**:
     ```sh
     ZUNIONSTORE result 2 set1 set2 WEIGHTS 2 3 AGGREGATE MAX
     ```
   - **Output**:
     ```sh
     (integer) 3
     ```

### **Advanced Usage Patterns**

#### **1. **Cluster Mode Commands**
   - **CLUSTER NODES**: Returns information about the cluster nodes.
     ```sh
     CLUSTER NODES
     ```
   - **CLUSTER INFO**: Provides information about the cluster status.
     ```sh
     CLUSTER INFO
     ```

#### **2. **Replication Commands**
   - **SLAVEOF**: Configures the current server as a slave of another server.
     ```sh
     SLAVEOF <masterip> <masterport>
     ```
   - **PSYNC**: Manages partial resynchronization between master and slave.
     ```sh
     PSYNC replication-id offset
     ```

#### **3. **Sentinel Commands**
   - **SENTINEL MONITOR**: Adds a new master to be monitored by Sentinel.
     ```sh
     SENTINEL MONITOR mymaster <ip> <port> <quorum>
     ```
   - **SENTINEL FAILOVER**: Forces a failover of the specified master.
     ```sh
     SENTINEL FAILOVER mymaster
     ```

#### **4. **Lua Scripting Commands**
   - **EVAL**: Executes a Lua script on the server.
     ```sh
     EVAL "return redis.call('SET', 'key', 'value')" 0
     ```
   - **EVALSHA**: Executes a Lua script using its SHA1 digest.
     ```sh
     EVALSHA <sha1> 0
     ```

#### **5. **Transactional Commands**
   - **MULTI**: Starts a transaction block.
     ```sh
     MULTI
     ```
   - **EXEC**: Executes all commands issued after MULTI.
     ```sh
     EXEC
     ```
   - **WATCH**: Monitors one or more keys for changes.
     ```sh
     WATCH key1 key2
     ```

#### **6. **Memory Optimization Commands**
   - **MEMORY USAGE**: Returns the memory usage of a key.
     ```sh
     MEMORY USAGE key
     ```
   - **MEMORY PURGE**: Purges all cached memory.
     ```sh
     MEMORY PURGE
     ```

### **Advanced Usage Scenarios**

#### **1. **Pub/Sub Messaging**
   - **PUBLISH**: Publishes a message to a channel.
     ```sh
     PUBLISH channel "message"
     ```
   - **SUBSCRIBE**: Subscribes to one or more channels.
     ```sh
     SUBSCRIBE channel
     ```

#### **2. **Streams**
   - **XADD**: Adds a new entry to a stream.
     ```sh
     XADD mystream * field1 value1 field2 value2
     ```
   - **XREAD**: Reads data from one or multiple streams.
     ```sh
     XREAD COUNT 2 STREAMS mystream 0
     ```
   - **XTRIM**: Trims a stream to a certain length.
     ```sh
     XTRIM mystream MAXLEN 1000
     ```

#### **3. **HyperLogLog**
   - **PFADD**: Adds elements to a HyperLogLog data structure.
     ```sh
     PFADD myhyperloglog element1 element2
     ```
   - **PFCOUNT**: Returns the approximated cardinality of a HyperLogLog.
     ```sh
     PFCOUNT myhyperloglog
     ```

#### **4. **Bitmap Operations**
   - **SETBIT**: Sets or clears the bit at the specified offset.
     ```sh
     SETBIT mybitmap 7 1
     ```
   - **GETBIT**: Gets the bit value at the specified offset.
     ```sh
     GETBIT mybitmap 7
     ```

### **Advanced Configuration and Management**

#### **1. **Redis Configuration**
   - **CONFIG GET**: Gets the value of a configuration parameter.
     ```sh
     CONFIG GET maxmemory
     ```
   - **CONFIG SET**: Sets the value of a configuration parameter.
     ```sh
     CONFIG SET maxmemory 100mb
     ```

#### **2. **Cluster Management**
   - **CLUSTER MEET**: Forces a node to join the cluster.
     ```sh
     CLUSTER MEET <node-ip> <node-port>
     ```

### **Advanced Commands and Concepts**

#### **1. **PERSISTENT Storage**
   - **RDB (Redis Database Backup)**: Snapshotting of Redis data to disk.
     - **SAVE**: Saves the database to disk synchronously.
       ```sh
       SAVE
       ```
     - **BGSAVE**: Saves the database to disk asynchronously.
       ```sh
       BGSAVE
       ```

#### **2. **AOF (Append-

Only File)**
   - **BGREWRITEAOF**: Rewrites the AOF file in the background.
     ```sh
     BGREWRITEAOF
     ```

#### **3. **Redis Modules**
   - **MODULE LIST**: Lists all loaded modules.
     ```sh
     MODULE LIST
     ```
   - **MODULE LOAD**: Loads a new module.
     ```sh
     MODULE LOAD /path/to/module.so
     ```

#### **4. **Keyspace Notifications**
   - **CONFIG SET notify-keyspace-events**: Configures keyspace notifications.
     ```sh
     CONFIG SET notify-keyspace-events KEA
     ```

### **Commands for Monitoring and Debugging**

#### **1. **INFO**
   - **Description**: Provides information and statistics about the server.
   - **Syntax**: `INFO [section]`
   - **Example**:
     ```sh
     INFO MEMORY
     ```

#### **2. **MONITOR**
   - **Description**: Streams all commands processed by the Redis server.
   - **Syntax**: `MONITOR`
   - **Example**:
     ```sh
     MONITOR
     ```

#### **3. **SLOWLOG**
   - **Description**: Manages the slow queries log.
   - **Syntax**:
     - **SLOWLOG GET**: Gets the slow logs.
       ```sh
       SLOWLOG GET 10
       ```
     - **SLOWLOG LEN**: Returns the length of the slow logs.
       ```sh
       SLOWLOG LEN
       ```

#### **4. **DEBUG**
   - **Description**: Provides low-level debugging commands.
   - **Syntax**:
     - **DEBUG OBJECT**: Returns information about an object.
       ```sh
       DEBUG OBJECT key
       ```

#### **5. **CLIENT**
   - **Description**: Manages client connections.
   - **Syntax**:
     - **CLIENT LIST**: Lists connected clients.
       ```sh
       CLIENT LIST
       ```


Certainly! Here’s an expanded look into even more advanced Redis commands, usage scenarios, and configurations. We’ll cover additional complex commands, scripting, performance tuning, and other advanced features.

### **Continue Advanced Commands**

#### **1. **XTRIM**
   - **Description**: Trims a stream to a specified length or maximum length.
   - **Syntax**: `XTRIM key [MAXLEN|MINID] [~] count`
   - **Example**:
     ```sh
     XTRIM mystream MAXLEN 1000
     ```
   - **Output**:
     ```sh
     (integer) 100
     ```

#### **2. **XADD**
   - **Description**: Adds a new entry to a stream or appends to an existing one.
   - **Syntax**: `XADD key id field value [field value ...]`
   - **Example**:
     ```sh
     XADD mystream * field1 value1 field2 value2
     ```
   - **Output**:
     ```sh
     "1681797641611-0"
     ```

#### **3. **XLEN**
   - **Description**: Returns the length of a stream.
   - **Syntax**: `XLEN key`
   - **Example**:
     ```sh
     XLEN mystream
     ```
   - **Output**:
     ```sh
     (integer) 100
     ```

#### **4. **XRANGE**
   - **Description**: Returns a range of elements from a stream.
   - **Syntax**: `XRANGE key start end [COUNT count]`
   - **Example**:
     ```sh
     XRANGE mystream - + COUNT 10
     ```
   - **Output**:
     ```sh
     1) 1) "1681797641611-0"
        2) 1) "field1"
           2) "value1"
           3) "field2"
           4) "value2"
     ```

#### **5. **XREVRANGE**
   - **Description**: Returns a range of elements from a stream in reverse order.
   - **Syntax**: `XREVRANGE key end start [COUNT count]`
   - **Example**:
     ```sh
     XREVRANGE mystream + - COUNT 10
     ```
   - **Output**:
     ```sh
     1) 1) "1681797641611-0"
        2) 1) "field1"
           2) "value1"
           3) "field2"
           4) "value2"
     ```

#### **6. **XACK**
   - **Description**: Acknowledges one or more messages as processed in a stream.
   - **Syntax**: `XACK key group id [id ...]`
   - **Example**:
     ```sh
     XACK mystream mygroup 1681797641611-0
     ```
   - **Output**:
     ```sh
     (integer) 1
     ```

#### **7. **XGROUP**
   - **Description**: Manages stream consumer groups.
   - **Syntax**:
     - **CREATE**: Creates a new consumer group.
       ```sh
       XGROUP CREATE key groupname id [MKSTREAM]
       ```
     - **SETID**: Sets the ID of the consumer group.
       ```sh
       XGROUP SETID key groupname id
       ```
   - **Example**:
     ```sh
     XGROUP CREATE mystream mygroup 0
     ```
   - **Output**:
     ```sh
     OK
     ```

#### **8. **XREADGROUP**
   - **Description**: Reads messages from a stream as part of a consumer group.
   - **Syntax**: `XREADGROUP GROUP groupname consumername [BLOCK milliseconds] [COUNT count] STREAMS key [key ...] id [id ...]`
   - **Example**:
     ```sh
     XREADGROUP GROUP mygroup consumer1 COUNT 10 STREAMS mystream >
     ```
   - **Output**:
     ```sh
     1) 1) "mystream"
        2) 1) 1) "1681797641611-0"
              2) 1) "field1"
                 2) "value1"
              2) 1) "field2"
                 2) "value2"
     ```

### **Advanced Usage Scenarios**

#### **1. **Redis Streams**
   - **Message Queues**: Use Redis Streams as a powerful message queue with the ability to handle large volumes of messages.
   - **Event Sourcing**: Utilize streams to record all events in an application for auditing or replay purposes.

#### **2. **Redis HyperLogLog**
   - **Cardinality Estimation**: Perfect for scenarios requiring approximate counting of unique items with minimal memory usage, such as counting unique visitors to a site.

#### **3. **Redis Geospatial Indexing**
   - **Location-based Services**: Ideal for applications that need to query locations within a certain distance, like finding nearby restaurants or users.

#### **4. **Redis Pub/Sub**
   - **Real-Time Notifications**: Utilize Pub/Sub for real-time messaging and notifications systems where you need instant data updates.

### **Performance Tuning**

#### **1. **Memory Management**
   - **maxmemory**: Configure the maximum amount of memory Redis can use. When the limit is reached, Redis will start evicting keys according to the configured policy.
     ```sh
     CONFIG SET maxmemory 2gb
     ```

   - **maxmemory-policy**: Sets the policy for handling keys when `maxmemory` is reached. Options include `noeviction`, `allkeys-lru`, `allkeys-random`, `volatile-lru`, `volatile-random`, and `volatile-ttl`.
     ```sh
     CONFIG SET maxmemory-policy allkeys-lru
     ```

#### **2. **Persistence Configuration**
   - **RDB Persistence**: Configure snapshotting frequency with `SAVE` and `BGSAVE`.
     ```sh
     SAVE
     BGSAVE
     ```
   - **AOF Persistence**: Configure AOF rewrite and append policies.
     ```sh
     CONFIG SET appendonly yes
     CONFIG SET appendfsync everysec
     ```

#### **3. **Cluster Performance**
   - **Cluster Sharding**: Distribute data across multiple nodes to balance the load.
   - **Replication**: Use replicas to offload read operations and increase fault tolerance.

### **Advanced Redis Configuration**

#### **1. **Redis Sentinel**
   - **Description**: Provides high availability and monitoring.
   - **Syntax**:
     - **SENTINEL MONITOR**: Monitors a master instance.
       ```sh
       SENTINEL MONITOR mymaster 127.0.0.1 6379 2
       ```
     - **SENTINEL FAILOVER**: Forces a failover of the monitored master.
       ```sh
       SENTINEL FAILOVER mymaster
       ```

#### **2. **Redis Cluster**
   - **Description**: Enables horizontal scaling of Redis.
   - **Syntax**:
     - **CLUSTER MEET**: Adds a new node to the cluster.
       ```sh
       CLUSTER MEET <node-ip> <node-port>
       ```
     - **CLUSTER FORGET**: Removes a node from the cluster.
       ```sh
       CLUSTER FORGET <node-id>
       ```

### **Additional Redis Modules**

#### **1. **RedisGraph**
   - **Description**: Adds graph database functionality to Redis.
   - **Syntax**:
     - **GRAPH.QUERY**: Executes a graph query.
       ```sh
       GRAPH.QUERY mygraph "MATCH (n) RETURN n"
       ```

#### **2. **RedisJSON**
   - **Description**: Provides native JSON support in Redis.
   - **Syntax**:
     - **JSON.SET**: Sets a JSON value.
       ```sh
       JSON.SET myjson . '{"name":"John"}'
       ```
     - **JSON.GET**: Gets a JSON value.
       ```sh
       JSON.GET myjson
       ```

#### **3. **RedisTimeSeries**
   - **Description**: Provides time series data management.
   - **Syntax**:
     - **TS.CREATE**: Creates a time series.
       ```sh
       TS.CREATE myts
       ```
     - **TS.ADD**: Adds data to the time series.
       ```sh
       TS.ADD myts 1625495400 25.6
       ```

### **Debugging and Monitoring**

#### **1. **Redis Debugging**
   - **DEBUG OBJECT**: Returns low-level information about a key.
     ```sh
     DEBUG OBJECT key
     ```

#### **2. **Redis Monitoring**
   - **MONITOR**: Continuously streams all commands received by the Redis server.
     ```sh
     MONITOR
     ```

   - **SLOWLOG**: Provides information about slow queries.
     ```sh
     SLOWLOG GET 10
     ```

   - **INFO**: Provides various statistics about the Redis server.
     ```sh
     INFO MEMORY
     ```

#### **3. **Keyspace Notifications**
   - **CONFIG SET notify-keyspace-events**: Configures notifications for keyspace events.
     ```sh
     CONFIG SET notify-keyspace-events KEA
     ```
