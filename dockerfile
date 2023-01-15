# Build stage
FROM python:3.9 as build

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY . .

# Run tests
RUN pytest

# Run stage
FROM python:3.9-alpine

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY --from=build /app/requirements.txt .

# Install the dependencies
RUN apk add --no-cache --virtual .build-deps build-base \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps

# Copy the source code
COPY --from=build /app .

# Copy the .env file
COPY .env .

# Run the bot
CMD ["python", "bot.py"]
