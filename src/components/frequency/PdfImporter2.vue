<template>
  <div class="pdf-importer">
    <h1>导入 PDF 文件</h1>
    <input type="file" @change="handleFileUpload" />
    <button @click="uploadPdf">上传 PDF</button>
    <div v-if="selectedFile" class="file-info">
      已选择文件: {{ selectedFile.name }} ({{ selectedFile.size }} 字节)
    </div>
    <div v-if="textFromServer">
      <h2>解析结果:</h2>
      <pre>{{ textFromServer }}</pre>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PdfImporter',
  data() {
    return {
      selectedFile: null,
      textFromServer: null,
    };
  },
  methods: {
    handleFileUpload(event) {
      const files = event.target.files;
      if (files && files.length > 0) {
        this.selectedFile = files[0];
      }
    },
    uploadPdf() {
      if (this.selectedFile) {
        const formData = new FormData();
        formData.append('file', this.selectedFile);

        fetch('http://localhost:12345/upload', {
          method: 'POST',
          body: formData,
        })
            .then(response => response.json())
            .then(data => {
              if (data.error) {
                alert(data.error);
              } else {
                this.textFromServer = data.text;
              }
            })
            .catch(error => {
              console.error('上传时出错:', error);
            });
      }
    },
  },
};
</script>

<!-- 样式保持不变 -->

<style scoped>
.pdf-importer {
  max-width: 400px;
  margin: 50px auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  text-align: center;
}

.pdf-importer input[type="file"] {
  margin-top: 20px;
}

.file-info {
  margin-top: 20px;
  font-size: 0.9em;
  color: #666;
}
</style>