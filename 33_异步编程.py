# 性能对比
import random
import time
import asyncio
import logging
# # 同步版本
# def sync_demo():
#     def task(name, delay):
#         print(f"{name}开始")
#         time.sleep(delay)
#         print(f"{name}完成")
#     start = time.time()
#     task("任务1",2)
#     task("任务2", 1)
#     print(f"总耗时：{time.time() - start:.2f}秒")
#
# # 异步版本
# async def async_demo():
#     async def task(name, delay):
#         print(f"{name}开始")
#         await asyncio.sleep(delay)
#         print(f"{name}完成")
#     start = time.time()
#     await asyncio.gather(task("任务1", 2), task("任务2", 1))
#     print(f"总耗时：{time.time() - start:.2f}秒")
#
# print(f"=== 同步版本 ===")
# sync_demo()
#
# print(f"=== 异步版本 ===")
# asyncio.run(async_demo())

# async def simple_coroutine():
#     print("协程开始执行")
#     await asyncio.sleep(1)
#     print("协程结束")
#     return "协程结果"
#
# async def coroutine_usage():
#     print("=== 直接等待 ===")
#     result = await simple_coroutine()
#     print(f"结果：{result}")
#
#     print("=== 创建任务 ===")
#     task = asyncio.create_task(simple_coroutine())
#     result = await task
#     print(f"任务结果：{result}")
#
#     print("\n===并发执行 ===")
#     tasks = [
#         simple_coroutine(),
#         simple_coroutine(),
#         simple_coroutine()
#     ]
#     results = await asyncio.gather(*tasks)
#     print(f"所有结果：{results}")
#
# asyncio.run(coroutine_usage())

# 获取事件循环
# loop = asyncio.get_event_loop()
# print(f"事件循环：{loop}")
# print(f"循环是否运行：{loop.is_running()}")
# print(f"循环是否关闭：{loop.is_closed()}")
#
# async def simple_task():
#     await asyncio.sleep(1)
#     return "任务完成"
#
# loop = asyncio.get_event_loop()
# try:
#     if not loop.is_running():
#         result = loop.run_until_complete(simple_task())
#         print(f"手动执行结果：{result}")
# finally:
#     loop.close()

# async/await关键字
# class AsyncExample():
#     async def io_operation(self, name, delay):
#         """模拟I/O操作"""
#         print(f"{name}:开始I/O操作，需要{delay}秒")
#         await asyncio.sleep(delay)
#         print(f"{name}: I/O操作完成")
#         return f"{name}_result"
#
#     async def concurrent_operations(self):
#         """并发操作示例"""
#         tasks = [
#            self.io_operation(f"任务{i}",i) for i in range(1,4)
#         ]
#         print("=== 并发I/O操作 ===")
#         results = await asyncio.gather(*tasks)
#         print(f"并发结果: {results}")
#
# examples = AsyncExample()
# asyncio.run(examples.concurrent_operations())

# class AsyncDatabaseConnection:
#     async def __aenter__(self):
#         print("建立数据库链接...")
#         await asyncio.sleep(0.5)
#         print("数据库连接已建立")
#         return self
#
#     async def __aexit__(self, exc_type, exc_val, exc_tb):
#         print("关闭数据库连接...")
#         await asyncio.sleep(0.2)
#         print("数据库连接已关闭")
#         return False
#     async def execute_query(self,query):
#         print(f"执行查询: {query}")
#         await asyncio.sleep(0.3)
#         return f"查询结果: {query}"
#
# async def async_context():
#     async with AsyncDatabaseConnection() as db:
#         result = await db.execute_query("SELECT * FROM users")
#         print(result)
#
# asyncio.run(async_context())
# 异步迭代器
# class AsyncDataStream:
#     """异步数据流"""
#
#     def __init__(self, data_list, delay=0.5):
#         self.data = data_list
#         self.delay = delay
#         self.index = 0
#     def __aiter__(self):
#         return self
#     async def __anext__(self):
#         if self.index >= len(self.data):
#             raise StopAsyncIteration
#         item = self.data[self.index]
#         self.index += 1
#         await asyncio.sleep(self.delay)
#         return item
# async def async_iterator():
#     """异步迭代器演示"""
#     data_list = ["数据1", "数据2", "数据3", "数据4"]
#     stream = AsyncDataStream(["数据1", "数据2", "数据3", "数据4"],0.3)
#     print("使用异步for循环")
#     async for item in stream:
#         print(f"接收到: {item}")
#     print("\n使用异步推导式:")
#     stream2 = AsyncDataStream(["A", "B", "C", "D"], 0.2)
#     results = [item async for item in stream2]
#     print(f"所有数据: {results}")
#
# asyncio.run(async_iterator())

