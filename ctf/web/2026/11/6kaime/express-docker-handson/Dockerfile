# 軽量なNode.js 20のAlpine Linuxベースイメージを使用
FROM node:20-alpine

# コンテナ内の作業ディレクトリを /app に設定
WORKDIR /app

# レイヤーキャッシュを効かせるため、先に package.json だけをコピー
COPY package.json ./

# 依存パッケージ（express）をコンテナ内にインストール
RUN npm install

# 残りのソースコード（server.jsなど）をコピー
COPY . .

# サーバーが使用するポート番号を明示
EXPOSE 3000

# セキュリティのため非rootユーザー（node）に切り替え
USER node

# コンテナ起動時にExpressサーバーを実行
CMD ["npm", "start"]
