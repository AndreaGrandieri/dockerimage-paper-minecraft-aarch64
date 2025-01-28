# Andrea Grandieri andreagrandieri.github.io grn@giusp.com

from datetime import datetime
import os


def main():
    # Create server.properties content and print for piping
    print(f"""
    # Minecraft server properties
    # Generated on {datetime.now().strftime("%d.%b.%Y %H:%M:%S")}

    accepts-transfers={os.getenv("ACCEPTS_TRANSFERS", "false")}
    allow-flight={os.getenv("ALLOW_FLIGHT", "false")}
    allow-nether={os.getenv("ALLOW_NETHER", "true")}
    broadcast-console-to-ops={os.getenv("BROADCAST_CONSOLE_TO_OPS", "true")}
    broadcast-rcon-to-ops={os.getenv("BROADCAST_RCON_TO_OPS", "true")}
    difficulty={os.getenv("DIFFICULTY", "easy")}
    enable-command-block={os.getenv("ENABLE_COMMAND_BLOCK", "false")}
    enable-jmx-monitoring={os.getenv("ENABLE_JMX_MONITORING", "false")}
    enable-query={os.getenv("ENABLE_QUERY", "false")}
    enable-rcon={os.getenv("ENABLE_RCON", "false")}
    enable-status={os.getenv("ENABLE_STATUS", "true")}
    enforce-secure-profile={os.getenv("ENFORCE_SECURE_PROFILE", "true")}
    enforce-whitelist={os.getenv("ENFORCE_WHITELIST", "true")}

    # Should be changed on needs, usually decresed (default: 100)
    entity-broadcast-range-percentage={os.getenv("ENTITY_BROADCAST_RANGE_PERCENTAGE", "100")}

    force-gamemode={os.getenv("FORCE_GAMEMODE", "true")}
    function-permission-level={os.getenv("FUNCTION_PERMISSION_LEVEL", "4")}
    gamemode={os.getenv("GAMEMODE", "survival")}
    generate-structures={os.getenv("GENERATE_STRUCTURES", "true")}
    generator-settings={os.getenv("GENERATOR_SETTINGS", "")}
    hardcore={os.getenv("HARDCORE", "false")}
    hide-online-players={os.getenv("HIDE_ONLINE_PLAYERS", "false")}
    initial-disabled-packs={os.getenv("INITIAL_DISABLED_PACKS", "")}
    initial-enabled-packs={os.getenv("INITIAL_ENABLED_PACKS", "vanilla")}
    level-name={os.getenv("LEVEL_NAME", "world")}
    level-seed={os.getenv("LEVEL_SEED", "")}
    level-type={os.getenv("LEVEL_TYPE", "minecraft:normal")}
    max-build-height={os.getenv("MAX_BUILD_HEIGHT", "256")}
    log-ips={os.getenv("LOG_IPS", "true")}
    max-chained-neighbor-updates={os.getenv("MAX_CHAINED_NEIGHBOR_UPDATES", "1000000")}
    max-players={os.getenv("MAX_PLAYERS", "20")}
    max-tick-time={os.getenv("MAX_TICK_TIME", "30000")}
    max-world-size={os.getenv("MAX_WORLD_SIZE", "29999984")}
    motd={os.getenv("MOTD", "Minecraft Server")}
    network-compression-threshold={os.getenv("NETWORK_COMPRESSION_THRESHOLD", "256")}
    online-mode={os.getenv("ONLINE_MODE", "true")}
    op-permission-level={os.getenv("OP_PERMISSION_LEVEL", "4")}
    pause-when-empty-seconds={os.getenv("PAUSE_WHEN_EMPTY_SECONDS", "-1")}
    player-idle-timeout={os.getenv("PLAYER_IDLE_TIMEOUT", "0")}
    prevent-proxy-connections={os.getenv("PREVENT_PROXY_CONNECTIONS", "false")}
    previews-chat={os.getenv("PREVIEWS_CHAT", "false")}
    pvp={os.getenv("PVP", "true")}
    query.port={os.getenv("QUERY_PORT", "25565")}
    rate-limit={os.getenv("RATE_LIMIT", "0")}

    # Should be a strong password, even if rcon is unused
    rcon.password={os.getenv("RCON_PASSWORD", "")}
    rcon.port={os.getenv("RCON_PORT", "25575")}

    region-file-compression={os.getenv("REGION_FILE_COMPRESSION", "deflate")}
    require-resource-pack={os.getenv("REQUIRE_RESOURCE_PACK", "false")}
    resource-pack={os.getenv("RESOURCE_PACK", "")}
    resource-pack-id={os.getenv("RESOURCE_PACK_ID", "")}
    resource-pack-prompt={os.getenv("RESOURCE_PACK_PROMPT", "")}
    resource-pack-sha1={os.getenv("RESOURCE_PACK_SHA1", "")}

    server-ip={os.getenv("SERVER_IP", "")}
    server-port={os.getenv("SERVER_PORT", "25565")}

    # Should be changed on needs, usually decresed (default: 10)
    simulation-distance={os.getenv("SIMULATION_DISTANCE", "10")}

    spawn-animals={os.getenv("SPAWN_ANIMALS", "true")}
    spawn-monsters={os.getenv("SPAWN_MONSTERS", "true")}
    spawn-npcs={os.getenv("SPAWN_NPCS", "true")}
    spawn-protection={os.getenv("SPAWN_PROTECTION", "16")}
    sync-chunk-writes={os.getenv("SYNC_CHUNK_WRITES", "true")}
    text-filtering-config={os.getenv("TEXT_FILTERING_CONFIG", "")}
    use-native-transport={os.getenv("USE_NATIVE_TRANSPORT", "true")}

    # Should be changed on needs, usually decresed (default: 10)
    view-distance={os.getenv("VIEW_DISTANCE", "10")}

    white-list={os.getenv("WHITE_LIST", "true")}
    """
    )


if __name__ == "__main__":
    main()
