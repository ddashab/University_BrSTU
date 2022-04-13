#include "receipt.h"


void Print(Receipt receipt)
{
    std::cout << "The number is " << receipt.GetNumber() << std::endl;
    std::cout << "The data is " << receipt.GetData() << std::endl;
    std::cout << "The sum is " << receipt.GetSum() << std::endl;
}


int main()
{
    int a = 5;
    Receipt emptyReceipt;
    Receipt myReceipt(213, 31, 888);
    Receipt anyReceipt = myReceipt;
    Receipt staticReceipts [3]{emptyReceipt, myReceipt, anyReceipt};
    Receipt * dynamicReceipts = new Receipt[3];
    dynamicReceipts[0] = emptyReceipt;
    dynamicReceipts[1] = myReceipt;
    dynamicReceipts[2] = anyReceipt;
    Print(dynamicReceipts[0]);
    void (Receipt :: *pf)(int);
    pf = &Receipt :: SetData;
    (dynamicReceipts[0].*pf)(33);
    Print(dynamicReceipts[0]);
    return 0;
}

