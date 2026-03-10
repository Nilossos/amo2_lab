# AMO2 Lab

## Запуск

### 1. Установка окружения

```bash
python -m venv venv
```

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Linux / macOS / Git Bash:**
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Запуск пайплайна

```bash
bash pipeline.sh
```

На Windows можно использовать Git Bash или WSL. Пайплайн последовательно выполняет:
1. Создание датасетов
2. Предобработку данных
3. Обучение модели
4. Тестирование модели

---

## Данные

Синтетические погодные данные: 200 дней с колонками `day`, `temperature`, `humidity`, `pressure`. Есть сезонность, шум и ~5% пропусков. Train — 5 файлов без аномалий, test — 3 файла с аномалиями (резкие скачки температуры и влажности).

---

## Файлы

| Файл | Описание |
|------|----------|
| `data_creation.py` | Генерация train/test CSV |
| `model_preprocessing.py` | Заполнение пропусков, StandardScaler, сохранение в `data/processed/` |
| `model_preparation.py` | Обучение LinearRegression, сохранение в `models/model.pkl` |
| `model_testing.py` | Загрузка модели, MSE и R² на тесте |
| `pipeline.sh` | Скрипт запуска всего пайплайна |
