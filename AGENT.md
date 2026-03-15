# Vibe Calculator 專案規範 (DDD Edition)

## 專案概述
這是一個採用 **DDD (Domain-Driven Design)** 架構的 FastAPI 計算機專案。

## 技術堆疊
- 語言: Python 3.10+
- 框架: FastAPI
- 測試: Pytest
- CI/CD: GitLab CI

## 🏗️ 架構規範 (Architecture Guidelines)
本專案嚴格遵守 DDD 分層架構，**禁止**將所有邏輯寫在單一檔案。請依照以下結構重構：

### 目標資料夾結構
src/
├── domain/          # 核心業務邏輯 (純 Python)
│   └── services.py  # 加法、乘法運算
├── application/     # 應用層
│   └── calculator_service.py
└── interfaces/      # 介面層 (API)
    └── api/
        └── main.py  # FastAPI Entry Point

### 依賴原則
1. **Domain** 不依賴任何層。
2. **Application** 依賴 Domain。
3. **Interfaces** 依賴 Application。

## 🧪 測試與驗收
1. 重構後必須確保 `pytest` 通過。
2. 必須修正 `add` 和 `multiply` 的計算邏輯錯誤。

## 📝 編碼準則
- 所有函式必須包含 **Type Hints**。
