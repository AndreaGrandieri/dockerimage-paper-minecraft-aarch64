# andreagrandieri/paper-minecraft-aarch64

Docker image for a Paper Minecraft Server.

## Basic config with docker.compose

```yaml
services:
  minecraft:
    image: andreagrandieri/paper-minecraft-aarch64:1.21.4-126
    tty: true
    stdin_open: true
    ports:
      # Game
      - "<EXPOSED_PORT_1>:25565"
      # RCON Console
      - "<EXPOSED_PORT_2>:25575"
    volumes:
      - "<BIND_VOLUME_PATH>:/data"
    networks:
      - stacknet
    restart: unless-stopped

networks:
  stacknet:
```

## Env variables

| Variable Name                     | Required | Default Value    | Description |
| --------------------------------- | -------- | ---------------- | ----------- |
| JVM_MIN_MEM                       | NO       | 1G               |             |
| JVM_MAX_MEM                       | NO       | 1G               |             |
| JVM_XX_OPTS                       | NO       |                  |             |
| ACCEPTS_TRANSFERS                 | NO       | false            |             |
| ALLOW_FLIGHT                      | NO       | false            |             |
| ALLOW_NETHER                      | NO       | true             |             |
| BROADCAST_CONSOLE_TO_OPS          | NO       | true             |             |
| BROADCAST_RCON_TO_OPS             | NO       | true             |             |
| DIFFICULTY                        | NO       | easy             |             |
| ENABLE_COMMAND_BLOCK              | NO       | false            |             |
| ENABLE_JMX_MONITORING             | NO       | false            |             |
| ENABLE_QUERY                      | NO       | false            |             |
| ENABLE_RCON                       | NO       | false            |             |
| ENABLE_STATUS                     | NO       | true             |             |
| ENFORCE_SECURE_PROFILE            | NO       | true             |             |
| ENFORCE_WHITELIST                 | NO       | true             |             |
| ENTITY_BROADCAST_RANGE_PERCENTAGE | NO       | 100              |             |
| FORCE_GAMEMODE                    | NO       | true             |             |
| FUNCTION_PERMISSION_LEVEL         | NO       | 4                |             |
| GAMEMODE                          | NO       | survival         |             |
| GENERATE_STRUCTURES               | NO       | true             |             |
| GENERATOR_SETTINGS                | NO       |                  |             |
| HARDCORE                          | NO       | false            |             |
| HIDE_ONLINE_PLAYERS               | NO       | false            |             |
| INITIAL_DISABLED_PACKS            | NO       |                  |             |
| INITIAL_ENABLED_PACKS             | NO       | vanilla          |             |
| LEVEL_NAME                        | NO       | world            |             |
| LEVEL_SEED                        | NO       |                  |             |
| LEVEL_TYPE                        | NO       | minecraft:normal |             |
| MAX_BUILD_HEIGHT                  | NO       | 256              |             |
| LOG_IPS                           | NO       | true             |             |
| MAX_CHAINED_NEIGHBOR_UPDATES      | NO       | 1000000          |             |
| MAX_PLAYERS                       | NO       | 20               |             |
| MAX_TICK_TIME                     | NO       | 30000            |             |
| MAX_WORLD_SIZE                    | NO       | 29999984         |             |
| MOTD                              | NO       | Minecraft Server |             |
| NETWORK_COMPRESSION_THRESHOLD     | NO       | 256              |             |
| ONLINE_MODE                       | NO       | true             |             |
| OP_PERMISSION_LEVEL               | NO       | 4                |             |
| PAUSE_WHEN_EMPTY_SECONDS          | NO       | -1               |             |
| PLAYER_IDLE_TIMEOUT               | NO       | 0                |             |
| PREVENT_PROXY_CONNECTIONS         | NO       | false            |             |
| PREVIEWS_CHAT                     | NO       | false            |             |
| PVP                               | NO       | true             |             |
| QUERY_PORT                        | NO       | 25565            |             |
| RATE_LIMIT                        | NO       | 0                |             |
| RCON_PASSWORD                     | NO       |                  |             |
| RCON_PORT                         | NO       | 25575            |             |
| REGION_FILE_COMPRESSION           | NO       | deflate          |             |
| REQUIRE_RESOURCE_PACK             | NO       | false            |             |
| RESOURCE_PACK                     | NO       |                  |             |
| RESOURCE_PACK_PROMPT              | NO       |                  |             |
| RESOURCE_PACK_SHA1                | NO       |                  |             |
| SERVER_IP                         | NO       |                  |             |
| SERVER_PORT                       | NO       | 25565            |             |
| SIMULATION_DISTANCE               | NO       | 10               |             |
| SPAWN_ANIMALS                     | NO       | true             |             |
| SPAWN_MONSTERS                    | NO       | true             |             |
| SPAWN_NPCS                        | NO       | true             |             |
| SPAWN_PROTECTION                  | NO       | 16               |             |
| SYNC_CHUNK_WRITES                 | NO       | true             |             |
| TEXT_FILTERING_CONFIG             | NO       |                  |             |
| USE_NATIVE_TRANSPORT              | NO       | true             |             |
| VIEW_DISTANCE                     | NO       | 10               |             |
| WHITE_LIST                        | NO       | true             |             |

## Suggested config with docker.compose using Aikar's Flags and recommended memory for JVM

```yaml
services:
  minecraft:
    image: andreagrandieri/paper-minecraft-aarch64:1.21.4-126
    tty: true
    stdin_open: true
    ports:
      # Game
      - "<EXPOSED_PORT_1>:25565"
      # RCON Console
      - "<EXPOSED_PORT_2>:25575"
    environment:
      JVM_MIN_MEM: "2G"
      JVM_MAX_MEM: "8G"
      JVM_XX_OPTS: >
        -XX:+UseG1GC
        -XX:+ParallelRefProcEnabled
        -XX:MaxGCPauseMillis=200
        -XX:+UnlockExperimentalVMOptions
        -XX:+DisableExplicitGC
        -XX:+AlwaysPreTouch
        -XX:G1NewSizePercent=30
        -XX:G1MaxNewSizePercent=40
        -XX:G1HeapRegionSize=8M
        -XX:G1ReservePercent=20
        -XX:G1HeapWastePercent=5
        -XX:G1MixedGCCountTarget=4
        -XX:InitiatingHeapOccupancyPercent=15
        -XX:G1MixedGCLiveThresholdPercent=90
        -XX:G1RSetUpdatingPauseTimePercent=5
        -XX:SurvivorRatio=32
        -XX:+PerfDisableSharedMem
        -XX:MaxTenuringThreshold=1
    volumes:
      - "<BIND_VOLUME_PATH>:/data"
    networks:
      - stacknet
    restart: unless-stopped

networks:
  stacknet:
```
