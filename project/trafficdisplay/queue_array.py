class QueueArray:
    def __init__(self) -> None:
        self.__capacity = 10
        self.__elements = [None] * self.__capacity
        self.__num_elements = 0
        self.__head = 0
        self.__tail = 0

    def _expand(self) -> None:
        if self.__head > self.__tail:
            self.__elements = \
                self.__elements[:self.__tail + 1] + \
                [None] * self.__capacity + self.__elements[self.__head:]
            self.__head = self.__head + self.__capacity

        else:
            self.__elements.extend([None] * self.__capacity)

        self.__capacity = self.__capacity * 2

    def enqueue(self, element: object) -> None:
        self.__elements[self.__tail] = element
        self.__num_elements = self.__num_elements + 1

        if self.__num_elements == self.__capacity:
            self._expand()

        self.__tail = (self.__tail + 1) % self.__capacity

    def dequeue(self) -> object:
        if self.is_empty():
            raise IndexError

        element = self.__elements[self.__head]
        self.__elements[self.__head] = None
        self.__head = (self.__head + 1) % self.__capacity
        self.__num_elements = self.__num_elements - 1

        return element

    def peek(self) -> object:
        if self.is_empty():
            raise IndexError

        return self.__elements[self.__head]

    def is_empty(self) -> bool:
        if self.__head == self.__tail:
            return True

        return False

    def size(self) -> int:
        return self.__num_elements
