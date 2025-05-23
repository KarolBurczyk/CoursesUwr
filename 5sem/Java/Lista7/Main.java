import structures.OrderedList;

public class Main {
    public static void main(String[] args) {
        OrderedList<Integer> intList = new OrderedList<>();
        intList.insert(5);
        intList.insert(2);
        intList.insert(10);
        System.out.println("Integer List: " + intList);
        System.out.println("Min: " + intList.min());
        System.out.println("Max: " + intList.max());
        System.out.println("Contains 10? " + intList.search(10));
        System.out.println("Element at index 1: " + intList.at(1));
        intList.remove(5);
        System.out.println("After removing 5: " + intList);

        System.out.println("\nIterating Integer List:");
        for (int num : intList) {
            System.out.println(num);
        }

        OrderedList<String> stringList = new OrderedList<>();
        stringList.insert("Apple");
        stringList.insert("Orange");
        stringList.insert("Banana");
        System.out.println("\nString List: " + stringList);
    }
}
