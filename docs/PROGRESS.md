# 進捗管理

現在地と次の作業の正本。通常の再開では本書から必要な資料へ進む。詳細な作業履歴は [M0の履歴](history/M0.md) に保存する。更新はCLAUDE.mdの承認規則に従う。

## 1. 現在地

| 項目 | 現在値 |
|---|---|
| 現在のマイルストーン | M0: 開発基盤とエンドツーエンド疎通 |
| 現在のサイクル | M0-C1: バックエンドの最小health API |
| 状態 | In progress（テストまで完了。残りは停止・再起動の再現確認と `application` フィールド追加） |
| 学習モード | Level 1: Follow |
| 第一完成地点 | M8 |
| 詳細計画 | [M0](milestones/M0.md) の基本情報・スコープ・M0-C1 |

## 2. 次に行う1ステップ

停止・再起動の再現確認を本人が手で行う。`backend/` で `uv run uvicorn main:app --reload` を起動し、別ターミナルの `curl -i http://127.0.0.1:8000/health` で200と `{"backend":"ok"}` を確認する。次にCtrl+Cで停止して同じcurlを実行し、HTTP応答ではなく接続拒否（`Connection refused`）になることを確認する。最後に再起動して最初と同じ結果に戻ることを確認する。

完了確認：3回のcurl結果（200、接続拒否、200）を報告できる。完了後、M0-C1最後の小さな変更課題である `application` フィールド追加へ進む。

## 3. 完了済み・未解決事項

- 完了済み：Pythonとuvによる環境準備、health APIの実装、正常応答の確認（ユーザーの問題解消報告に基づく。当時のCodexによるHTTP再検証は未実施）。
- M0-C1の残り：停止・再起動確認、`application` フィールド追加。詳細チェックは [M0-C1](milestones/M0.md#m0-c1-バックエンドの最小health-api)。
- ブロッカー：なし。
- 未理解事項：辞書からJSONへの変換をFastAPIが担当すること（本人はUvicornと回答）。詳細は [L-M0-004の後日の振り返り](learning/M0.md#l-m0-004)。

## 4. 直近の変更（2026-09-14）

本人が手元で `uv run pytest` を実行し1 passedを確認した。テストコードの各行の役割も説明でき、受け入れ条件「health APIのテストが通る」を完了した。変更はPR #2として `develop` へマージ済み。

同日、本人が `GET /health` からJSON応答までの処理経路を説明し、M0-C1の学習確認を完了した。JSON変換の担当は未理解事項として学習記録に残した。
Claude Codeが `backend/tests/test_health.py`（TestClientで `/health` の200応答と本文を検証する1件）を追加し、`backend/pyproject.toml` に開発用依存のpytestとhttpx2、pytestの `testpaths`・`pythonpath` 設定を加えた。httpx2は、現行のStarletteがTestClient用にhttpxではなくhttpx2を推奨するため採用した。

### 2026-09-13

コーディングエージェントをCodexからClaude Codeへ切り替えた。`AGENTS.md` を `CLAUDE.md` へ改名し、各文書のCodex表記を置換、`.claude/` にpermission modeの設定と `/resume-cycle`・`/start-milestone` スキルを追加した。

同日、目指すエンジニア像をREADMEへ、本人が手で行う作業の基準をCLAUDE.md第4.1節へ追記した。ロードマップにはGit・差分レビュー、静的検査（M1）、最小CI（M3）、生成品質評価（M6）、プロンプトインジェクション対策（M7・M8）を追加した。アプリの実装とM0-C1の完了状態は変えていない。詳細は [履歴](history/M0.md)。

M0-C1の残り作業では、テスト実行と起動・停止確認を本人が手で行う。

## 5. 必要なときに読む資料

- [README](../README.md)：概要、構成、開始手順。
- [ロードマップ](ROADMAP.md)：全体の到達点と通過条件。
- [スケジュール](SCHEDULE.md)：2026-09-07〜2027-08-22の全体計画。W01の当時の日別計画は [履歴](history/M0.md)。
- [M0の履歴](history/M0.md)：過去の確認結果、判断、保留案。現在の方針は現行の各文書を確認する。
- [学習記録の運用](learning/README.md)：学習記録を作成・更新するときの対象と書式。

## 6. 再開方法

Claude Codeで `/resume-cycle` を実行する。スキル本文は `.claude/skills/resume-cycle/SKILL.md` にある。手動で指示する場合の文面は次の通り。

```text
CLAUDE.mdの読み込み規則に従い、docs/PROGRESS.mdの「次に行う1ステップ」から再開してください。
現在のマイルストーンの基本情報・スコープ・該当サイクルと、関連する実装・テストを必要な範囲で確認してください。
目的、理由、対象ファイル、変更内容、期待結果、確認方法を先に説明し、承認済みの範囲で進めてください。
```
