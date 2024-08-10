<template>
  <div class="pdf-importer">
    <h1>导入 PDF 文件</h1>
    <input type="file" @change="handleFileUpload" />
    <div v-if="selectedFile" class="file-info">
      已选择文件: {{ selectedFile.name }} ({{ selectedFile.size }} 字节)
    </div>
  </div>
</template>

<script>
export default {
  name: 'PdfImporter',
  data() {
    return {
      selectedFile: null,
    };
  },
  methods: {
    handleFileUpload(event) {
      // 阻止默认行为，因为我们将手动处理文件
      event.preventDefault();

      // 获取文件输入元素中的文件对象
      const files = event.target.files;
      if (files && files.length > 0) {
        // 更新 selectedFile 数据属性
        this.selectedFile = files[0];
      }
    },
  },
};
</script>

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