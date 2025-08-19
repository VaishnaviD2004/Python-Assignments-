class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue (insert element at end)
    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} added to queue")

    # Dequeue (remove element from front)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"

    # Peek at front element
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"

    # Check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Display queue
    def display(self):
        print("Queue:", self.queue)


# Example usage
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

print("Front element is:", q.peek())
print("Dequeued element:", q.dequeue())
q.display()
