# Creating Queues using Class
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
         print("Queue is empty")
         return
        ele = self.queue.pop(0)
        print("Dqeued element:",ele)

    def peek(self):
        if self.is_empty():
         print("Queue is empty")
         return
        peek_ele = self.queue[0]
        print("Peek_element:",peek_ele)

    def is_empty(self):
        return len(self.queue)==0
    
queue1 = Queue()
queue1.dequeue()
queue1.enqueue("Ayush")
queue1.enqueue("Piyush")
queue1.enqueue("Shubham")
queue1.enqueue("Golu")
print(queue1.queue)
queue1.peek()
queue1.dequeue()
queue1.peek()
