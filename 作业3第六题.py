class B:
    def handle(self):
        print("B 的 handle 方法被调用")

class A(B):
    def handle(self):
        super().handle()
        print("A 的 handle 方法被调用")

instance_a = A()
instance_a.handle()
