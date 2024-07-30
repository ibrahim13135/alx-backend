Redis Data Integration (RDI) is a tool designed to help Redis customers sync Redis Enterprise with live data from slower disk-based databases. The goal is to meet the speed and scale requirements of read queries, save resources and time in building data pipelines, and reduce the total cost of ownership by saving on expensive database read replicas.

### RDI Scenarios

RDI supports two primary scenarios:

#### 1. Ingest Scenario

In this scenario, RDI mirrors the primary database of an application to Redis using a change data capture (CDC) tool. The data from the database is transformed into Redis models and types. This is useful when the primary database cannot handle the performance and scalability requirements for read queries. By offloading read queries to Redis, applications can achieve higher performance and scalability.

**Note:**
- Ingest is supported with Redis database or CRDB (Active Active Replication) targets.

#### Example of Ingest Scenario

Let's say you have a MySQL database that is too slow to handle the volume of read queries your application generates. You can set up RDI to mirror the MySQL database to Redis:

1. **Setup RDI with Debezium**: Use Debezium to capture changes from MySQL.
2. **Transform Data**: RDI transforms MySQL data into Redis-compatible formats.
3. **Ingest into Redis**: The transformed data is ingested into Redis.

#### 2. Write-Behind Scenario (Preview)

In this scenario, RDI applies data changes made in Redis to one or more downstream data stores. It maps and transforms Redis data models to match the models required by the downstream data stores. This is useful for applications that require fast writes and reads for some queries but need to share data with other downstream services.

**Note:**
- Write-behind is not supported with CRDB (Active Active Replication).

#### Example of Write-Behind Scenario

Consider an application where fast writes are crucial, and you are using Redis for its speed. However, you need to propagate these changes to a SQL Server for reporting purposes:

1. **Write Changes to Redis**: The application writes changes to Redis.
2. **Setup RDI**: Configure RDI to capture changes from Redis.
3. **Transform Data**: RDI transforms the Redis data to match SQL Server's schema.
4. **Propagate to SQL Server**: The transformed data is then applied to SQL Server.

### Supported Sources (Ingest)

RDI supports the following database sources using Debezium Server connectors:

| Database                | Versions           |
|-------------------------|--------------------|
| Oracle                  | 12c, 19c, 21c      |
| MariaDB                 | >= 10.5            |
| MySQL                   | 5.7, 8.0.x         |
| Postgres                | 10, 11, 12, 13, 14, 15 |
| SQL Server              | 2017, 2019         |
| Google Cloud SQL MySQL  | 8.0                |
| Google Cloud SQL Postgres | 15               |
| Google Cloud SQL SQL Server | 2019          |
| Google Cloud AlloyDB for PostgreSQL |        |

### Supported Targets (Write-Behind)

RDI supports the following database targets for the write-behind scenario:

- Oracle
- MariaDB
- MySQL
- Postgres
- SQL Server
- Cassandra

### Features

RDI is an enterprise-grade product with a robust set of features:

#### Resiliency, High Availability, and Data Delivery Guarantees

- **At Least Once Guarantee**: Ensures data is delivered at least once, end to end.
- **Data Replication**: Data in transit is replicated to a replica shard.
- **Data Persistence**: Uses Redis AOF (Append Only File) for persistence.
- **Back-Pressure Mechanism**: Prevents cascading failures by managing load.
- **Reconnect on Failure and Write Retries**: Ensures reliable data delivery.

#### Developer Tools and Data Transformation

- **Declarative Data Filtering, Mapping, and Transformations**: Allows customization of data transformations.
- **Support for SQL and JMESPath Expressions**: Facilitates complex data transformations.
- **Additional JMESPath Custom Functions**: Simplifies transformation expressions.
- **Transformation Jobs Validation**: Ensures correctness of transformation jobs.
- **Zero Downtime Pipeline Reconfiguration**: Allows updates without downtime.
- **Hard Failures Routing**: Routes problematic data to a dead-letter queue for troubleshooting.
- **Trace Tool**: Helps in tracing and debugging data flows.

#### Operator Tools and Lifecycle Management

- **CLI with Built-in Help and Validations**: Command-line interface for easy management.
- **Installation Using CLI**: Simplifies setup.
- **Zero Downtime Upgrade of RDI**: Allows updates without disrupting operations.
- **Status Tool for Health and Data Provenance**: Monitors system health and data lineage.
- **Monitoring Using Prometheus and Grafana**: Provides detailed monitoring and visualization.

### Example Output

Let's consider an example of the Ingest scenario:

