#!/bin/bash

JAR_PATH="./selenium/selenium-server-4.41.0.jar"

echo "Запуск Selenium Grid..."
java -jar "$JAR_PATH" standalone --selenium-manager true &
GRID_PID=$!  # сохраняем PID Grid, чтобы можно было убить процесс после тестов

sleep 10     # ждем, чтобы Grid поднялся (можно увеличить до 10 секунд при медленном старте)

echo "Запуск тестов через pytest-xdist..."
pytest tests/ -n 2

echo "Остановка Selenium Grid..."
kill $GRID_PID

#chmod +x run_tests.sh