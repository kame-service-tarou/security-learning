# Writeup

## 攻略法
canary_savedとinputが同じ値ならflagゲットできる。
canary_savedは何なのか見ると
canary_savedはcanaryのデリファレンスであった。

[メモ]
>**デリファレンスとは**
ポインタが格納しているアドレスを使って、そのアドレスの先にある値にアクセスすること

さらに見てみよう。canaryというポインタ変数はなんて定義されているかというと、
``` c
canary = (unsigned long *)(buf + 0xc8);
```
とあった。bufの+0xc8のアドレスをcanaryにぶち込んでいる。
**つまり、目標はbufの+0xc8のアドレスの値を見つけること。**

どうやってその値を把握するか考える。
コードについて調べながら考える。
まずはread関数だ。
```c
read(fd, buf, count)
```
この引数と意味は以下のとおりだよ。
|引数|意味|
|--|--|
|fd|読み込み元を指定するファイルディスクリプタ|
|buf|読み込んだデータを格納するメモリの先頭アドレス|
|count|最大なんバイト読み込むか|
cコードは
``` c
read(0, buf, 0xcf);
```
これは読み込み元をターミナルに指定し、bufの先頭アドレスから読み込んで、最大0xcfバイト読み込むことを意味する。
最初のread関数のところは分かった。じゃあ次の関数を見てみると
```c
puts(buf)
```
これはbufに格納されている文字列をターミナルに出力します。
この関数を利用して、buf+0xc8のアドレスにある値を出力させたい。
puts関数の仕様として、上記のコードは概念的に次のような意味です。
```c
puts(&buf[0])
```
つまり、bufから先頭要素のアドレスを取得して、そのアドレスをputsに渡し、putsはそのアドレスから文字を順番に読み取り、``\0``が見つかったら読み取りを終了して、文字列を出力して改行します。

なるほどじゃあ、初めのInputでbufを0xc8バイト分埋めてしまえば出てくるんじゃないかな。やってみた。

```
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
\xe7\x96v \xa8\xa3\x9d\x10\xdf\xd9\xca\xfd\x7f
```
出たーでた。でたー！
でも待ってやPIEあるから実行ごとに変わるくね。どうすんのや。調べよう。調べた。
**stack smashing**は最後のほうに起きるからリークさせた後にその値を何かしらのpwntoolsを使って保存しておく。
そして二つ目のread関数を使って第二引数であるrsiにリークさせた値を入れて、flagをゲットする方針で活きます。
でも今回の問題の第二引数はInputのアドレスを指しているだけなので、普通にcanary_savedの値を入れるだけでいい
でも今回のスタックは




# 参考文献
[pwn入門](https://qiita.com/trimscash/items/71f417f99508f8ca78f8)

[SSP](https://qiita.com/GmS944y/items/b10a1abde35f7175ea4b)

