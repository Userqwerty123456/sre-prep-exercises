#!/bin/bash
# Скрипт для удаления файлов старше N дней в указанной директории
# Использование: ./clean_old_files.sh <directory> <days>

# Проверяем, что переданы два аргумента
if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: $0 <directory> <days>"
    exit 1
fi

DIR="$1"
DAYS="$2"

# Проверяем, что директория существует
if [ ! -d "$DIR" ]; then
    echo "Error: Directory $DIR does not exist."
    exit 1
fi

# Проверяем, что DAYS — положительное число
if ! [[ "$DAYS" =~ ^[0-9]+$ ]]; then
    echo "Error: Days must be a positive integer."
    exit 1
fi

# Находим и удаляем файлы
echo "Deleting files older than $DAYS days in $DIR ..."
find "$DIR" -type f -mtime +"$DAYS" -delete

if [ $? -eq 0 ]; then
    echo "Done."
else
    echo "Error occurred."
    exit 1
fi
