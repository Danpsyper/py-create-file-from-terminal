import datetime
import os
import sys

command = sys.argv
command_tag = command[1]

if "-f" in command and "-d" in command:
    names = []
    d_idx = command.index("-d")
    f_idx = command.index("-f")

    if d_idx < f_idx:
        for i in range(d_idx + 1, f_idx):
            names.append(command[i])
    elif d_idx > f_idx:
        for i in range(d_idx + 1, len(command)):
            names.append(command[i])

    full_dir_path = os.path.join(*names)
    os.makedirs(full_dir_path, exist_ok=True)

    trg_file = os.path.join(full_dir_path, command[f_idx + 1])

    file_exists = os.path.exists(trg_file) and os.path.getsize(trg_file) > 0

    with open(trg_file, "a") as f:
        if file_exists:
            f.write("\n")

        f.write(str(datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S")) + "\n")
        running = True
        line = 1
        while running:
            user_input = input("Enter content line: ")
            if user_input == "stop":
                running = False
            else:
                f.write(f"{line} {user_input}\n")
                line += 1

elif command_tag == "-d":
    names = []
    for i in range(2, len(command)):
        names.append(command[i])

    full_dir_path = os.path.join(*names)
    os.makedirs(full_dir_path, exist_ok=True)

elif command_tag == "-f":
    trg_file = command[2]
    file_exists = os.path.exists(trg_file) and os.path.getsize(trg_file) > 0

    with open(trg_file, "a") as f:
        if file_exists:
            f.write("\n")

        f.write(str(datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S")) + "\n")
        line = 1
        running = True
        while running:
            user_input = input("Enter content line: ")
            if user_input == "stop":
                running = False
            else:
                f.write(f"{line} {user_input}\n")
                line += 1
