package structures;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class OrderedList<T extends Comparable<T>> implements OrderedSequence<T>, Iterable<T> {
    private Node<T> head;
    private int size = 0;

    @Override
    public void insert(T el) {
        if (el == null) throw new NullPointerException("Element cannot be null.");
        if (search(el)) throw new IllegalArgumentException("Duplicate elements are not allowed.");
        
        Node<T> newNode = new Node<>(el);
        if (head == null || head.data.compareTo(el) > 0) {
            newNode.next = head;
            head = newNode;
        } else {
            Node<T> current = head;
            while (current.next != null && current.next.data.compareTo(el) < 0) {
                current = current.next;
            }
            newNode.next = current.next;
            current.next = newNode;
        }
        size++;
    }

    @Override
    public void remove(T el) {
        if (head == null) throw new NoSuchElementException("The list is empty.");
        if (head.data.equals(el)) {
            head = head.next;
            size--;
            return;
        }
        
        Node<T> current = head;
        while (current.next != null && !current.next.data.equals(el)) {
            current = current.next;
        }
        if (current.next == null) throw new NoSuchElementException("Element not found.");
        current.next = current.next.next;
        size--;
    }

    @Override
    public T min() {
        if (head == null) throw new NoSuchElementException("The list is empty.");
        return head.data;
    }

    @Override
    public T max() {
        if (head == null) throw new NoSuchElementException("The list is empty.");
        Node<T> current = head;
        while (current.next != null) {
            current = current.next;
        }
        return current.data;
    }

    @Override
    public boolean search(T el) {
        Node<T> current = head;
        while (current != null) {
            if (current.data.equals(el)) return true;
            current = current.next;
        }
        return false;
    }

    @Override
    public T at(int pos) {
        if (pos < 0 || pos >= size) throw new IndexOutOfBoundsException("Invalid index.");
        Node<T> current = head;
        for (int i = 0; i < pos; i++) {
            current = current.next;
        }
        return current.data;
    }

    @Override
    public int index(T el) {
        Node<T> current = head;
        int index = 0;
        while (current != null) {
            if (current.data.equals(el)) return index;
            current = current.next;
            index++;
        }
        throw new NoSuchElementException("Element not found.");
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public Iterator<T> iterator() {
        return new OrderedListIterator();
    }

    private class Node<E extends Comparable<E>> {
        private E data;
        private Node<E> next;

        Node(E data) {
            this.data = data;
        }
    }

    private class OrderedListIterator implements Iterator<T> {
        private Node<T> current = head;
        private Node<T> lastReturned = null;

        @Override
        public boolean hasNext() {
            return current != null;
        }

        @Override
        public T next() {
            if (!hasNext()) throw new NoSuchElementException();
            lastReturned = current;
            current = current.next;
            return lastReturned.data;
        }

        @Override
        public void remove() {
            if (lastReturned == null) throw new IllegalStateException("Remove operation cannot be performed.");
            OrderedList.this.remove(lastReturned.data);
            lastReturned = null;
        }
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder("[");
        Node<T> current = head;
        while (current != null) {
            sb.append(current.data).append(current.next != null ? ", " : "");
            current = current.next;
        }
        sb.append("]");
        return sb.toString();
    }
}
