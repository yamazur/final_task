#!/bin/bash

JAR_PATH="./selenium/selenium-server-4.41.0.jar"

# аргумент — браузер (по умолчанию chrome)
BROWSER=${1:-chrome}

echo "Браузер: $BROWSER"

echo "Запуск Selenium Grid..."
java -jar "$JAR_PATH" standalone --selenium-manager true &
GRID_PID=$!

echo "Ждём запуска Grid..."
sleep 10

export GRID_URL="http://localhost:4444"

echo "Запуск тестов через Grid..."
pytest tests/ -n 2 --browser=$BROWSER --remote

echo "Остановка Selenium Grid..."
kill $GRID_PID