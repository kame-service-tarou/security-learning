
import socket
import string


# 接続先
HOST = "34.170.146.252"
PORT = 62655

# Base64で使用されるデータ文字
BASE64_CHARS = (
    string.ascii_lowercase
    + string.ascii_uppercase
    + string.digits
    + "+/"
)


class MySocket:
    """ソケット通信を行うクラス"""

    def __init__(self):
        self.sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        self.buffer = b""

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        totalsent = 0

        while totalsent < len(msg):
            sent = self.sock.send(msg[totalsent:])

            if sent == 0:
                raise RuntimeError("socket connection broken")

            totalsent += sent

    def myreceive(self):
        prompt = b"Input: "

        while True:
            # プロンプトが受信データに含まれているか確認
            index = self.buffer.find(prompt)

            if index != -1:
                # プロンプトより前の部分がサーバーの応答
                response = self.buffer[:index]

                # プロンプトより後ろをバッファに残す
                self.buffer = self.buffer[index + len(prompt):]

                return response

            # まだプロンプトが届いていなければ追加受信
            chunk = self.sock.recv(2048)

            if chunk == b"":
                raise RuntimeError("socket connection broken")

            self.buffer += chunk

    def close(self):
        self.sock.close()


def main():

    client = MySocket()

    try:
        # 1. サーバーに接続
        client.connect(HOST, PORT)

        # 2. 最初のInput: を受信
        response = client.myreceive()
        print("接続時の応答:", repr(response))

        # 3. 既知のBase64部分
        known = b"QWxwYWNhe"

        # 4. 調査するプローブ
        # 0x20 と 0x21～0x2f
        probes = [0x20] + list(range(0x21, 0x30))

        # 5. 実際のサーバーの反応を保存
        results = []

        print("\n--- サーバーへの問い合わせ ---")

        for probe in probes:

            # 既知の部分 + プローブ1文字 + 改行
            msg = known + bytes([probe]) + b"\n"

            client.mysend(msg)

            response = client.myreceive()

            # ErrorならTrue、IncorrectならFalse
            is_error = b"Error" in response

            results.append(is_error)

            print(
                f"probe: {probe:#04x}, "
                f"character: {chr(probe)!r}, "
                f"response: {response!r}"
            )

        print("\n実際の反応パターン:")
        print(results)

        # 6. 未知の文字の候補を予測
        print("\n--- 候補文字の照合 ---")

        candidates = []

        for candidate in BASE64_CHARS:

            predictions = []

            for probe in probes:

                # 候補文字とプローブのXOR
                xor_result = ord(candidate) ^ probe

                # XOR結果がBase64のデータ文字ならError
                is_error = chr(xor_result) in BASE64_CHARS

                predictions.append(is_error)

            # 実際の反応と予測が一致するか
            if predictions == results:
                candidates.append(candidate)

        print("未知文字の候補:", candidates)
        print("候補数:", len(candidates))

    finally:
        client.close()


if __name__ == "__main__":
    main()
