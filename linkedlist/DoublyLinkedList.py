class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None, None)

    def insert_at_beginning(self, data):
        node = Node(data, None, self.head)
        self.head.prev = node
        self.head = node

    def insert_at(self, index, data):

        if index < 0 or index > self.get_length():
            print('Index out of bounds')
            return

        if self.head.next is None or index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr, itr.next)
                old_next_node = itr.next
                itr.next = node
                old_next_node.prev = node
                break

            count += 1
            itr = itr.next

    def insert_after_value(self, data_after, data_to_insert):

        itr = self.head
        inserted = False
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr, itr.next)
                old_next_node = itr.next
                itr.next = node
                old_next_node.prev = node
                inserted = True
                break

            itr = itr.next

        if not inserted:
            print(f'{data_after} does not exist')

    def insert_at_end(self, data):
        itr = self.head

        while itr.next.next:
            itr = itr.next

        node = Node(data, itr, None)
        itr.next = node

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_beginning(data)

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            print('Index out of bounds')
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                rmv_next_node = itr.next.next
                itr.next = rmv_next_node
                rmv_next_node.prev = itr
                break

            count += 1
            itr = itr.next

    def remove_by_value(self, data):
        itr = self.head
        removed = False
        if self.head.next is None or index == 0:
            self.remove_at_beginning(data)
            return
        while itr:
            if itr.data == data:
                rmv_next_node = itr.next
                rmv_prev_node = itr.prev
                tmp = rmv_prev_node
                rmv_prev_node.next = rmv_next_node
                rmv_next_node.prev = tmp
                removed = True
                break

            itr = itr.next

        if not removed:
            print(f'{data} does not exist')

    def remove_at_beginning(self):
        self.head = self.head.next

    def remove_at_end(self):
        itr = self.head

        while itr.next.next:
            itr = itr.next

        itr.next = None

    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count

    def print_forward(self):

        if self.head.next is None:
            print('DLL is empty')
            return

        itr = self.head
        dll = ''
        while itr:
            dll += str(itr.data) + '<-->' if itr.next else str(itr.data)
            itr = itr.next

        print(dll)

    def print_backward(self):

        if self.head.next is None:
            print('DLL is empty')
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        # now the itr is at the tail node
        dll_rev = ''
        while itr:
            dll_rev += str(itr.data) + '<-->' if itr.prev else str(itr.data)
            itr = itr.prev

        print(dll_rev)


if __name__ == '__main__':
    ll = DoublyLinkedList()

    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0, "jackfruit")
    ll.print_forward()
    # ll.insert_at(6, "dates")
    # ll.print_forward()
    ll.insert_at(2, "kiwi")
    ll.print_forward()

    # dll.insert_at_beginning(2)
    # dll.insert_at_beginning(4)
    # dll.insert_at_beginning(6)
    # dll.insert_at_beginning(8)

    # dll.print_forward()

    # dll.insert_at(50, 2)
    # dll.insert_at(100, 4)

    # dll.print_forward()

    # dll.insert_after_value(6, 25)

    # dll.print_forward()

    # dll.insert_at_end("fruity")

    # dll.print_forward()

    # dll.print_backward()

    # dll.insert_values([12, 13, 14, 15, 16])

    # dll.print_forward()

    # dll.remove_at(2)

    # dll.print_forward()

    # dll.remove_at_beginning()

    # dll.print_forward()

    # dll.remove_at_end()

    # dll.print_forward()

    # dll.remove_by_value(6)

    # dll.print_forward()
