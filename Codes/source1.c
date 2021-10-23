// stack using array menu driven program
#include <stdio.h>
#include <stdlib.h>
int top = -1;
int stack[50];
int size;
void display()
{
    if (top == -1)
        printf("\nStack is empty\n");
    else
    {
        printf("The Stack is:\n");
        printf("->%d", stack[top]);
        for (int i = top - 1; i >= 0; i--)
        {
            printf("\n%d", stack[i]);
        }
    }
}

void check_empty()
{
    if (top == -1)
    {
        printf("\nThe stack is empty\n");
    }

    else
    {
        printf("\nStack not empty\nDisplaying the stack:\n");
        display();
    }
}

void push()
{
    int ele;

    printf("Enter element:");
    scanf("%d", &ele);
    if (top == size - 1)
    {
        printf("Overflow!!Stack Full");
    }
    else
    {
        top++;
        stack[top] = ele;
    }
}

int pop()
{
    int item;
    item = stack[top];
    top--;
    return item;
}

int main()
{
    system("cls");
    printf("Enter size of the stack:");
    scanf("%d", &size);
    int ch;
    do
    {
        printf("\n\n\t\tSTACK\n");
        printf("1.Check if Stack is empty\n");
        printf("2.Display the contents of Stack\n");
        printf("3.Push\n");
        printf("4.Pop\n");
        printf("5.Exit");
        printf("\nEnter choice(1-5):");
        scanf("%d", &ch);
        switch (ch)
        {
        case 1:
            check_empty();
            break;
        case 2:
            display();
            break;
        case 3:
            push();
            break;
        case 4:
            printf("Deleted element:%d", pop());
            break;
        case 5:
            exit(1);
            break;
        default:
            printf("Wrong input ...try again!!!");
        }
    } while (ch);
    return 0;
}