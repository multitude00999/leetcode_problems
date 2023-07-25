class queueFromList:
	def __init__(self, k):
		"""
		initialize queue of size k
		"""
		self.size = k
		self.data = []

	def enqueue(self, value):
		"""
		perform enqueue operation
		"""
		if self.isFull():
			return False

		self.data.append(value)
		print("element inserted in queue: ", value)
		return True

	def dequeue(self):
		"""
		perform dequeque operation
		"""
		if self.isEmpty():
			return False
		print("element popped from queue: ", self.data.pop(0))
		return True

	def isFull(self):
		"""
		check if the queue has reached the maximum size
		"""
		if len(self.data) >= self.size:
			print("queue is full")
			return True
		return False

	def isEmpty(self):
		"""
		check if the queue is empty
		"""
		if len(self.data) == 0:
			print("queue is empty")
			return True

		return False

if __name__ == "__main__":
	q = queueFromList(10)
	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)
	q.enqueue(4)
	q.dequeue()
	q.dequeue()
	q.dequeue()
	q.dequeue()
	q.dequeue()

