<template>
  <div class="word-frequency-app">
    <header>
      <!-- 应用标题和菜单 -->
    </header>
    <aside>
      <!-- PDF 文件npm install pdfjs-dist列表 -->
    </aside>
    <main>
      <!-- PDF 预览和词频分析结果 -->
      <pdf-viewer :pdf="selectedPdf" />
      <word-frequency-list :words="wordFrequencies" />
    </main>
    <footer>
      <!-- 状态信息显示 -->
    </footer>
  </div>
</template>

<script>
// 导入组件
import PdfViewer from './components/PdfViewer.vue';
import WordFrequencyList from './components/WordFrequencyList.vue';

export default {
  components: {
    PdfViewer,
    WordFrequencyList
  },
  data() {
    return {
      selectedPdf: null,
      wordFrequencies: []
    };
  },
  methods: {
    // 方法：加载 PDF 和分析词频
  }
};
</script>