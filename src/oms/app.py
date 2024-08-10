from flask import Flask, request, jsonify
from pdfminer.high_level import extract_text
import os
import tempfile

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload_file():
    # 检查请求中是否有文件
    if 'file' not in request.files:
        return jsonify(error="没有文件部分"), 400
    file = request.files['file']

    # 如果用户没有选择文件，浏览器也会提交一个没有文件名的空部分
    if file.filename == '':
        return jsonify(error="没有选择文件"), 400

    if file:
        # 将文件保存到临时文件
        with tempfile.NamedTemporaryFile(delete=False) as temp:
            temp.write(file.read())
            temp.seek(0)

        # 使用 pdfminer.six 解析 PDF 文件
        text = extract_text(temp.name)

        # 返回解析的文本
        return jsonify(text=text), 200


if __name__ == '__main__':
    app.run(port=12345, debug=True)  # 使用固定的端口号