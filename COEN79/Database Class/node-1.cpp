// Justin Chung
// COEN 79 Lab 7

#ifndef ITEM_CPP
#define ITEM_CPP

#include "node.h"

namespace coen79_lab7
{
    // Postcondition: The node contains the specified name, price and link values.
    node::node(const std::string &itemName, const float &newPrice, node *nextNode)
    {
        name = itemName;
        price = newPrice;
        link = nextNode;
    }
    // Precondition: product_name is a non-empty string
    // Postcondition:  Sets the name field of the node
    void node::setName(const std::string &newName)
    {
        name = newName;
    }

    // Postcondition: Sets the price field of the node
    void node::setPrice(const float &newPrice)
    {
        price = newPrice;
    }

    // Postcondition: Sets the link field of the node
    void node::setLink(node *new_next)
    {
        link = new_next;
    }

    // Postcondition: The return value is the link from this node.
    node *node::getLink()
    {
        return link;
    }

    // Postcondition: The return value is the link from this node.
    const node *node::getLink() const
    {
        return link;
    }

    // Postcondition: Returns the name field of the node
    std::string node::getName() const
    {
        return name;
    }

    // Postcondition: Returns the price field of the node
    float node::getPrice() const
    {
        return price;
    }

    // Precondition: newName is a non_empty string
    // Postcondition:  initializes an empty list (where head and tail are NULL).
    // Takes in a head and tail pointer,  creates a new node, and modifies the head
    // and tail pointer to point to the new node
    void list_init(node *&head, node *&tail, const std::string &newName, const float &newPrice)
    {
        head = new node(newName, newPrice, NULL);
        tail = head;
    }

    // Precondition: tail_ptr is the tail pointer of a non-empty linked list,
    // newName is a non_empty string
    // Postcondition: Adds a node to the end of the linked list.
    void list_tail_insert(node *&tail, const std::string &newName, const float &newPrice)
    {
        if (tail == NULL)
        {
            return;
        }

        node *new_node = new node(newName, newPrice, NULL);
        tail->setLink(new_node);
        tail = tail->getLink();
    }

    // Precondition: head_ptr is the head pointer of a linked list.
    // Postcondition: All nodes of the list have been returned to the heap,
    // and the head_ptr is now NULL.
    void list_clear(node *&head)
    {
        if (head == NULL) // empty list
        {
            return;
        }

        while (head != NULL) // while there is still existing nodes in the list
        {
            list_head_remove(head);
        }
    }

    // Precondition: source_ptr is the head pointer of a linked list.
    // Postcondition: head_ptr and tail_ptr are the head and tail pointers for
    // a new list that contains the same items as the list pointed to by
    // source_ptr. The original list is unaltered.
    void list_copy(const node *old_head, node *&new_head, node *&new_tail)
    {
        new_head = NULL;
        new_tail = new_head;

        const node *cur = old_head;
        while (cur != NULL)
        {
            if (new_head == NULL)
            {
                new_head = new node(cur->getName(), cur->getPrice());
                new_tail = new_head;
            }
            else
            {
                new_tail->setLink(new node(cur->getName(), cur->getPrice()));
                new_tail = new_tail->getLink();
            }
            cur = cur->getLink();
        }
    }

    // Precondition: head_ptr is the head pointer of a linked list, with at
    // least one node.
    // Postcondition: The head node has been removed and returned to the heap;
    // head_ptr is now the head pointer of the new, shorter linked list.
    void list_head_remove(node *&head)
    {
        if (head == NULL) // node is empty
        {
            return;
        }

        node *temp_node = head;
        head = head->getLink();
        delete temp_node;
    }

    // Precondition: head_ptr is the head pointer of a linked list.
    // Postcondition:  Prints the list.
    void list_print(node *head)
    {
        node *cur = head;
        while (cur != NULL) // iterates through whole list
        {
            std::cout << "- " << cur->getName() << ", where the price is $" << cur->getPrice() << std::endl;
            cur = cur->getLink();
        }
    }

    // Precondition: head_ptr is the head pointer of a linked list, and name is
    // a non-empty string
    // Postcondition:  Returns true if "name" is in the linked list,
    // returns false if the item is not in the linked list
    bool list_contains_item(node *head_ptr, const std::string &newName)
    {
        return (list_search(head_ptr, newName) != NULL);
    }

    // Precondition: head_ptr is the head pointer of a linked list, and name is
    // a non_empty string
    // Postcondition: The pointer returned points to the first node containing
    node *list_search(node *head_ptr, const std::string &target)
    {
        node *cursor;

        for (cursor = head_ptr; cursor != NULL; cursor = cursor->getLink()) // iterates through whole list
            if (target == cursor->getName())                                // target name exists in the linked list
                return cursor;
        return NULL;
    }

    // Precondition: head_ptr is the head pointer of a linked list, and name is
    // a non_empty string
    // Postcondition: The pointer returned points to the first node containing
    // the specified target in its data member. If there is no such node, the
    // null pointer is returned.
    const node *list_search(const node *head_ptr, const std::string &target)
    {
        const node *cursor;

        for (cursor = head_ptr; cursor != NULL; cursor = cursor->getLink()) //iterates through whole list
            if (target == cursor->getName()) // target name exists in the linked list
                return cursor;
        return NULL;
    }

}

#endif