# Menggunakan Node.js sebagai base image
FROM node:latest

# Set working directory
WORKDIR /app

# Copy file package.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy semua file ke working directory
COPY . .

# Ekspos port 3000
EXPOSE 3000

# Jalankan aplikasi
CMD ["node", "server.js"]