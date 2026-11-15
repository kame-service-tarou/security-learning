import express from 'express';
import os from 'node:os'; 

const app = express();
const PORT = process.env.PORT || 3000;

// JSONリクエストボディのパースを有効化
app.use(express.json());

// ルートエンドポイント：コンテナの内部情報をJSONで返す
app.get('/', (req, res) => {
  res.json({
    message: 'Hello from Express running inside a Docker Container!',
    containerInfo: {
      hostname: os.hostname(),       // UTS Namespaceによって隔離されたコンテナ固有ホスト名
      platform: os.platform(),       // コンテナのOSプラットフォーム (linux)
      architecture: os.arch(),
      processId: process.pid,        // PID Namespace内のプロセスID
      uptimeSeconds: process.uptime()
    },
    environment: process.env.NODE_ENV || 'development',
    timestamp: new Date().toISOString()
  });
});

// ヘルスチェック用エンドポイント
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'ok' });
});

// 【注意】コンテナ内では "localhost(127.0.0.1)" ではなく "0.0.0.0" で待ち受ける
app.listen(PORT, '0.0.0.0', () => {
  console.log(`🚀 Express server is running on http://0.0.0.0:${PORT}`);
});
