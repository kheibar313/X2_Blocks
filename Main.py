from random import random
from os import system, path, remove
from time import sleep
from platform import uname

sys_type = (uname()[0]).lower()

recent = []
_extra_print = 1
counter_score = 0
_recent_outcums = []
global board
# noinspection PyRedeclaration
board = [
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0
]


def clear_database():
    global _extra_print
    _extra_print = 1

    global counter_score
    counter_score = 0

    global _recent_outcums
    _recent_outcums = []

    global board
    board = [
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0
    ]

    return True


def counter_score_():
    return counter_score


def delet_(index):
    _index1 = index
    _index2 = index + 5
    while True:
        if _index2 > 34:
            board[_index1] = 0
            return True

        board[_index1] = board[_index2]
        recent.append(_index1)
        _index1 += 5
        _index2 += 5
    return None


def delet_min_value(start):
    _delet_min_value_buffer = []
    _index_counter = 34
    while _index_counter > -1:
        if board[_index_counter] < start:
            delet_(_index_counter)
            _delet_min_value_buffer.extend([(_index_counter - 5), (_index_counter - 1), _index_counter,
                                            (_index_counter + 1), (_index_counter + 5)])
        _index_counter -= 1

    _dmvb_len = len(_delet_min_value_buffer)
    _itterable = 0
    while _itterable < _dmvb_len:
        if -1 < _delet_min_value_buffer[_itterable]:
            if _delet_min_value_buffer[_itterable] < 35:
                if not (_delet_min_value_buffer[_itterable] in recent):
                    recent.append(_delet_min_value_buffer[_itterable])
        _itterable += 1

    return True


def find_index(choice, value):
    _column_list = [
        board[(choice + 29)],
        board[(choice + 24)],
        board[(choice + 19)],
        board[(choice + 14)],
        board[(choice + 9)],
        board[(choice + 4)],
        board[(choice - 1)]
    ]

    # The first row Occupied:
    if _column_list[0] != 0:
        # The first row is value:
        if _column_list[0] == value:
            board[(choice + 29)] += 1
            recent.append((choice + 29))
            return -11

        # The first row Occupied but isn't vlue:
        if 0 in board:
            return -3
        _row_list = [
            board[30],
            board[31],
            board[32],
            board[33],
            board[34],
        ]
        if value in _row_list:
            return -3
        return -2

    # Main find_index():
    _itterable = 0
    while _itterable < 7:
        if _column_list[_itterable] == 0:
            _itterable += 1
            continue
        __index = ((choice - 1) + ((7 - _itterable) * 5))
        board[__index] = value
        time_break()
        board[__index] = 0
        recent.append(__index)
        return True
    else:
        board[(choice - 1)] = value
        time_break()
        board[(choice - 1)] = 0
        recent.append((choice - 1))
        print("recent2", recent)
        return choice - 1


def inputer():
    print(f"\n Enter Choice[1,5]: ", end="")
    choice = input()
    # Breaker by input string("exit")
    if choice.lower() == "exit":
        return -1
    # Breaker by input string("exit")
    if choice.lower() == "ex":
        return -1
    # Checking True Number:
    if choice.isnumeric():
        if 0 < int(choice) < 6:
            return int(choice)
    # If Number is not True !!
    print(" Enter True number in range[1,5] ! ")
    return inputer()


def _lst_random_():
    def diagnosis(_index):
        # column_0:
        if _index % 5 == 0:
            if board[(_index + 1)] == 0:
                if _index < 5:
                    return True
                if board[(_index - 4)] != 0:
                    return True
            return False
        # column_5:
        if _index % 5 == 4:
            if board[(_index - 1)] == 0:
                if _index < 5:
                    return True
                if board[(_index - 6)] != 0:
                    return True
            return False
        if board[(_index - 1)] == 0:
            if _index < 5:
                return True
            if board[(_index - 6)] != 0:
                return True
        if board[(_index + 1)] == 0:
            if _index < 5:
                return True
            if board[(_index - 4)]:
                return True

    len_lst = 0
    _index_list = []
    _column_index_memory = []
    column_value_memory = []

    zero_counter = 0
    _itterable = 34
    while _itterable > -1:
        if board[_itterable] == 0:
            zero_counter += 1
            _itterable -= 1
            continue

        # Up columns:
        if _itterable % 5 not in _column_index_memory:
            if board[_itterable] not in column_value_memory:
                _index_list.append(_itterable)
                len_lst += 1
                _column_index_memory.append((_itterable % 5))
                column_value_memory.append(board[_itterable])
                _itterable -= 1
                continue

        # Others index:
        if board[_itterable] != 0:
            if board[_itterable] not in column_value_memory:
                if diagnosis(_itterable):
                    _index_list.append(_itterable)
                    len_lst += 1
                    _column_index_memory.append((_itterable % 5))
                    column_value_memory.append(board[_itterable])

        _itterable -= 1

    return list([column_value_memory, len_lst, zero_counter])


