/**
设计一个支持在平均 时间复杂度 O(1) 下，执行以下操作的数据结构。
insert(val)：当元素 val 不存在时，向集合中插入该项。
remove(val)：元素 val 存在时，从集合中移除该项。
getRandom：随机返回现有集合中的一项。每个元素应该有相同的概率被返回。

示例 :
// 初始化一个空的集合。
RandomizedSet randomSet = new RandomizedSet();
// 向集合中插入 1 。返回 true 表示 1 被成功地插入。
randomSet.insert(1);
// 返回 false ，表示集合中不存在 2 。
randomSet.remove(2);
// 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
randomSet.insert(2);
// getRandom 应随机返回 1 或 2 。
randomSet.getRandom();
// 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
randomSet.remove(1);
// 2 已在集合中，所以返回 false 。
randomSet.insert(2);
// 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
randomSet.getRandom();
*/

#include <iostream>
#include <list>
#include <map>
#include <cstdlib>
#include <ctime>
using namespace std;

class MyListNode {
    public:
        int val;
        MyListNode* last;
        MyListNode* next;
        MyListNode() {}
        MyListNode(int i) {
            val = i;
        }
};

class RandomizedSet {

private:
    MyListNode* listHead;
    MyListNode* listTail;
    int size;
    map<int, MyListNode*> numsIndexMap;

public:
    /** Initialize your data structure here. */
    RandomizedSet() {
        map<int, MyListNode*> emptyMap;
        listHead = NULL;
        listTail = NULL;
        size = 0;
        numsIndexMap.swap(emptyMap);
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if(numsIndexMap.find(val) != numsIndexMap.end()) {
            return false;
        }else {
            MyListNode* node = new MyListNode(val);
            if(listHead == NULL) {
                listHead = node;
                listTail = node;
            }else {
                listTail -> next = node;
                node -> last = listTail;
                listTail = node;
            }
            numsIndexMap[val] = node;
            size++;
            return true;
        }
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        if(numsIndexMap.find(val) != numsIndexMap.end()) {
            if(size == 1) {
                listHead = NULL;
                listTail = NULL;
            }else {
                MyListNode* node = numsIndexMap[val];
                if(node -> last == NULL) {
                    listHead = node -> next;
                }else if(node -> next == NULL) {
                    listTail = node -> last;
                }else {
                    node -> last = node -> next;
                }
            }
            numsIndexMap.erase(val);
            size--;
            return true;
        }else {
            return false;
        }
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        int r = rand();
        int index = r % size;
        map<int, MyListNode*>::iterator iter = numsIndexMap.begin();
        for(int i = 0 ; i < index ; i++) {
            iter++;
        }
        return iter -> first;
    }
};

int main() {
    // ["RandomizedSet","remove","remove","insert","getRandom","remove","insert"]
    // [[],[0],[0],[0],[],[0],[0]]
    // ["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]
    // [[],[1],[2],[2],[],[1],[2],[]]
    // ["RandomizedSet","insert","insert","remove","insert","remove","getRandom"]
    // [[],[0],[1],[0],[2],[1],[]]
    RandomizedSet* randomizedSet = new RandomizedSet();
    cout << randomizedSet -> insert(0) << '\n';
    cout << randomizedSet -> insert(1) << '\n';
    cout << randomizedSet -> remove(0) << '\n';
    cout << randomizedSet -> insert(2) << '\n';
    cout << randomizedSet -> remove(1) << '\n';
    cout << randomizedSet -> getRandom() << '\n';

    // randomizedSet -> insert(0);
    // randomizedSet -> insert(1);
    // randomizedSet -> remove(0);
    // randomizedSet -> insert(2);
    // randomizedSet -> remove(1);
    // randomizedSet -> getRandom();
    return 0;
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */