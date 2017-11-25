#!/usr/bin/env python3
import sys
import winsound
import threading
import time
from modules.virtual_chip8 import Virtual_chip8
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from modules.gui import Gui


wait_to_key_command = ('f', '0a')
threads = []


def main():
    if len(sys.argv) < 2:
        print('There are no arguments for start\
                write at least the name of the game')
        sys.exit()
    name = sys.argv[1]
    debug, registers, memory = parse_args(sys.argv)
    with open('{0}'.format(name), 'rb') as file:
        start(file, debug, registers, memory)
    return


def parse_args(args):
    debug = False
    registers = False
    memory = False
    for i in range(2, len(args)):
        if args[i].lower() == 'd':
            debug = True
        elif args[i].lower() == 'r':
            registers = True
        elif args[i].lower() == 'm':
            memory = True
        elif args[i].lower() == 'h':
            print('if you want debug then:\n\
                   print "d" for main info\n\
                   print "r" for registers info\n\
                   print "m" for memory info')
            sys.exit()
        else:
            print('There are no such command: {0}'.format(args[i].lower()))
            sys.exit()
    return (debug, registers, memory)


def start(file, debug, registers, memory):
    vc8 = Virtual_chip8()
    app = QApplication([])
    gui = Gui(vc8)
    sys.exit(app.exec_())
    load_memory(file, vc8)

    thread_print = threading.Thread(target=print_field,
                                    args=(gui, app))
    thread_execute = threading.Thread(target=execute,
                                      args=(vc8, debug, registers, memory))

    thread_execute.start()
    thread_print.start()

    threads.append(thread_execute)
    threads.append(thread_print)
    return


def execute(vc8, debug, registers, memory):
    prev_pc = vc8.pc
    while vc8.pc < vc8.memory_limit:
        command = get_command(vc8)
        treat_tick(vc8, debug, registers, memory, command)
        key_command = (command[0], command[2:])
        while (key_command == wait_to_key_command and
                vc8.pressed_key not in vc8.keys):
            time.sleep(0.5)
        vc8.compare_and_execute(command)
        if vc8.pc == prev_pc:
            time.sleep(5)
            print('GAME OVER!')
            for thread in threads:
                sys.exit(thread)
        else:
            prev_pc = vc8.pc
        time.sleep(1 / vc8.speed)
        gui.print_field()
    return


def load_memory(file, vc8):
    counter = 0
    temp_num = ''
    for line in file.readlines():
        for num in line:
            temp_num = hex(num)
            if len(temp_num) < 4:
                temp_num = '0x0' + temp_num[2]
            vc8.memory[counter + vc8.shift] = temp_num
            counter += 1
    return


def get_command(vc8):
    command = vc8.memory[vc8.pc] + vc8.memory[vc8.pc + 1]
    command = command.replace('0x', '')
    command = '0x' + command
    return command


def treat_tick(vc8, debug, registers, memory, command):
    if vc8.sound_timer > 0:
        winsound.Beep(1000, 100)
        vc8.sound_timer -= 1
    if vc8.delay_timer > 0:
        vc8.delay_timer -= 1
    if debug:
        print("PC: {0}, I: {1}, delay: {2}, sound: {3} command: {4}"
              .format(vc8.pc, vc8.i, vc8.delay_timer, vc8.sound_timer,
                      command))
    if registers:
        print(vc8.registers)
    if memory:
        print(vc8.memory)
    return


def print_field(gui, app):
    gui.print_field()
    QtCore.QCoreApplication.processEvents()
    return

if __name__ == "__main__":
    main()
