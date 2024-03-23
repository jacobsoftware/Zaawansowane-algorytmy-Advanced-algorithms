import time 
import random
import heapq

def sort_func(table,r):
    start_time = time.time()

    table.sort()
    mid = table[int((float((pow(10,r)))/2))-1]

    end_time = time.time()
    time_spent = end_time - start_time
    time_spent = float("{:.2f}".format(time_spent))

    # print('sortowanie:', time_spent)
    # print(mid)
    output_list = (time_spent,mid)
    return output_list 


def queue_func(table,r):
    start_time = time.time()

    heapq.heapify(table)
    smallest = heapq.nsmallest(int((float((pow(10,r)))/2)),table)
    mid = smallest[-1]

    end_time = time.time()
    time_spent = end_time - start_time
    time_spent = float("{:.2f}".format(time_spent))
    # print('kolejka p:',time_spent)
    # print(mid)
    output_list = (time_spent,mid)
    return output_list 

def hoare_func(table,r):
    start_time = time.time()

    quick_sort(table,0,len(table)-1)
    mid = table[int((float((pow(10,r)))/2))-1]

    end_time = time.time()
    time_spent = end_time - start_time
    time_spent = float("{:.2f}".format(time_spent))

    # print("Hoare'a:",time_spent)
    # print(mid)
    output_list = (time_spent,mid)
    return output_list

def mp_func(table,r):
    start_time = time.time()   

    length = int((len(table)/2)-1)
    mid = magic_fives(table,length)

    end_time = time.time()
    time_spent = end_time - start_time
    time_spent = float("{:.2f}".format(time_spent))

    # print("MP:",time_spent)
    # print(mid)
    output_list = (time_spent,mid)
    return output_list

def run():

    for r in range(1,100):
        print(f'rozmiar: 10^{r}')
        table_base = [0] * pow(10,r)

        #tab2 = random.sample(range(1,pow(10,r)+1),pow(10,r))

        for i in range(0,pow(10,r)):            
            table_base[i] = random.randint(1,pow(10,r))

        if r==1:
            string = ''
            for i in range(0,10):
                string = string + str(table_base[i]) + ' '
            print(string)
        
        table_one = table_base[:]
        table_two = table_base[:]
        table_three = table_base[:]
        table_four = table_base[:]

        sort_over_60 = False
        queue_over_60 = False
        hoare_over_60 = False
        mp_over_60 = False

        if sort_over_60 and queue_over_60 and hoare_over_60 and mp_over_60:
            break

        else: 
            if sort_over_60:
                print('sortowanie: 60+')
                print('?')
            else:
                sort_list = sort_func(table_one,r)
                if sort_list[0] > 60:
                    sort_over_60 = True
                    print('sortowanie: 60+')
                    print('?')
                else:
                    print('sortowanie:',sort_list[0])
                    print(sort_list[1])

            if queue_over_60:
                print('kolejka p: 60+')
                print('?')
            else:
                queue_list = queue_func(table_two,r)
                if queue_list[0] > 60:
                    queue_over_60 = True
                    print('kolejka p: 60+')
                    print('?')
                else:
                    print('kolejka p:',queue_list[0])
                    print(queue_list[1])


            if hoare_over_60:
                print("Hoare'a: 60+")
                print('?')
            else:
                hoare_list = hoare_func(table_three,r)
                if hoare_list[0] > 60:
                    hoare_over_60 = True
                    print("Hoare'a: 60+")
                    print('?')
                else:
                    print("Hoare'a:",hoare_list[0])
                    print(hoare_list[1])


            if mp_over_60:
                print('MP: 60+')
                print('?')
            else:
                mp_list = mp_func(table_four,r)
                if mp_list[0] > 60:
                    mp_over_60 = True
                    print('MP: 60+')
                    print('?')
                else:
                    print('MP:',mp_list[0])
                    print(mp_list[1])



def partition(arr, low, high): 
    pivot = arr[high]  
    i = (low - 1) 
    for j in range(low, high): 
        if arr[j] <= pivot: 
            i += 1 
            arr[i], arr[j] = arr[j], arr[i] 
    arr[i + 1], arr[high] = arr[high], arr[i + 1] 
    return (i + 1) 
      
def quick_sort(arr, low, high): 
    if low < high: 
        pi = partition(arr, low, high) 
        quick_sort(arr, low, pi - 1) 
        quick_sort(arr, pi + 1, high) 

def magic_fives(table, length):

    if len(table) <= 10:

        table.sort()
        return table[length]
    else:

        P = [table[i:i+5] for i in range(0, len(table), 5)]
        medians = [sorted(p)[len(p) // 2] for p in P]        
        x = magic_fives(medians, len(medians) // 2)
        less_than_x = [a for a in table if a < x]
        equal_to_x = [a for a in table if a == x]
        greater_than_x = [a for a in table if a > x]  

        if length < len(less_than_x):
            return magic_fives(less_than_x, length)
        elif length < len(less_than_x) + len(equal_to_x):
            return x
        else:
            return magic_fives(greater_than_x, length - len(less_than_x) - len(equal_to_x))



if __name__ == '__main__':
    run()