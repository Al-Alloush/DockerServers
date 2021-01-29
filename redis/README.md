# Docker redis / redisTimeSeries Connections

### 1. Redis Commend:

>  `http://localhost:8081/`

### 2. to Use redisTimeSeries
uncomment redisTimeSeries and mack redis like a comment
 ```
    # redis:
    #     image: "redis:latest"
    #     container_name: redis
    #     hostname: redis
    #     volumes:
    #       - type: volume
    #         source: redisdata
    #         target: /data
    #     ports:
    #       - "6379:6379"
    #     networks:
    #         network:
    #     restart: always
    redis:
        image: "redislabs/redistimeseries"
        container_name: redisTimeSeries
        hostname: RedisTimeSeries
        volumes:
          - type: volume
            source: redisdata
            target: /data
        entrypoint:
          - redis-server 
          - --loadmodule
          - /usr/lib/redis/modules/redistimeseries.so
          - --appendonly yes
        ports:
            - "6379:6379"
        networks:
            network:
        restart: always
 ```

### 3. add connection in Python
for avoid return string in this form b'sting' encoding this text by: .encode('utf-8')
but when we need to use this test we must decoding  the get() return by: .decode('utf-8')
cache.set('var1', 'the test'.encode('utf-8'))
or add charset="utf-8" to connection code.
```
> import redis
> redisDB = redis.Redis(host='redis', port=6379, charset="utf-8", decode_responses=True) 
```

