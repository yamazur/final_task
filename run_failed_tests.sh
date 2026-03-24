#!/bin/bash

JAR_PATH="./selenium/selenium-server-4.41.0.jar"

echo "Запуск Selenium Grid..."
java -jar "$JAR_PATH" standalone --selenium-manager true &
GRID_PID=$!

sleep 10

export GRID_URL="http://localhost:4444"

echo "Запуск только упавших тестов..."
pytest --lf -n 2

kill $GRID_PID

#./run_failed_tests.sh