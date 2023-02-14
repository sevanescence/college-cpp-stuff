#include <iostream>

template <typename T>
class List {
public:
    List() = default;

    ~List() {
        if (m_top != nullptr) {
            auto it = m_top;
            while (it->next != nullptr) {
                auto tmp = it;
                it = it->next;
                delete tmp;
            }
            delete it;
        }
    }

    void push_back(T value) {
        if (m_top == nullptr) {
            m_top = new Node { nullptr, std::move(value) };
            return;
        }

        auto it = m_top;
        while (it->next != nullptr) {
            it = it->next;
        }

        it->next = new Node { nullptr, std::move(value) };
    }

    void push_front(T value) {
        if (m_top == nullptr) {
            m_top = new Node { nullptr, std::move(value) };
            return;
        }

        m_top = new Node { m_top, std::move(value) };
    }

    T pop_front() {
        if (m_top == nullptr) {
            throw "List is empty";
        }

        auto value = std::move(m_top->value);

        auto next = m_top->next;
        delete m_top;
        m_top = next;

        return value;
    }

    T pop_back() {
        if (m_top == nullptr) {
            throw "List is empty.";
        }

        if (m_top->next == nullptr) {
            auto value = std::move(m_top->value);
            delete m_top;
            m_top = nullptr;
            return value;
        }

        auto it = m_top;
        while (it->next->next != nullptr) {
            it = it->next;
        }
        auto value = std::move(it->next->value);
        delete it->next;
        it->next = nullptr;

        return value;
    }

    bool empty() const {
        return m_top == nullptr;
    }
private:
    struct Node {
        Node *next;
        T value;
    };

    Node *m_top;
};

class Test {
public:
    Test() { std::cout << "Test()\n"; }
    ~Test() { std::cout << "~Test()\n"; }

    Test(Test &&other) { }
    Test &operator=(Test &&other) { return *this; }
};

// TODO write assertion function, comment code
int main() {
    auto list = List<int> { };
    list.push_back(2);
    list.push_back(3);
    list.push_front(1);

    while (!list.empty()) {
        std::cout << list.pop_front() << ", ";
    } std::endl(std::cout);

    auto test_list = List<Test> { };
    test_list.push_back(Test { });
    auto test = test_list.pop_back();
    std::cout << test_list.empty() << '\n';

    std::cout << "End of program.\n";
}
