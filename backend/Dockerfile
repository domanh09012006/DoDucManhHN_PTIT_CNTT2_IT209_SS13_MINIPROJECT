# Stage 1: Build application with Gradle
FROM eclipse-temurin:21-jdk-jammy AS builder
WORKDIR /app

# Copy gradle wrapper and configuration files
COPY gradlew settings.gradle build.gradle ./
COPY gradle ./gradle

# Make gradlew executable
RUN chmod +x gradlew

# Download dependencies to cache them
RUN ./gradlew dependencies --no-daemon || true

# Copy source code and build JAR
COPY src ./src
RUN ./gradlew bootJar --no-daemon -x test

# Stage 2: Runtime image with minimal JRE 21
FROM eclipse-temurin:21-jre-jammy
WORKDIR /app

# Create non-root system user for security
RUN groupadd -r spring && useradd -r -g spring spring
USER spring:spring

# Copy built JAR from builder
COPY --from=builder /app/build/libs/*.jar app.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "app.jar"]
