# 流式数据处理
class StreamProcessor:
    """流式数据处理"""

    def __init__(self, data_stream):
        self.data_stream = data_stream

    def __iter__(self):
        return self

    def filter_valid(self):
        # 过滤有效数据
        return filter(lambda x: x is not None and x != "", self.data_stream)

    def transform_data(self):
        # 转换数据
        return map(str.upper, self.filter_valid())

    def batch_process(self, batch_size=1000):
        batch = []
        transform_data = self.transform_data()
        for item in transform_data:
            batch.append(item)
            if len(batch) >= batch_size:
                yield batch
                batch = []
        if batch:
            yield batch

    def process(self):
        # 处理流水线
        total_processed = 0
        for batch in self.batch_process(3):
            total_processed += len(batch)
            print(f"处理批次：{batch}")
        print(f"总共处理：{total_processed} 条记录")


def data_stream():
    data = ["hello", "", "world", None, "python", "stream", "", "processing"]
    for item in data:
        yield item


processor = StreamProcessor(data_stream())
processor.process()

# 最佳实践
# 使用迭代器处理大数据集
