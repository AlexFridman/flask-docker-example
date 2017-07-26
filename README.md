# Пример упаковки модели-веб-сервиса с зависимостями в docker контейнер

## Для ускорения процесса сборки контейнера тяжелые wheel помещены в папку packages
(альтернативный вариант - при каждой сборке ставить все из requirements.txt)

Запуск процесса сборки

```bash
docker build -t flask-sample-one:latest .
```

Запуск контейнера (модель будет доступна на порту 5000)

```bash
docker run -d -p 5000:5000 flask-sample-one
```

Пример обращения к модели

```bash
$ curl -H "Content-Type: application/json" -X POST -d '{"data":"data"}' http://127.0.0.1:5000/predict
{
  "X": {
    "data": "data"
  },
  "y_pred": [
    1.0,
    1.0
  ]
}
```
