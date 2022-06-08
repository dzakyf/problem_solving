class Queues:
    def __init__(self):
        self.inbox = []
        self.outbox = []

    def push(self, data):
        self.inbox.append(data)

    def pop(self):
        self.peek()
        return self.outbox.pop()
    
    def peek(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        
        return self.outbox[-1]

    def empty(self):
        return not self.inbox and not self.outbox


def main():
    obj = Queues()
    obj.push(1)
    obj.push(2)
    param_3 = obj.peek()
    param_2 = obj.pop()
    param_4 = obj.empty()
    
    print(param_2,param_3,param_4)

if __name__ == '__main__':
    main()
