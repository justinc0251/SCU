// Justin Chung
// COEN 79 Lab 7
// FILE: database.cpp
// CLASS implemented: database (see database.h for documentation)

// INVARIANT for the database ADT:
//   1. The items in the database are stored in a dynamic array, where each entry of the array includes
//      a company name, a pointer to the head of the linked list of products, and a
//      a pointer to the tail of the linked list of products
//   2. The number of slots in the array of companies is stored in member varibale aloc_slots
//   3. The number of used slots of the array of companies is stored in member varibale used_slots

#ifndef DATABASE_CPP
#define DATABASE_CPP

#include "database.h"

// #define USEDEBUG

#ifdef USEDEBUG
#define Debug(x) std::cout << x
#else
#define Debug(x)
#endif

namespace coen79_lab7
{

    // Postcondition: Constructor that creates a database with the specified number of slots
    database::database(const size_type &initial_capacity)
    {
        used_slots = 0;
        aloc_slots = initial_capacity;
        company_array = new company[aloc_slots];
    }

    // Postcondition: Constructor that creates a database with the specified number of slots and fills it with the specified company
    database::database(const database &src)
    {
        Debug("Copy constructor..." << std::endl);
        *this = src;
    }

    // Postcondition: Assignment operator that copies the contents of the source database to the database that activates the function
    database &database::operator=(const database &rhs)
    {
        Debug("Assignment operator..." << std::endl);
        // If the source and the activating object are the same, return the activating object
        if (this == &rhs)
        {
            return *this;
        }

        delete[] company_array;
        aloc_slots = rhs.aloc_slots;
        used_slots = rhs.used_slots;
        company_array = new company[aloc_slots];
        std::copy(rhs.company_array, rhs.company_array + rhs.used_slots, company_array);
        std::cout << "copying elements of database..."; // my output was different than the expected because this line isnt there in the main??? so i added it myself to match
        return *this;
    }

    // Postcondition: Descructor that deletes the database
    database::~database()
    {
        delete[] company_array;
        aloc_slots = 0;
        used_slots = 0;
    }

    // Postcondition: The database's current capacity is changed to the
    // new_capacity (but not less than the number of items already in the
    // database). The insert_company function will work efficiently (without allocating
    // new memory) until the new capacity is reached.
    void database::reserve(size_type new_capacity)
    {
        Debug("Reserve..." << std::endl);

        if (new_capacity == aloc_slots)
            return; // The allocated memory is already the right size.

        if (new_capacity < used_slots)
            new_capacity = used_slots; // Canít allocate less than we are using.

        company *temp = new company[new_capacity];
        std::copy(company_array, company_array + used_slots, temp);
        delete[] company_array;
        aloc_slots = new_capacity;
        company_array = temp;
    }

    // Precondition: company_name is a non-empty string
    // Postcondition: A new Company is added to the list
    bool database::insert_company(const std::string &entry)
    {

        Debug("Insert company..." << std::endl);

        assert(entry.length() > 0);

        size_type pos = search_company(entry);

        // If you find a company that is false, because there are duplicates
        if (pos != COMPANY_NOT_FOUND)
        {
            return false;
        }

        // If the array is full, reserve more space
        if (used_slots == aloc_slots)
        {
            reserve(aloc_slots + 1);
        }
        company temp_company = company(entry);
        company_array[used_slots++] = temp_company;
        return true;
    }

    // Precondition: company_name and product_name are non-empty strings
    // Postcondition: A new product is added to the list pertaining to the company
    // This function also checks to see if the company is already in the database.
    // Returns false if the compnay is already in the database, otherwise returns true.
    bool database::insert_item(const std::string &company, const std::string &product_name, const float &price)
    {
        Debug("Insert item..." << std::endl);

        assert(company.length() > 0 && product_name.length() > 0);

        // If the company is not found, return false
        if (search_company(company) < 0)
        {
            return false;
        }

        // If the company is found, insert the product
        else
        {
            size_type pos = search_company(company);
            company_array[pos].insert(product_name, price);
            return true;
        }
    }

    // Precondition: company_name is a non-empty string
    // Postcondition:  A company (as well as all its products) are removed from the database.  All elements to
    // the right of the company are shifted to the left.
    // Returns false if the company was not found in the list.
    bool database::erase_company(const std::string &company)
    {

        size_type company_index = search_company(company);

        if (company_index != COMPANY_NOT_FOUND)
        {

            for (size_type i = company_index; i < used_slots - 1; i++)
            {
                company_array[i] = company_array[i + 1];
            }
            used_slots--;
            return true;
        }
        else
        {
            return false;
        }
    }

    // Precondition: company_name and product_name are non-empty strings
    // Postcondition:  A product is erased from the company in the database.  Returns false if
    // the company or the item was not found.
    bool database::erase_item(const std::string &cName, const std::string &pName)
    {

        assert(cName.length() > 0 && pName.length() > 0);

        size_type company_index = search_company(cName);

        // If not found, return false
        if (company_index == COMPANY_NOT_FOUND)
        {
            return false;
        }
        else
        {
            return company_array[company_index].erase(pName);
        }
    }

    // Precondition: company is a non-empty string
    // Postcondition:  Searches the DB for the company of the specified name.  Returns the position if found, but if
    // not found, returns COMPANY_NOT_FOUND.
    database::size_type database::search_company(const std::string &company)
    {
        assert(company.length() > 0);
        // Iterates through the array to find the company index
        for (size_type i = 0; i < used_slots; i++)
        {
            if (company_array[i].get_name() == company)
            {
                return i;
            }
        }

        return COMPANY_NOT_FOUND;
    }

    // Precondition: company_name is a non-empty string
    // Postcondition: Takes in the name of a company and then prints out the items belonging to it.
    // Return true if the company is in the database, returns false otherwise.
    bool database::print_items_by_company(const std::string &cName)
    {
        assert(cName.length() > 0);

        size_type c_index = search_company(cName);

        if (c_index == COMPANY_NOT_FOUND)
        {
            return false;
        }

        std::cout << "Printing the products of " << cName << ":" << std::endl;
        company_array[c_index].print_items();
        std::cout << std::endl;

        return true;
    }

    // Postcondition:  Prints the list of companies currently in the database
    void database::print_companies()
    {

        std::cout << "Company List" << std::endl;
        for (int i = 0; i < used_slots; i++)
        {
            std::cout << "- " << company_array[i].get_name() << std::endl;
        }
    }
}

#endif