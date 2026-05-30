# 中文文本分词与词频统计工具

基于 jieba 分词库的中文文本处理工具，支持分词、词频统计和关键词提取功能。

## 功能特性

- 中文文本分词
- 词频统计与排序
- 停用词过滤
- 关键词提取（TF-IDF 算法）
- 词性标注

## 文件说明

| 文件 | 说明 |
|------|------|
| `example1.py` | 词频统计示例，支持停用词过滤 |
| `example2.py` | 关键词提取示例，使用 TF-IDF 算法 |
| `excludeWord.txt` | 停用词列表 |
| `keyWords_Freq.txt` | 输出的关键词词频结果 |

## 环境要求

- Python 3.x
- jieba

## 安装依赖

```bash
pip install jieba
```

## 使用方法

### 词频统计 (example1.py)

```bash
python example1.py
```

运行后输入要提取的关键词数量，程序会将结果保存到 `keyWords_Freq.txt`。

### 关键词提取 (example2.py)

```bash
python example2.py
```

使用 TF-IDF 算法自动提取文本中的关键词。

## 示例输出

```
音乐    9
梦想    8
亡灵    8
世界    8
亲情    5
追求    4
死亡    4
```

## 自定义停用词

编辑 `excludeWord.txt` 文件，每行添加一个停用词即可。

## 许可证

MIT License