1. **Initial Data in MySQL**:
   ```sql
   CREATE TABLE users (
       id INT PRIMARY KEY,
       name VARCHAR(100),
       email VARCHAR(100)
   );

   INSERT INTO users (id, name, email) VALUES (1, 'Alice', 'alice@example.com');
   ```

2. **RDI Configuration**:
   - Set up Debezium to capture changes from the `users` table.
   - Configure RDI to transform and ingest data into Redis.

3. **Data in Redis**:
   ```redis
   HMSET user:1 id 1 name Alice email alice@example.com
   ```

4. **Application Querying Redis**:
   ```redis
   HGETALL user:1
   ```

   **Output**:
   ```
   1) "id"
   2) "1"
   3) "name"
   4) "Alice"
   5) "email"
   6) "alice@example.com"
   ```

In this example, read queries are offloaded to Redis, improving performance and scalability.

For detailed guides on the architectures of Ingest and Write-Behind scenarios, you can refer to the official Redis documentation.



----


### Node-Redis

Node-Redis is a modern, high-performance Redis client for Node.js. It provides a simple and intuitive API for interacting with Redis, making it easy to integrate Redis into your Node.js applications.

### Installation

To get started with Node-Redis, you need to have a running Redis server. You can start a Redis server using Docker with the following command:

```sh
docker run -p 6379:6379 -it redis/redis-stack-server:latest
```

Then, install the Node-Redis package using npm:

```sh
npm install redis
```

If you have an existing codebase, make sure to check the migration guide for any necessary changes.

### Basic Usage

Here is a basic example of how to use Node-Redis:

```javascript
import { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => console.log('Redis Client Error', err));

await client.connect();

await client.set('key', 'value');
const value = await client.get('key');
console.log(value); // Outputs: value

await client.disconnect();
```

This example connects to a Redis server running on `localhost` on port `6379`, sets a key-value pair, retrieves the value, and then disconnects from the server.

### Connecting to a Different Host or Port

You can connect to a different host or port using a connection string:

```javascript
createClient({
  url: 'redis://alice:foobared@awesome.redis.server:6380'
});
```

You can also use discrete parameters, UNIX sockets, and TLS to connect. Details can be found in the client configuration guide.

### Checking Connection Status

To check if the client is connected and ready to send commands, use `client.isReady`:

```javascript
if (client.isReady) {
  console.log('Client is ready to send commands');
}
```

`client.isOpen` is also available to check if the client's underlying socket is open.

### Redis Commands

Node-Redis supports all Redis commands, which can be used in their raw form (e.g., `HSET`, `HGETALL`) or in a friendlier camel-cased form (e.g., `hSet`, `hGetAll`):

```javascript
// Raw Redis commands
await client.HSET('key', 'field', 'value');
await client.HGETALL('key');

// Friendly JavaScript commands
await client.hSet('key', 'field', 'value');
await client.hGetAll('key');
```

### Command Modifiers

Modifiers can be specified using a JavaScript object:

```javascript
await client.set('key', 'value', {
  EX: 10, // Expiration time in seconds
  NX: true // Only set the key if it does not already exist
});
```

### Transforming Replies

Replies are transformed into useful data structures:

```javascript
await client.hGetAll('key'); // { field1: 'value1', field2: 'value2' }
await client.hVals('key'); // ['value1', 'value2']
```

### Using Buffers

Buffers are supported as well:

```javascript
await client.hSet('key', 'field', Buffer.from('value')); // 'OK'
await client.hGetAll(
  commandOptions({ returnBuffers: true }),
  'key'
); // { field: <Buffer 76 61 6c 75 65> }
```

### Unsupported Redis Commands

For commands not natively supported by Node-Redis, use `.sendCommand()`:

```javascript
await client.sendCommand(['SET', 'key', 'value', 'NX']); // 'OK'
await client.sendCommand(['HGETALL', 'key']); // ['key1', 'field1', 'key2', 'field2']
```

### Transactions (Multi/Exec)

Start a transaction with `.multi()`, chain your commands, and then call `.exec()`:

```javascript
await client.set('another-key', 'another-value');

const [setKeyReply, otherKeyValue] = await client
  .multi()
  .set('key', 'value')
  .get('another-key')
  .exec(); // ['OK', 'another-value']
```

You can also watch keys with `.watch()` to abort a transaction if any watched keys change.

### Blocking Commands

Blocking commands can be run on a new connection using the `isolated` option. The new connection is closed once the command's promise is fulfilled:

```javascript
import { commandOptions } from 'redis';

const blPopPromise = client.blPop(
  commandOptions({ isolated: true }),
  'key',
  0
);

await client.lPush('key', ['1', '2']);

await blPopPromise; // '2'
```

