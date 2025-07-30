# Build stage
FROM debian:latest AS build-env

# Install Flutter dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    unzip \
    xz-utils \
    zip \
    libglu1-mesa \
    && rm -rf /var/lib/apt/lists/*

# Install Flutter
RUN git clone https://github.com/flutter/flutter.git /flutter
ENV PATH="/flutter/bin:${PATH}"

# Enable web support
RUN flutter channel stable
RUN flutter upgrade
RUN flutter config --enable-web

# Copy the app files to the container
COPY . /app/
WORKDIR /app

# Get app dependencies
RUN flutter pub get

# Build the app for the web
RUN flutter build web

# Production stage
FROM nginx:alpine

# Copy the built app from the build stage
COPY --from=build-env /app/build/web /usr/share/nginx/html

# Copy nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"] 