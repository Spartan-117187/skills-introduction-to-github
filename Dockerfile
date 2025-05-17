# Dockerfile for an intentionally vulnerable web application
# This uses OWASP Juice Shop, an open-source project for security training

FROM node:14

# Get the vulnerable application source
RUN git clone https://github.com/juice-shop/juice-shop.git /app
WORKDIR /app

# Install dependencies
RUN npm install --silent

# Expose the default Juice Shop port
EXPOSE 3000

# Start the vulnerable application
CMD ["npm", "start"]