# 任务和Future

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
#
#
# class TaskManager:
#     """任务管理器"""
#
#     def __init__(self):
#         self.tasks = set()
#
#     async def worker(self, name, duration):
#         """工作协程"""
#         logging.info(f"任务 {name} 开始")
#         try:
#             await asyncio.sleep(duration)
#             logging.info(f"任务 {name} 完成")
#             return f"{name}_result"
#         except asyncio.CancelledError:
#             logging.info(f"任务 {name} 被取消")
#             raise
#
#     async def create_tasks(self, count):
#         """创建多个任务"""
#         for i in range(count):
#             task = asyncio.create_task(
#                 self.worker(f"worker_{i}", i + 1),
#                 name=f"task_{i}"
#             )
#             self.tasks.add(task)
#             task.add_done_callback(self.tasks.discard)
#
#         logging.info(f"创建了 {count} 个任务")
#
#     async def monitor_tasks(self):
#         """监控任务状态"""
#         while True:
#             running_tasks = [t for t in self.tasks if not t.done()]
#             logging.info(f"运行中的任务: {len(running_tasks)}")
#
#             if not running_tasks:
#                 break
#
#             await asyncio.sleep(0.5)
#
#     async def cancel_all_tasks(self):
#         """取消所有任务"""
#         logging.info("取消所有任务")
#         for task in self.tasks:
#             task.cancel()
#
#         await asyncio.gather(*self.tasks, return_exceptions=True)
#
#
# async def task_management():
#     """任务管理演示"""
#     manager = TaskManager()
#
#     await manager.create_tasks(5)
#     monitor_task = asyncio.create_task(manager.monitor_tasks())
#
#     await asyncio.sleep(2)
#     await manager.cancel_all_tasks()
#
#     await monitor_task
#
#
# asyncio.run(task_management())

# async def future_example():
#     """Future 对象示例"""
#
#     # 创建一个Future对象
#     future = asyncio.Future()
#     print(f"Future初始状态: {future.done()}")
#
#     async def set_future_result():
#         print("set_future_result")
#         await asyncio.sleep(3)
#         if not future.done():
#             future.set_result("Future结果")
#             print("Future结果已设置")
#
#     async def use_future():
#         print("等待Future结果...")
#         result = await future
#         print(f"收到Future结果: {result}")
#         return result
#
#     # 并发执行设置和获取Future结果
#     results = await asyncio.gather(
#         set_future_result(),
#         use_future()
#     )
#
#     print(f"所有操作完成: {results}")
#
#
# asyncio.run(future_example())

class AsyncProducerConsumer:
    """异步生产者-消费者"""
    def __init__(self,queue_size = 5):
        self.queue = asyncio.Queue(maxsize=queue_size)
        self.producers = []
        self.consumers = []
    async def producer(self,name,count):
        for i in range(count):
            item = f"{name}_item_{i}"
            production_time = random.uniform(0.1,0.5)
            await asyncio.sleep(production_time)

            await self.queue.put(item)
            print(f"生产者 {name} 生产了: {item} (队列大小: {self.queue.qsize()})")
        print(f"生产者 {name} 完成")

    async def consumer(self,name):
        """消费者"""
        while True:
            try:
                item = await asyncio.wait_for(self.queue.get(),timeout=2.0)
                consumption_time = random.uniform(0.2,0.8)

                await asyncio.sleep(consumption_time)
                print(f"消费者 {name} 消费了: {item} (队列大小: {self.queue.qsize()})")
                self.queue.task_done()
            except asyncio.TimeoutError:
                print(f"消费者 {name} 超时，退出")
                break
    async def run(self,producer_count=2,items_per_producer=5,consumer_count=3):
        """运行生产者-消费者系统"""
        print("启动生产者-消费者系统...")
        # 创建生产者任务
        for i in range(producer_count):
            producer_task = asyncio.create_task(
                self.producer(f"P{i}", items_per_producer)
            )
            self.producers.append(producer_task)

        # 创建消费者任务
        for i in range(consumer_count):
            consumer_task = asyncio.create_task(self.consumer(f"C{i}"))
            self.consumers.append(consumer_task)

        # 等待所有生产者完成
        await asyncio.gather(*self.producers)
        print("所有生产者已完成")

        # 等待队列中所有项目被消费
        await self.queue.join()
        print("队列已清空")

        # 取消所有消费者任务
        for consumer in self.consumers:
            consumer.cancel()

        await asyncio.gather(*self.consumers, return_exceptions=True)
        print("所有消费者已结束")

# 使用示例
system = AsyncProducerConsumer()
asyncio.run(system.run())