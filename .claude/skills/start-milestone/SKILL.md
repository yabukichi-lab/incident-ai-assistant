---
name: start-milestone
description: 新しいマイルストーンを開始し、docs/milestones/TEMPLATE.md を基に docs/milestones/Mx.md を作成する。引数にマイルストーン番号を指定する。
argument-hint: "[M1]"
disable-model-invocation: true
---

$0 を開始します。引数が空の場合は、docs/PROGRESS.md と docs/ROADMAP.md から次に開始するマイルストーン番号を確認し、進める前に番号の確認を求めてください。

README.md、CLAUDE.md、docs/ROADMAP.md、docs/SCHEDULE.md、docs/PROGRESS.md、
docs/milestones/TEMPLATE.md、直前の完了済みマイルストーンの docs/milestones/Mx.md を確認してください。

CLAUDE.md 第6節「マイルストーン開始時のルール」に従い、次を行ってください。

1. ロードマップの $0 の到達状態・通過条件と、直前のマイルストーンの振り返り・未解決事項を確認する
2. $0 で必要な合成データの件数・性質と、既存データの充足状況を確認し、不足分だけ最小限で定義する
3. $0 の到達状態と通過条件を変えずに、現在の実装状態に合わせて2〜5個の短いサイクルへ分割する
4. 各サイクルの目的・理由・成果物・受け入れ条件・異常系確認と、今回の対象外を記載する
5. docs/milestones/$0.md の作成案と docs/PROGRESS.md の現在地の更新案を提示し、承認を得てから反映する

実在する業務データは使用しないでください。未来のマイルストーン詳細やデータは先回りして作成しないでください。