### Packages

Node-Redis offers several packages for different Redis modules:

| Name               | Description               | Downloads | Version | Docs                        |
|--------------------|---------------------------|-----------|---------|-----------------------------|
| redis              |                           | Downloads | Version |                             |
| @redis/client      |                           | Downloads | Version | [Docs](#)                   |
| @redis/bloom       | Redis Bloom commands      | Downloads | Version | [Docs](#)                   |
| @redis/graph       | Redis Graph commands      | Downloads | Version | [Docs](#)                   |
| @redis/json        | Redis JSON commands       | Downloads | Version | [Docs](#)                   |
| @redis/search      | RediSearch commands       | Downloads | Version | [Docs](#)                   |
| @redis/time-series | Redis Time-Series commands| Downloads | Version | [Docs](#)                   |

In version 4.1.0, subpackages moved from `@node-redis` to `@redis`. If you use subpackages directly, update to the new scope.

### Resources

- [Redis University](https://university.redis.com/): Learn Redis for free.
- [Redis Launchpad](https://launchpad.redis.com/): Build faster with Redis.
- [Redis Cloud](https://redis.com/cloud/): Try Redis Cloud.
- [Developer Tutorials](https://redis.com/developers/): Dive into tutorials.
- [Redis Community](https://redis.com/community/): Join the community.
- [Redis Careers](https://redis.com/careers/): Work at Redis.

By leveraging Node-Redis, you can efficiently manage Redis data and integrate Redis functionalities into your Node.js applications, enhancing performance and scalability.


---

### Pub/Sub

**Pub/Sub** (Publish/Subscribe) is a messaging pattern where publishers send messages to channels and subscribers receive messages from channels. Node-Redis supports Pub/Sub functionality, allowing you to create real-time applications that respond to events.

#### Example

1. **Publisher**: Sends a message to a channel.

```javascript
import { createClient } from 'redis';

async function publisher() {
  const client = createClient();
  await client.connect();

  await client.publish('channel', 'Hello, Redis!');
  await client.disconnect();
}

publisher();
```

2. **Subscriber**: Listens for messages on a channel.

```javascript
import { createClient } from 'redis';

async function subscriber() {
  const client = createClient();
  await client.connect();

  await client.subscribe('channel', (message) => {
    console.log('Received message:', message);
  });
}

subscriber();
```

**Output**:

```sh
Received message: Hello, Redis!
```

### Scan Iterator

Node-Redis supports scanning keys using async iterators, making it easy to iterate over keys and perform operations on them.

#### Example

1. **SCAN**: Iterating over keys in the database.

```javascript
import { createClient } from 'redis';

async function scanKeys() {
  const client = createClient();
  await client.connect();

  await client.set('key1', 'value1');
  await client.set('key2', 'value2');

  for await (const key of client.scanIterator()) {
    const value = await client.get(key);
    console.log(key, value);
  }

  await client.disconnect();
}

scanKeys();
```

**Output**:

```sh
key1 value1
key2 value2
```

### Programmability

Redis provides a programming interface that allows you to execute code on the Redis server. This is useful for custom logic and complex operations.

#### Functions

Here’s an example of registering and using a Redis function:

1. **Registering the Function**:

```lua
#!lua name=library

redis.register_function {
  function_name = 'add',
  callback = function(keys, args) return redis.call('GET', keys[1]) + args[1] end,
  flags = { 'no-writes' }
}
```

Load the function using `redis-cli`:

```sh
FUNCTION LOAD "#!lua name=library\nredis.register_function{function_name=\"add\", callback=function(keys, args) return redis.call('GET', keys[1])+args[1] end, flags={\"no-writes\"}}"
```

2. **Using the Function in Node-Redis**:

```javascript
import { createClient } from 'redis';

const client = createClient({
  functions: {
    library: {
      add: {
        NUMBER_OF_KEYS: 1,
        transformArguments(key, toAdd) {
          return [key, toAdd.toString()];
        },
        transformReply(reply) {
          return reply;
        }
      }
    }
  }
});

async function useFunction() {
  await client.connect();

  await client.set('key', '17');
  const result = await client.library.add('key', 25); // 42
  console.log(result);

  await client.disconnect();
}

useFunction();
```

**Output**:

```sh
42
```

### Lua Scripts

Lua scripts allow you to run custom logic on the Redis server.

#### Example

1. **Define and Use a Lua Script in Node-Redis**:

```javascript
import { createClient, defineScript } from 'redis';

const client = createClient({
  scripts: {
    add: defineScript({
      NUMBER_OF_KEYS: 1,
      SCRIPT: 'return redis.call("GET", KEYS[1]) + ARGV[1];',
      transformArguments(key, toAdd) {
        return [key, toAdd.toString()];
      },
      transformReply(reply) {
        return reply;
      }
    })
  }
});

async function useLuaScript() {
  await client.connect();

  await client.set('key', '17');
  const result = await client.add('key', 25); // 42
  console.log(result);

  await client.disconnect();
}

useLuaScript();
```

**Output**:

```sh
42
```

### Disconnecting

Node-Redis provides two methods for disconnecting from the Redis server: `.quit()` and `.disconnect()`.

#### Example

1. **Using `.quit()`**:

```javascript
import { createClient } from 'redis';

async function gracefulQuit() {
  const client = createClient();
  await client.connect();

  const [ping, get, quit] = await Promise.all([
    client.ping(),
    client.get('key'),
    client.quit()
  ]);

  console.log(ping, get, quit); // ['PONG', null, 'OK']
}

gracefulQuit();
```

**Output**:

```sh
PONG null OK
```

2. **Using `.disconnect()`**:

```javascript
import { createClient } from 'redis';

async function forceDisconnect() {
  const client = createClient();
  await client.connect();

  await client.set('key', 'value');
  await client.disconnect();

  try {
    await client.get('key');
  } catch (err) {
    console.log('ClosedClient Error');
  }
}

forceDisconnect();
```

**Output**:

```sh
ClosedClient Error
```
Let's dive into the functionalities of **Auto-Pipelining**, **Clustering**, and **Events** in Node-Redis, with full explanations, examples, and outputs.

### Auto-Pipelining

Auto-Pipelining in Node-Redis groups multiple commands issued during the same event loop tick into a single network request. This reduces the number of round trips to the Redis server, improving performance.

#### Example

1. **Without Auto-Pipelining**:

```javascript
import { createClient } from 'redis';

async function withoutAutoPipelining() {
  const client = createClient();
  await client.connect();

  await client.set('Tm9kZSBSZWRpcw==', 'users:1');
  await client.sAdd('users:1:tokens', 'Tm9kZSBSZWRpcw==');

  await client.disconnect();
}

withoutAutoPipelining();
```

2. **With Auto-Pipelining**:

```javascript
import { createClient } from 'redis';

async function withAutoPipelining() {
  const client = createClient();
  await client.connect();

  await Promise.all([
    client.set('Tm9kZSBSZWRpcw==', 'users:1'),
    client.sAdd('users:1:tokens', 'Tm9kZSBSZWRpcw==')
  ]);

  await client.disconnect();
}

withAutoPipelining();
```

In this example, using `Promise.all` ensures that both commands are pipelined together, reducing network latency.

### Clustering

Redis clustering allows you to distribute your data across multiple Redis nodes. Node-Redis supports clustering, which improves scalability and availability.

#### Example

```javascript
import { createCluster } from 'redis';

async function clusteringExample() {
  const cluster = createCluster({
    rootNodes: [
      { url: 'redis://localhost:6379' },
      { url: 'redis://localhost:6380' },
      { url: 'redis://localhost:6381' }
    ]
  });

  await cluster.connect();

  await cluster.set('key', 'value');
  const value = await cluster.get('key');
  console.log('Value:', value);

  await cluster.disconnect();
}

clusteringExample();
```

This code connects to a Redis cluster, sets a key-value pair, retrieves it, and then disconnects.

### Events

Node-Redis is an EventEmitter and emits events to signal changes in the network status. It's important to handle these events to manage the client's lifecycle effectively.

#### Example

```javascript
import { createClient } from 'redis';

async function eventHandling() {
  const client = createClient();

  client.on('connect', () => {
    console.log('Connecting to Redis server...');
  });

  client.on('ready', () => {
    console.log('Client is ready to use');
  });

  client.on('end', () => {
    console.log('Connection has been closed');
  });

  client.on('error', (error) => {
    console.error('Redis Client Error:', error);
  });

  client.on('reconnecting', () => {
    console.log('Client is trying to reconnect to the server');
  });

  await client.connect();

  await client.set('key', 'value');
  const value = await client.get('key');
  console.log('Value:', value);

  await client.quit();
}

eventHandling();
```

**Output**:

```sh
Connecting to Redis server...
Client is ready to use
Value: value
Connection has been closed
```

In this example, we listen to various events emitted by the Node-Redis client, such as `connect`, `ready`, `end`, `error`, and `reconnecting`. These events help you monitor and re
