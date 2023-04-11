/* A_1 Devansh Agrahari EXP-08 */
/* By default, number of frames == 3*/

#include <stdio.h>
#define MAXSIZE 3

int queue[MAXSIZE];

int front = -1;
int rear = -1;
int size = -1;

// If empty return size<0
// If full return size==MAXSIZE
// If front return Q[front]

void enqueue(int value)
{
    if(size<MAXSIZE)
    {
        if(size<0)
        {
            queue[0] = value;
            front = rear = 0;
            size = 1;
        }
        else if(rear == MAXSIZE-1)
        {
            queue[0] = value;
            rear = 0;
            size++;
        }
        else
        {
            queue[rear+1] = value;
            rear++;
            size++;
        }
    }
    else
    {
        printf("Queue is full\n");
    }
}

int dequeue()
{
    if(size<0)
    {
        printf("Queue is empty\n");
    }
    else
    {
        size--;
        front++;
    }
    return 0;
}

void display()
{
    int i;
    if(rear>=front)
    {
        for(i=front;i<=rear;i++)
        {
            printf("%d ",queue[i]);
        }
    }
    else
    {
        for(i=front;i<MAXSIZE;i++)
        {
            printf("%d ",queue[i]);
        }
        for(i=0;i<=rear;i++)
        {
            printf("%d ",queue[i]);
        }
    }
}

int main()
{
    int i, j, sizeQ, sizeRef, value;
    int Ref_string[20] = {7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3};
    char Solution[20];
    int faults=0, hits=0;
    sizeQ = MAXSIZE;  /*Size of Q or Frames */
    sizeRef = 12;  /* Size of the Reference String */

    for(i=0; i < sizeQ; i++)
    {
        enqueue(Ref_string[i]);
        Solution[i] = 'F';
    }

    for(i=3; i< sizeRef;)
    {
        for(j=0; j<sizeQ;j++)
        {
            if (Ref_string[i] == queue[j])
            {
                Solution[i] = 'H';
                i++;
            }
            else
            {
                dequeue();
                enqueue(Ref_string[i]);
                Solution[i] = 'F';
                i++;
            }
        }
    }
    printf("\n");
    for(i=0; i < sizeRef; i++){
        printf("%c ", Solution[i]);
    }

    for(i=0;i<sizeRef;i++)
    {
        if (Solution[i] == 'H')
        {
            hits++;
        } else{
            faults++;
        }
    }
    float fratio = (float)faults/(float)sizeRef;
    float hratio = (float)hits/(float)sizeRef;
    printf("\nNo of Faults: %d\nNo of Hits: %d\nRatio of Faults: %.1f\nRatio of Hits: %.1f",
           faults, hits, fratio, hratio);

    return 0;
}