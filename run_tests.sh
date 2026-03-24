#!/bin/bash

JAR_PATH="./selenium/selenium-server-4.41.0.jar"

# Запускаем Grid на localhost
echo "Запуск Selenium Grid..."
java -jar "$JAR_PATH" standalone --selenium-manager true &
GRID_PID=$!

sleep 10

# Устанавливаем URL для тестов
export GRID_URL="http://localhost:4444"

echo "Запуск тестов через pytest-xdist..."
pytest tests/ -n 2

echo "Остановка Selenium Grid..."
kill $GRID_PID

#chmod +x run_tests.sh - запуск в терминале