def int_random(condition=None):
    def start_():
        _mb = max(board)

        if _mb > 15:
            return _mb - 12
        if _mb > 13:
            return 3
        if _mb > 10:
            return 2
        # if mb<11:
        return 1

    start = start_()
    # Just return (start):
    if not (condition is None):
        return start

    _low = 2
    _high = 5
    __lst_random = _lst_random_()
    if __lst_random[2] < 5:
        _low = 4
        _high = 5

    _val = [_high, _high, _high, _high, _high, _high]
    counter_ = 0
    _itterable = 0
    while _itterable < __lst_random[1]:
        if __lst_random[0][_itterable] > (start - 1):
            if __lst_random[0][_itterable] < (start + 6):
                _val[(__lst_random[0][_itterable] - start)] = _low
                counter_ += 1
        _itterable += 1

    main_random_list = []
    _ju_for_re = start
    for _value in _val:
        _itterable = 0
        while _itterable < _value:
            main_random_list.append(_ju_for_re)
            _itterable += 1
        _ju_for_re += 1

    _ran = int(random() * ((_high * 6) - (counter_ * (_high - _low))))
    return list([main_random_list[_ran], start])


def print_board(ex0=None):
    # Upgrade start base_random_int :
    if ex0 is not None:
        print("\n", f"Good job, you Arrived to {ex0}".center(45), "\n")

    print("   [1]      [2]      [3]      [4]      [5]   ")

    # Main_Print:
    mb = max(board)
    if mb == 0:
        mb = 1
    for _itterable in range(7):
        # if board[index] == max(board)
        print("\n  ", end="")
        for __itterable in range(5):
            up = "     "
            if board[((_itterable * 5) + __itterable)] == mb:
                up = "  *  "
            print(up, "   ", end="")

        # Main_Print:
        print("\n  ", end="")
        for __itterable in range(5):
            __index = ((_itterable * 5) + __itterable)

            style = number_style(pow(2, board[__index]), board[__index])
            number = str(style).center(5)
            if board[__index] == 0:
                number = " [_] "

            print(number, "   ", end="")
        print()
    print()


def print_board_ex():
    global _extra_print
    _start = int_random(True)
    if _start > _extra_print:
        _extra_print = _start
        print_board(pow(2, _extra_print))
        return True
    print_board()
    return False


