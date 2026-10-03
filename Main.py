from dataBase import *


# show doc-string:
if not path.exists(r"Lib\memory\memory_docstring_show.txt"):
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

    with open("Lib\memory\memory_docstring_show.txt", "wb") as m_d_s:
        m_d_s.write(b" This Document just for memory which one more showed doc-string and not showing more.s ")


if sys_type == "windows":
    system("cls")
else:
    system("clear")

print(f"\n\n\n\n\n\n          Please make the opened window'cmd' {green('full screen')}           \n\n\n\n\n\n")
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

    # if have default argument:
    if path.exists(r"Lib\memory\memory_next_number_x2_blocks.txt"):
        with open(r"Lib\memory\memory_next_number_x2_blocks.txt", "rb") as m_n_n:
            lst_memory_next_number = list(m_n_n.readlines())

        value_list.clear()
        value_list.append(len(lst_memory_next_number[0]) - 2)
        value_list.append(len(lst_memory_next_number[1]))

        delet_min_value(int_random(True))  # delet_ min value in board;
        while len(recent) > 0:
            while len(recent) > 0:
                diagnosis_procces(recent[0])
                del recent[0]
            proccecs()

        for itter in range(2):
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

            score()
            print_board_ex()  # Print board

            # random number:
            #     number
            _num = pow(2, value_list[0])
            _len_num = len(str(_num))
            _style = number_style(_num, value_list[0])
            _ra_pri = str(_style[0])
            print(("{" + _style[1](_ra_pri) + "}").center(45 - _len_num + len(_style[1](_ra_pri))))
            #     next number:
            _ra_pri = str(number_style(pow(2, value_list[1])))
            print(" " * 23, f"next: {_ra_pri}".center(22), sep="")

            # player choosing procces:
            print(f"\n\n  Save: ({green('sa')})     Retry: ({red('re')})      Exit: (ex)  ")
            while True:
                choice = inputer()

                if choice > -1:
                    break

                if sure():
                    break

                print("Please be careful in your choice")

            if choice == -1:
                loss_ex_sa_re_breaker = 1
                retry_condition = 1
                break
            if choice == -2:
                loss_ex_sa_re_breaker = 1
                save_condition = 1
                break
            if choice == -3:
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
            if f_index == -2:
                loss_ex_sa_re_breaker = 1
                loss_condition = 1
                break
                # if board[29,34] == value:
            if f_index == -11:
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

                break
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

            del value_list[0]
            value_list.append(int_random()[0])

    if not loss_ex_sa_re_breaker:
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
                _len_num = len(str(_num))
                _style = number_style(_num, value_list[0])
                _ra_pri = str(_style[0])
                print(("{" + _style[1](_ra_pri) + "}").center(45 - _len_num + len(_style[1](_ra_pri))))
                #     next number:
                _ra_pri = str(number_style(pow(2, value_list[1])))
                print(" " * 23, f"next: {_ra_pri}".center(22), sep="")

                # player choosing procces:
                print(f"\n\n  Save: ({green('sa')})     Retry: ({red('re')})      Exit: (ex)  ")
                while True:
                    choice = inputer()

                    if choice > -1:
                        break

                    if sure():
                        break

                    print("Please be careful in your choice")

                if choice == -1:
                    loss_ex_sa_re_breaker = 1
                    retry_condition = 1
                    break
                if choice == -2:
                    loss_ex_sa_re_breaker = 1
                    save_condition = 1
                    break
                if choice == -3:
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

    if save_condition == 1:
        # save board values:
        with open(r"Lib\memory\memory_board_x2_blocks.txt", "wb") as mem:
            i = 0
            while i < 35:
                if board[i] == 0:
                    mem.write(b"\r\n")
                    i += 1
                    continue
                mem.write((b"*" * board[i]) + b"\r\n")
                i += 1

        # save next_values:
        if len(value_list) < 2:
            value_list.append(int_random()[0])
            if len(value_list) < 2:
                value_list.append(int_random()[0])
        with open(r"Lib\memory\memory_next_number_x2_blocks.txt", "wb") as m_n_n:
            # noinspection PyUnboundLocalVariable
            m_n_n.write(b"*" * value_list[0] + b"\r\n")
            m_n_n.write(b"*" * value_list[1])

        # save counter_score:
        csn = counter_score_()  # counter_score_number;
        if csn > 0:
            with open(r"Lib\memory\memory_counter_score_x2_blocks.txt", "wb") as m_c_s:
                while csn > 0:
                    m_c_s.write((b"*" * (csn % 10)) + b"\r\n")
                    csn = csn // 10
        print("\n")
    elif loss_condition == 1:
        # delet board:
        if path.exists(r"Lib\memory\memory_board_x2_blocks.txt"):
            remove(r"Lib\memory\memory_board_x2_blocks.txt")
        # delet counter_score:
        if path.exists(r"Lib\memory\memory_counter_score_x2_blocks.txt"):
            remove(r"Lib\memory\memory_counter_score_x2_blocks.txt")
        # delet next_value:
        if path.exists(r"Lib\memory\memory_next_number_x2_blocks.txt"):
            remove(r"Lib\memory\memory_next_number_x2_blocks.txt")
        print("\n\n\t You LOSS !!! ")

        sleep(1)
        print("\n")
        _re = input("\tDo you want to try again?  (y / n): ")

        if _re.lower() == "y":
            continue
    elif retry_condition == 1:
        recent.clear()
        clear_database()

        loss_ex_sa_re_breaker = 0
        loss_condition = 0
        save_condition = 0
        retry_condition = 0
        value_list.clear()

        # delet board:
        if path.exists(r"Lib\memory\memory_board_x2_blocks.txt"):
            remove(r"Lib\memory\memory_board_x2_blocks.txt")
        # delet counter_score:
        if path.exists(r"Lib\memory\memory_counter_score_x2_blocks.txt"):
            remove(r"Lib\memory\memory_counter_score_x2_blocks.txt")
        # delet next_value:
        if path.exists(r"Lib\memory\memory_next_number_x2_blocks.txt"):
            remove(r"Lib\memory\memory_next_number_x2_blocks.txt")

        continue
    # EXIT:
    else:
        print("\n")

    # The end:
    print("\t Good Luck ... \n\n")
    sleep(1.5)
    break
