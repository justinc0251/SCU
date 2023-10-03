// Justin Chung
// COEN 79 Lab 7
// FILE: company.cpp
// CLASS implemented: company (see company.h for documentation)

#include <cassert>
#include "company.h"

// #define USEDEBUG

#ifdef USEDEBUG
#define Debug(x) std::cout << x
#else
#define Debug(x)
#endif

namespace coen79_lab7
{
    // Postcondition: The company object is initialized with empty company name
    company::company()
    {
        this->company_name = "";
        this->head_ptr = NULL;
        this->tail_ptr = NULL;
    }

    // Precondition: company_name is a non-empty string
    // Postcondition: The company object is initialized with "company_name"
    company::company(const std::string &company_name)
    {
        assert(company_name.length() > 0);
        this->company_name = company_name;
        this->head_ptr = NULL;
        this->tail_ptr = NULL;
    }

    // Postcondition: creates a new company using source company's attributes
    company::company(const company &src)
    {
        Debug("Company copy constructor..." << std::endl);
        *this = src;
    }

    // Postcondition: returns a new company with the attributes of the source company object
    company &company::operator=(const company &src)
    {
        Debug("Company assignemnt operator..." << std::endl);

        if (this == &src)
        {
            return *this;
        }
        this->company_name = src.company_name;
        list_copy(src.get_head(), head_ptr, tail_ptr);
        return *this;
    }

    // Postcondition: deletes all nodes in the linked list of the company object
    company::~company()
    {
        list_clear(head_ptr);
    }

    // Postcondition: returns the name of the company object
    std::string company::get_name() const
    {
        return company_name;
    }

    // Postcondition: constant version of get_head()
    const node *company::get_head() const
    {
        return head_ptr;
    }

    // Postcondition: constant version of get_tail()
    const node *company::get_tail() const
    {
        return tail_ptr;
    }

    // Postcondition: returns the head pointer of the linked list of the company object
    node *company::get_head()
    {
        return head_ptr;
    }

    // Postcondition: returns the tail pointer of the linked list of the company object
    node *company::get_tail()
    {
        return tail_ptr;
    }

    // Postcondition: prints the name of the company object and the linked list of products
    void company::print_items()
    {
        list_print(head_ptr);
    }

    // Precondition: product_name is a non-empty string
    // Postcondition: Creates and inserts a new node (product) to the back of the linked list.
    // Returns true if successfully inserted, and returns false if there is a duplicate
    bool company::insert(const std::string &product_name, const float &price)
    {

        assert(product_name.length() > 0);

        if (list_contains_item(head_ptr, product_name))
        {
            return false;
        }
        if (head_ptr == NULL)
        {
            list_init(this->head_ptr, this->tail_ptr, product_name, price);
        }
        else
        {
            list_tail_insert(this->tail_ptr, product_name, price);
        }

        return true;
    }

    // Postcondition:  Erases the product that its name matches product_name. Returns true if the
    // product has been found and deleted, returns false otherwise
    bool company::erase(const std::string &product_name)
    {
        assert(product_name.length() > 0);

        if (list_contains_item(this->head_ptr, product_name))
        {
            node *precur = head_ptr;
            node *temp = list_search(head_ptr, product_name);
            while (precur->getLink() != temp)
            {
                precur = precur->getLink();
            }
            precur->setLink(temp->getLink());
            delete temp;
            return true;
        }
        return false;
    }
}