def number_style(number, num_pow=None):
    if number < 1000:
        return str(number)

    _index_dict = {1: "K", 2: "M", 3: "T"}
    _index_list = range(97, 123)
    _number_len = (len(str(number)) - 1) // 3

    if 0 < _number_len < 4:
        return str(number // (1000 ** _number_len)) + _index_dict[_number_len]
    return str(number // (1000 ** _number_len)) + chr(_index_list[(_number_len - 4)])


def score():
    _mb = max(board)
    _mb_num = number_style(pow(2, _mb), _mb)
    _len_num = len(str(_mb_num))

    _i_f_cs = counter_score
    if counter_score > 999999:
        _counter_score_len = len(str(counter_score))
        _i_f_cs = str(counter_score // (10 ** (_counter_score_len - 6))) + ".e" + str(_counter_score_len - 6)

    print("  ", ("High_Value:").center(21 - _len_num), f"Score:{_i_f_cs}".center(20), sep="")
    print()


def sure():
    while True:
        _condition = input("\n  Are you sure? (y/n): ")

        if _condition.lower() == "n":
            return False
        if _condition.lower() == "y":
            return True

        print("   Enter True value !!! ")


def time_break():
    if sys_type == "windows":
        system("cls")
    else:
        system("clear")
    score()
    print_board()
    sleep(0.35)
    return True


def proccecs():
    global _recent_outcums

    if len(_recent_outcums) == 0:
        return None

    # (#name_tag), prioritize:
    _recent_outcums = sorted(_recent_outcums, key=lambda x: x[0][0])

    # edited recent_outcums  ==is==  rec_out :
    rec_out = [_recent_outcums[0], ]
    # for diagnosis is bad chance and have better chance is rec_out;
    memory_set = {-1, }
    memory_set = memory_set.union(_recent_outcums[0][0][1])
    memory_set.discard(-1)  # Because system diagnosis is set and not dictionary.
    del _recent_outcums[0]
    # more element in recent_outcums :
    while 0 < len(_recent_outcums):
        if _recent_outcums[0][0][1].intersection(memory_set):
            del _recent_outcums[0]
            continue
        memory_set = memory_set.union(_recent_outcums[0][0][1])
        rec_out.append(_recent_outcums[0])
        del _recent_outcums[0]

    _rec_out_len = len(rec_out)

    # increasing:
    _itterable = 0
    while _itterable < _rec_out_len:
        board[rec_out[_itterable][1][0]] += rec_out[_itterable][1][1]
        _itterable += 1

    # (Recent) appending:
    _itterable = 0
    while _itterable < _rec_out_len:
        __itterable = 0
        while __itterable < len(rec_out[_itterable][3]):
            if rec_out[_itterable][3][__itterable] < 35:
                if rec_out[_itterable][3][__itterable] > -1:
                    recent.append(rec_out[_itterable][3][__itterable])
            __itterable += 1
        _itterable += 1

    # change to zero:
    _itterable = 0
    _mem_del = []
    while _itterable < _rec_out_len:
        __itterable = 0
        while __itterable < len(rec_out[_itterable][2]):
            board[rec_out[_itterable][2][__itterable]] = 0
            _mem_del.append(rec_out[_itterable][2][__itterable])
            __itterable += 1
        # while counter_condition ;
        _itterable += 1

    # delet_:
    sorted(_mem_del)
    _reverse_itterable = len(_mem_del) - 1
    while -1 < _reverse_itterable:
        delet_(_mem_del[_reverse_itterable])
        _reverse_itterable -= 1

    # score adding:
    global counter_score
    _itterable = 0
    while _itterable < _rec_out_len:
        counter_score += rec_out[_itterable][4][0] * rec_out[_itterable][4][1]
        _itterable += 1

    # The index which extra added in delet_()while :
    recent0 = []
    _itterable = 0
    while _itterable < len(recent):
        if recent[_itterable] in recent0:
            del recent[_itterable]
            continue
        recent0.append(recent[_itterable])
        _itterable += 1

    return list([rec_out, _rec_out_len])


def diagnosis_procces(index, value=None):
    if value is None:
        value = board[index]
    # If in recent, value==[] --> return None
    if value == 0:
        return None

    # Find place:
    # down - left - right - up

    def _sides_diagnosis_list(index0, value0):
        __cfs = 0
        __index_mode_5 = index0 % 5
        __sides_diagnosis_list = [0, 0, 0, 0]

        # Down condition:
        if index0 > 4:
            if board[(index0 - 5)] == value0:
                __sides_diagnosis_list[0] = 1
                __cfs += 1
        # Left condition:
        if __index_mode_5 != 0:
            if board[(index0 - 1)] == value0:
                __sides_diagnosis_list[1] = 1
                __cfs += 1
        # Right condition:
        if __index_mode_5 != 4:
            if board[(index0 + 1)] == value0:
                __sides_diagnosis_list[2] = 1
                __cfs += 1
        # Up condition:
        if index0 < 30:
            if board[(index0 + 5)] == value0:
                __sides_diagnosis_list[3] = 1
                __cfs += 1

        return list([__sides_diagnosis_list, __cfs])

    sides_diagnosis_list = _sides_diagnosis_list(index, value)
    _side_list = sides_diagnosis_list[0]
    _cfs = sides_diagnosis_list[1]

    # appending_to_recent_outcums = [
    #    [#name_tag]:   [(number_value), {index1, index2, ...}] ,
    #    [#increasing]: [index, increase_value]                 ,
    #    [#deleting]:   [index01, index02, ...]                 ,
    #    [#recenting]:  [index001, index002, ...]               ,
    #    [#score]:      [(can be in {1, 3, 7, 15}), value]      ,
    # ]

    global counter_score

    # Nothing
    if _cfs == 0:
        board[index] = value
        return 0

    # One place:
    if _cfs == 1:
        __i_f = 1
        if board[index] == 0:
            __i_f = (value + 1)

        if _side_list == [1, 0, 0, 0]:
            _recent_outcums.append([
                [3, {(index - 5), index}],
                [(index - 5), 1],
                [index],
                [(index - 5), (index - 10), (index - 6), (index - 4), index],
                [1, value],
            ])
            return 11
        if _side_list == [0, 1, 0, 0]:
            _recent_outcums.append([
                [3, {(index - 1), index}],
                [index, __i_f],
                [(index - 1)],
                [index, (index - 1), (index - 5), (index + 1), (index + 5)],
                [1, value],
            ])
            return 12
        if _side_list == [0, 0, 1, 0]:
            _recent_outcums.append([
                [3, {index, (index + 1)}],
                [index, __i_f],
                [(index + 1)],
                [index, (index + 1), (index - 5), (index - 1), (index + 5)],
                [1, value],
            ])
            return 13
        if _side_list == [0, 0, 0, 1]:
            _recent_outcums.append([
                [3, {index, (index + 5)}],
                [index, 1],
                [(index + 5)],
                [index, (index + 5), (index - 5), (index - 1), (index + 1)],
                [1, value],
            ])
            return 14

    # Two place:
    if _cfs == 2:
        __i_f = 2
        if board[index] == 0:
            __i_f = (value + 2)

        if _side_list == [1, 1, 0, 0]:
            _recent_outcums.append([
                [2, {(index - 5), (index - 1), index}],
                [(index - 5), 2],
                [index, (index - 1)],
                [(index - 5), (index - 10), (index - 6), (index - 4), index],
                [3, value],
            ])
            return 21
        if _side_list == [1, 0, 1, 0]:
            _recent_outcums.append([
                [2, {(index - 5), (index + 1), index}],
                [(index - 5), 2],
                [(index + 1), index],
                [(index - 5), (index - 10), (index - 6), (index - 4), index],
                [3, value],
            ])
            return 22
        if _side_list == [1, 0, 0, 1]:
            _recent_outcums.append([
                [2, {(index - 5), index, (index + 5)}],
                [(index - 5), 2],
                [(index + 5), index],
                [(index - 5), (index - 10), (index - 6), (index - 4), index],
                [3, value],
            ])
            return 23
        if _side_list == [0, 1, 1, 0]:
            _recent_outcums.append([
                [2, {(index - 1), index, (index + 1)}],
                [index, __i_f],
                [(index + 1), (index - 1)],
                [(index - 5), index, (index - 1), (index + 1), (index + 5)],
                [3, value],
            ])
            return 24
        if _side_list == [0, 1, 0, 1]:
            _recent_outcums.append([
                [2, {(index - 1), index, (index + 5)}],
                [index, 2],
                [(index + 5), (index - 1)],
                [(index - 5), index, (index - 1), (index + 1), (index + 5)],
                [3, value],
            ])
            return 25
        if _side_list == [0, 0, 1, 1]:
            _recent_outcums.append([
                [2, {index, (index + 1), (index + 5)}],
                [index, 2],
                [(index + 5), (index + 1)],
                [(index - 5), index, (index - 1), (index + 1), (index + 5)],
                [3, value],
            ])
            return 26

    # Three place:
    if _cfs == 3:
        if _side_list == [1, 1, 1, 0]:
            _recent_outcums.append([
                [1, {(index - 5), (index - 1), (index + 1), index}],
                [(index - 5), 3],
                [(index + 1), index, (index - 1)],
                [(index - 10), (index - 5), (index - 6), (index - 4), index],
                [7, value],
            ])
            return 31
        if _side_list == [1, 1, 0, 1]:
            _recent_outcums.append([
                [1, {(index - 5), (index - 1), index, (index + 5)}],
                [(index - 5), 3],
                [(index + 5), index, (index - 1)],
                [(index - 10), (index - 5), (index - 6), (index - 4), index],
                [7, value],
            ])
            return 32
        if _side_list == [1, 0, 1, 1]:
            _recent_outcums.append([
                [1, {(index - 5), index, (index + 1), (index + 5)}],
                [(index - 5), 3],
                [(index + 5), (index + 1), index],
                [(index - 10), (index - 5), (index - 6), (index - 4), index],
                [7, value],
            ])
            return 33
        if _side_list == [0, 1, 1, 1]:
            __i_f = 3
            if board[index] == 0:
                __i_f = (value + 3)
            _recent_outcums.append([
                [1, {(index - 1), index, (index + 1), (index + 5)}],
                [index, __i_f],
                [(index + 5), (index + 1), (index - 1)],
                [index, (index - 1), (index + 1), (index - 5), (index + 5)],
                [7, value],
            ])
            return 34

    # Four place:
    if _cfs == 4:
        _recent_outcums.append([
            [1, {(index - 5), (index - 1), index, (index + 1), (index + 5)}],
            [(index - 5), 4],
            [(index + 5), (index + 1), index, (index - 1)],
            [(index - 10), (index - 5), (index - 6), (index - 4), index],
            [15, value],
        ])
        return 40





# show doc-string:
def ds_x2():
    print(" "*15, "In the name of GOD")
    print("  Hellow,   Welcome to the x2_Blocks \n\n\n  Doc-string:")
    print("     This program is a game and its name is x2_Blocks\n")
    print("     x2_Blocks is based on the power of 2 \n")
    print("     Any neighboring and equal blocks are attracted to each other")
    print("     Of course, being attracted has a special priority")
    print("     Attraction priorities are as follows:")
    print("       1): Maximum 'Attraction'")
    print("       2): Player choice\n")
    print("     Gradually, As the board progresses, the numbers selected by the system ...")
    print("   expand. But the system always switches between 6 powers\n")
    print("     There are more tips that you will notice while playing")
    print("\n\n\n\n\n")

    sleep(2)

    # Did player read notice?
    input("          Did you read the text? (press any character): ")
ds_x2()

if sys_type == "windows":
    system("cls")
else:
    system("clear")

print("\n\n\n\n\n\n          Please make the opened window'cmd' full screen           \n\n\n\n\n\n")
sleep(3)


# procces:
while True:
    if sys_type == "windows":
        system("cls")
    else:
        system("clear")

    # Program Breaker:
    loss_ex_sa_re_breaker = 0
    loss_condition = 0
    save_condition = 0
    retry_condition = 0
    value_list = [int_random()[0], int_random()[0]]

    # Main while:
    while True:
        delet_min_value(int_random(True))  # delet_ min value in board;
        while len(recent) > 0:
            while len(recent) > 0:
                diagnosis_procces(recent[0])
                del recent[0]
            proccecs()

        if sys_type == "windows":
            system("cls")
        else:
            system("clear")

        # checking loss condition:
        if 0 not in board:
            lst0 = [board[34], board[33], board[32], board[31], board[30]]
            if value_list[0] not in lst0:
                loss_ex_sa_re_breaker = 1
                loss_condition = 1
                break

        while True:
            score()
            print_board_ex()  # Print board

            # random number:
            #     number
            _num = pow(2, value_list[0])
            _style = number_style(_num, value_list[0])
            print(f"<{_style}>".center(45))
            #     next number:
            _ra_pri = str(number_style(pow(2, value_list[1])))
            print(" " * 23, f"next: <{_ra_pri}>".center(22), sep="")

            # player choosing procces:
            print("\n\n", "Exit: (ex)          ".center(45), sep="")
            while True:
                choice = inputer()

                if choice > -1:
                    break

                if sure():
                    break

                print("Please be careful in your choice")

            if choice == -1:
                loss_ex_sa_re_breaker = 1
                break

            # find index procces:
            f_index = find_index(choice, value_list[0])

            #     Try again in range(1,5):
            if f_index == -3:
                if sys_type == "windows":
                    system("cls")
                else:
                    system("clear")
                print("\n\n", "Enter True number in range(1,5) !".center(45), "\n")
                continue
                # Loss Breaker:
            elif f_index == -2:
                loss_ex_sa_re_breaker = 1
                loss_condition = 1
                # if board[29,34] == value[0]:
            elif f_index == -11:
                diagnosis_procces(recent[0])
                del recent[0]
                proccecs()
                time_break()

                while len(recent) > 0:
                    while len(recent) > 0:
                        diagnosis_procces(recent[0])
                        del recent[0]
                    proccecs()
                    if len(recent) == 0:
                        if sys_type == "windows":
                            system("cls")
                        else:
                            system("clear")
                        break
                    time_break()
                # Main procces:
            else:
                diagnosis_procces(recent[0], value_list[0])
                del recent[0]
                proccecs()
                time_break()

                while len(recent) > 0:
                    while len(recent) > 0:
                        diagnosis_procces(recent[0])
                        del recent[0]
                    proccecs()
                    if len(recent) == 0:
                        if sys_type == "windows":
                            system("cls")
                        else:
                            system("clear")
                        break
                    time_break()

            recent.clear()
            break

        # main while condition:
        if not loss_ex_sa_re_breaker:
            del value_list[0]
            value_list.append(int_random()[0])
            continue

        break

    if sys_type == "windows":
        system("cls")
    else:
        system("clear")


    # The end:
    print("\t Good Luck ... \n\n")
    sleep(1.5)
    break
