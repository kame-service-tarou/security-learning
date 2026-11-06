# 逆アセンブル（Disassembly）ツールまとめ

逆アセンブルとは、実行ファイルなどに含まれる機械語をアセンブリ言語に変換すること。

CTFのPwn・Rev（Reverse Engineering）で、プログラムの処理や関数の動きを調べるために使用する。

## 1. objdump

ELFファイルなどの逆アセンブルに使う基本的なコマンド。

### 基本コマンド

```bash
objdump -d ./chall
```

実行ファイルの逆アセンブルを表示する。

```bash
objdump -M intel -d ./chall
```

Intel記法で逆アセンブルする。

```bash
objdump -M intel -d -S ./chall
```

ソースコード情報が利用可能な場合、アセンブリとソースコードを対応させて表示する。

## 2. GDB

プログラムを実行・デバッグしながら逆アセンブルできるデバッガ。

### 起動

```bash
gdb ./chall
```

### 主なコマンド

| コマンド | 説明 |
|---|---|
| `disassemble main` | main関数を逆アセンブル |
| `disassemble /r main` | マシンコードも表示 |
| `set disassembly-flavor intel` | Intel記法に変更 |
| `info functions` | 関数一覧を表示 |
| `x/10i $rip` | RIPから10命令を表示 |
| `break main` | main関数にブレークポイント |
| `run` | プログラムを実行 |
| `si` | 1命令ずつステップ実行 |

## 3. radare2

ターミナル上で静的解析や逆アセンブルができるツール。

### 起動

```bash
r2 -A ./chall
```

`-A` は解析を自動実行するオプション。

### 主なコマンド

| コマンド | 説明 |
|---|---|
| `aaa` | 詳細な解析を実行 |
| `afl` | 関数一覧を表示 |
| `pdf @ main` | main関数を逆アセンブル |
| `s main` | main関数の位置に移動 |
| `q` | 終了 |

## 4. Ghidra

GUIでプログラムを解析できるリバースエンジニアリングツール。

### 主な機能

- アセンブリコードの表示
- C言語に近い形式へのデコンパイル
- 関数・変数の解析
- クロスリファレンスの確認
- プログラム全体の構造把握

特に、アセンブリに慣れていない段階でプログラムの処理を理解するのに便利。

## 5. IDA Free

GUIで実行ファイルを解析できる逆アセンブラ。

### 主な機能

- アセンブリコードの表示
- 関数の解析
- 制御フローの可視化
- クロスリファレンスの確認

## 6. llvm-objdump

LLVMに付属する逆アセンブルツール。

```bash
llvm-objdump -d ./chall
```

Intel記法で表示する場合：

```bash
llvm-objdump -d --x86-asm-syntax=intel ./chall
```

## 7. ndisasm

x86・x86-64の生バイナリを逆アセンブルするツール。

```bash
ndisasm -b 64 binary.bin
```

`-b 64` は64ビットモードを指定するオプション。

ELFファイルではなく、機械語のバイト列を直接解析したい場合に便利。

---

## ツールの使い分け

| 目的 | おすすめ |
|---|---|
| ELF全体の逆アセンブル | objdump |
| 関数単位の逆アセンブル | GDB |
| 実行時のレジスタ・スタック確認 | GDB |
| ターミナルで静的解析 | radare2 |
| GUIでプログラム全体を解析 | Ghidra |
| GUIで逆アセンブル | IDA Free |
| LLVM系の逆アセンブル | llvm-objdump |
| 生バイナリの逆アセンブル | ndisasm |

## CTFでのおすすめ構成

- **Pwn**：GDB + pwndbg + objdump
- **Rev**：Ghidra + objdump
- **ターミナル中心の解析**：radare2

GDBで実行時のレジスタやスタックを確認し、Ghidraでプログラム全体の構造を把握すると、効率よく解析できる。
