# Andrea Grandieri andreagrandieri.github.io grn@giusp.com

FROM ubuntu:22.04
LABEL author="Andrea Grandieri andreagrandieri.github.io grn@giusp.com"
LABEL tag="1.21.4-126"
LABEL arch="aarch64 (aka: arm64)"
LABEL base="ubuntu:22.04"
LABEL local_availability_openjdk="openjdk-23.0.2_linux-aarch64_bin.tar.gz"
LABEL local_availability_paper="paper-1.21.4-126.jar"
LABEL local_availability_server_properties_builder="server.properties-builder.py"

RUN apt-get update
RUN apt-get install -y bash python3
RUN apt-get install -y tar curl nano

# Install OpenJDK 23.0.2 from local availability
ADD openjdk-23.0.2_linux-aarch64_bin.tar.gz /opt/
RUN ln -s /opt/jdk-23.0.2/bin/java /usr/bin/java

# Add Paper Server "build 126 for Minecraft 1.21.4" from local availability
ADD paper-1.21.4-126.jar /internal_data/paper-1.21.4-126.jar

ADD server.properties-builder.py /internal_data/server.properties-builder.py
WORKDIR /data

ENV JVM_MIN_MEM="1G"
ENV JVM_MAX_MEM="1G"
ENV JVM_XX_OPTS=""

EXPOSE 25565
EXPOSE 25575

CMD cp /internal_data/paper-1.21.4-126.jar /data/paper.jar && \
python3 /internal_data/server.properties-builder.py > /data/server.properties && \
echo "eula=true" > /data/eula.txt && \
echo "Starting server with minmem:" ${JVM_MIN_MEM} "and maxmem:" ${JVM_MAX_MEM} "..." && \
java -Xms$JVM_MIN_MEM -Xmx$JVM_MAX_MEM $JVM_XX_OPTS -jar /data/paper.jar --nogui
