from  statistics import *

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average(num_list)
    find_min_max(num_list)
    sort_temperature(num_list)
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
def get_user_input():
    numbers = input("Enter your values: ")
    numberslist = numbers.split(", ")
    temp = []
    for number in numberslist:
        temp += [float(number)]

    numberslist = temp

    #print(numberslist)
    return numberslist
def calc_average(numberslist):
    average = sum(numberslist) / len(numberslist)

    #print(average)
    return average
def find_min_max(numberslist):
    minmaxtemp = [int(min(numberslist)), int(max(numberslist))]

    #print(minmaxtemp)
    return minmaxtemp
def sort_temperature(numberslist):
    sortednumberslist = sorted(numberslist)

    #print(sortednumberslist)
    return sortednumberslist

if __name__ == "__main__":
    main()