#include <iostream>

using namespace std;

class link {
    public:
        link *next;
        int data;

};

link *add(link **head, int data){
    link *newNode = (link*) malloc(sizeof(link));
    newNode->data = data;
    newNode->next = *head;
    return newNode;
}

link *remove(link *head, link *next){
    free(head);
    return next;
}

int main(){
    link *head;
    link node1;

    node1.data = 1;
    node1.next = NULL;
    head = &node1;

    head = add(&head, 2);

    head = add(&head, 3);

    link cur = *head;

    while(cur.next != NULL){
        cout << cur.data << "  ";
        cur = *cur.next;
    }

    cout << cur.data << endl;

    head = remove(head, head->next);
    cout<< head->data << endl;

    head = remove(head, head->next);

    cout<< head->data << endl;
}