export const menus = [
    {
        key: 'home',
        hidden: false,
        name: '首页',
        component: () => import('@/components/home/Index.vue'),
    },
    {
        key: 'test',
        hidden: false,
        name: '测试',
        component: () => import('@/components/test/Index.vue'),
    },
    {
        key: 'frequency',
        hidden: false,
        name: '词频分析',
        component: () => import('@/components/frequency/PdfImporter2.vue'),
    }
]