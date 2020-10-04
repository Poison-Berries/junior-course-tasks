# Зачет по HTTP
Небольшая серия из 7 тасков на знание разных сущностей в протоколе HTTP, флагами в которых являются дни рождения, установленные в качестве переменных окружения (`flag0`, `flag1`, ..., `flag6`). Даты указываются с точками и ведущими нулями, например, `flag0=29.02`, `flag1=01.12`, `flag2=03.03`

## Использование
### With docker
```bash
docker run --rm \
    -e flag0=date0 -e flag1=date1 ... -e flag6=date6 -p 8080:6202 \
    docker.pkg.github.com/poison-berries/junior-course-tasks/http_exam
```

### Without docker
1. Установить зависимости из `requirements.txt`
2. Установить переменные окружения (см. описание)
3. Запустить `http_examp.py`

## Автор
[Nikolay Nechaev (aka @kolayne)](https://github.com/kolayne)
